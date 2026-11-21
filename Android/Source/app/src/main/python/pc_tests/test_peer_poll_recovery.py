"""A failed refresh must not leave connected peers permanently stale."""
import asyncio
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from sumuww import peer


async def eventually(predicate, timeout=4):
    async with asyncio.timeout(timeout):
        while not predicate():
            await asyncio.sleep(.01)


class PollRecoveryTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.root = tempfile.TemporaryDirectory(prefix='sumuww-poll-recovery-')
        self.nodes = []
        self.patches = [patch.object(peer, 'HEADER_REFRESH_INTERVAL', .04),
                        patch.object(peer, 'VERIFIED_PEER_FRESHNESS', .15)]
        for value in self.patches:
            value.start()

    async def asyncTearDown(self):
        await asyncio.gather(*(node.stop() for node in self.nodes))
        for value in self.patches:
            value.stop()
        self.root.cleanup()

    async def node(self, name):
        node = peer.PeerNode(Path(self.root.name) / (name + '.sqlite'),
                             host='127.0.0.1', port=0, network='regtest',
                             timeout=1, poll_interval=.01,
                             discover_peers=False, dht_enabled=False)
        self.nodes.append(node)
        await node.start()
        return node

    async def connected(self):
        client, server = await self.node('client'), await self.node('server')
        await client.connect(*server.address)
        await eventually(lambda: client.synchronization_info()['mining_ready'])
        await eventually(lambda: all(not s.header_requested for s in client._sessions.values()))
        return client, server

    async def test_peer_exception_cannot_stop_other_peer_refresh(self):
        client, first = await self.connected()
        second = await self.node('second')
        await client.connect(*second.address)
        await eventually(lambda: client.synchronization_info()['validated_mining_anchors'] == 2)
        original = client._poll_session
        injected = asyncio.Event()

        async def fail_one(session, *args):
            if session.outgoing == first.address and not injected.is_set():
                injected.set()
                raise RuntimeError('injected peer refresh failure')
            return await original(session, *args)

        with patch.object(client, '_poll_session', fail_one):
            await asyncio.wait_for(injected.wait(), 2)
            # Several complete freshness windows, with no new blocks arriving.
            await asyncio.sleep(.65)
            self.assertTrue(client.synchronization_info()['mining_ready'])
            self.assertTrue(any(s.outgoing == second.address and not s.writer.is_closing()
                                for s in client._sessions.values()))

    async def test_one_maintenance_exception_recovers_without_restart(self):
        client, _ = await self.connected()
        original = client._retire_duplicate_transports
        injected = asyncio.Event()

        def fail_once():
            if not injected.is_set():
                injected.set()
                raise OSError('injected temporary maintenance failure')
            return original()

        with patch.object(client, '_retire_duplicate_transports', fail_once):
            await asyncio.wait_for(injected.wait(), 2)
            await asyncio.sleep(.3)
            self.assertFalse(client.synchronization_info()['mining_ready'])
            await eventually(lambda: client.synchronization_info()['mining_ready'])
            await asyncio.sleep(.4)
            self.assertTrue(client.synchronization_info()['mining_ready'])

    async def test_repeated_failure_never_fakes_freshness_and_shutdown_stops_retry(self):
        client, _ = await self.connected()
        calls = []

        def fail_always():
            calls.append(asyncio.get_running_loop().time())
            raise OSError('injected persistent maintenance failure')

        with patch.object(client, '_retire_duplicate_transports', fail_always):
            await eventually(lambda: bool(calls))
            await asyncio.sleep(.4)
            self.assertFalse(client.synchronization_info()['mining_ready'])
            await client.stop()
            count = len(calls)
            await asyncio.sleep(.2)
            self.assertEqual(count, len(calls))
            self.assertFalse(client._tasks)
