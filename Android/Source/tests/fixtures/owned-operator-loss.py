"""Lose the only upstream peer, retain the validated chain, then reconnect."""
import asyncio
import json
from pathlib import Path
import tempfile
from sumuww.chain import Chain
from sumuww.peer import PeerNode
from sumuww.wallet import RegtestKey

async def until(predicate):
    async with asyncio.timeout(45):
        while not predicate():
            await asyncio.sleep(0.1)

async def exercise(root):
    first = root / 'operator.sqlite'
    saved = root / 'subscriber.sqlite'
    script = RegtestKey.from_int(77).script_pubkey
    with Chain(first) as chain:
        chain.mine(script, 3)
        tip = chain.tip_hash
    def node(path, **options):
        return PeerNode(path, discover_peers=False, dht_enabled=False,
                        poll_interval=0.15, timeout=3, **options)
    source = node(first)
    follower = None
    try:
        await source.start()
        port = source.address[1]
        follower = node(saved, peers=[source.address])
        await follower.start()
        await until(lambda: follower.chain.tip_hash == tip)
        await source.stop()
        await until(lambda: follower.info()['peers'] == 0)
        assert follower.chain.tip_hash == tip
        await follower.stop()
        with Chain(saved) as reopened:
            assert reopened.tip_hash == tip
        source = node(first, port=port)
        await source.start()
        follower = node(saved, peers=[source.address])
        await follower.start()
        source.chain.mine(script)
        await until(lambda: follower.chain.tip_hash == source.chain.tip_hash)
        return {'passed':True, 'initial_height':3, 'restored_height':follower.chain.summary()['height'],
                'scope':'owned loopback operator, subscriber and temporary regtest chain'}
    finally:
        if follower is not None: await follower.stop()
        await source.stop()

with tempfile.TemporaryDirectory() as directory:
    report = json.dumps(asyncio.run(exercise(Path(directory))))
