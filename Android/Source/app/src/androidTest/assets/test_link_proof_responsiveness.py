"""Expensive public-proof verification must not block the node's event loop."""
import asyncio
import copy
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import patch
from cryptography.exceptions import InvalidSignature

from sumuww import link_beacon as beacon
from sumuww.link_runtime import LinkRuntime
from sumuww.peer import PeerNode
from pc_tests.test_links9000 import LinkUpgradeTests


class ProofResponsivenessTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        LinkUpgradeTests.setUpClass()

    @classmethod
    def tearDownClass(cls):
        LinkUpgradeTests.tearDownClass()

    async def asyncSetUp(self):
        self.fixture = LinkUpgradeTests()
        self.fixture.setUp()
        parent, signature = self.fixture.selected_parent()
        pair = self.fixture.pair(parent, 108)
        self.proof = self.fixture.proof(pair, signature)
        self.runtime = LinkRuntime(SimpleNamespace(chain=self.fixture.chain,
            database=self.fixture.path, timeout=10, _sessions={}))

    async def asyncTearDown(self):
        await self.runtime.close()
        self.fixture.doCleanups()

    async def test_cold_verification_leaves_actor_and_database_responsive(self):
        for cache in (beacon._verify_beacon, beacon._verify_setup, beacon._group, beacon._verify_deal):
            cache.cache_clear()
        owner = threading.get_ident()
        entered, release = threading.Event(), threading.Event()
        original = beacon._verify_deal

        def expensive(*args):
            self.assertNotEqual(owner, threading.get_ident())
            entered.set()
            if not release.wait(5):
                raise RuntimeError('Actor failed to run while proof verification was pending')
            return original(*args)

        with patch.object(beacon, '_verify_deal', side_effect=expensive):
            task = asyncio.create_task(self.runtime.add_proof(self.proof))
            try:
                for _ in range(200):
                    if entered.is_set():break
                    await asyncio.sleep(.01)
                self.assertTrue(entered.is_set())
                self.assertFalse(task.done())
                self.assertEqual(0, len(self.fixture.chain.boundary.all_proofs()))
                self.assertGreater(self.fixture.chain.summary()['height'], 3)
                release.set()
                self.assertTrue(await asyncio.wait_for(task, 60))
            finally:
                release.set()
                if not task.done():task.cancel()
                await asyncio.gather(task, return_exceptions=True)
        self.fixture.chain.boundary.verify_storage()

    async def test_valid_beacon_does_not_bypass_bad_witness_rejection(self):
        bad = copy.deepcopy(self.proof)
        bad['left'] = {'codec': 'raw', 'data': '00' * 96}
        with self.assertRaises(InvalidSignature):
            await self.runtime.add_proof(bad)
        self.assertEqual([], self.fixture.chain.boundary.all_proofs())

    async def test_incomplete_proof_is_rejected_before_expensive_work(self):
        with patch.object(beacon, 'verify_beacon', side_effect=AssertionError('Unexpected BLS work')):
            with self.assertRaises(ValueError):
                await self.runtime.add_proof({'message': self.proof['message']})

    async def test_new_block_setup_does_not_block_network_actor(self):
        entered, release = threading.Event(), threading.Event()
        owner = threading.get_ident()
        original = beacon.verify_setup
        block = self.fixture.chain._path(self.fixture.chain.tip_hash)[3][1]
        def expensive(setup):
            self.assertNotEqual(owner, threading.get_ident())
            entered.set()
            if not release.wait(5):raise RuntimeError('Actor did not respond')
            return original(setup)
        with patch.object(beacon, 'verify_setup', side_effect=expensive):
            task = asyncio.create_task(PeerNode._verify_block_setup(self.runtime.node, block))
            try:
                for _ in range(200):
                    if entered.is_set():break
                    await asyncio.sleep(.01)
                self.assertTrue(entered.is_set())
                self.assertGreater(self.fixture.chain.summary()['height'], 3)
                release.set()
                await asyncio.wait_for(task, 60)
            finally:
                release.set()
                if not task.done():task.cancel()
                await asyncio.gather(task, return_exceptions=True)

    async def test_cancellation_never_commits_partially_verified_proof(self):
        entered, release = threading.Event(), threading.Event()
        def pending(*args):
            entered.set()
            release.wait(5)
        with patch.object(beacon, 'verify_beacon', side_effect=pending):
            task = asyncio.create_task(self.runtime.add_proof(self.proof))
            try:
                for _ in range(200):
                    if entered.is_set():break
                    await asyncio.sleep(.01)
                self.assertTrue(entered.is_set())
                task.cancel()
                with self.assertRaises(asyncio.CancelledError):await task
                self.assertEqual([], self.fixture.chain.boundary.all_proofs())
            finally:
                release.set()
