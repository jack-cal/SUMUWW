"""Explicit, disposable runtime diagnostic; never opens the user's node/wallet."""
import asyncio
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from .chain import Chain
from .peer import PeerNode
from .wallet import RegtestKey
from .boundary_crypto import NodeKeys,BLS,split_signature,verify_split,vrf_verify,canonical

def _selected_pair(chain, pay, keys, setup):
    from . import link_beacon as beacon
    from .link_crypto import proof_selected, slot

    for _ in range(256):
        parent = chain.tip_hash
        height = chain.summary()['height'] + 1
        event = slot(chain.boundary.network, height, parent.hex())
        partials = [beacon.partial(key, setup, event) for key in keys[:2]]
        signature = beacon.combine(setup, event, partials)
        if proof_selected(beacon.verify_beacon(setup, event, signature)):
            first, second = chain.mine(pay, 2)
            assert not chain.boundary.required(height, parent)
            assert not chain.boundary.all_proofs()
            return first, second, height, signature
        chain.mine(pay)
    raise AssertionError('No selected connection-proof event in the regtest sample')


def _seed_with_proof(database, keys):
    from . import link_beacon as beacon
    from .link_crypto import compress, digest, message

    pay = RegtestKey.from_int(1).script_pubkey
    with Chain(database, boundary_activation=3) as chain:
        chain.mine(pay, 2)
        network = chain.boundary.network
        contacts = [key.signed({'domain':'sumuww-link-contact-v1', 'network':network,
                                'nodeId':key.node_id, 'encryption':key.encryption_key}) for key in keys]
        context = beacon.context(network, chain.tip_hash.hex(), contacts)
        manifest = beacon.manifest(context, [beacon.make_deal(key, context) for key in keys])
        ready = sorted((beacon.recover(key, manifest) for key in keys), key=lambda row: row['payload']['nodeId'])
        setup = {'manifest':manifest, 'ready':ready}
        beacon.verify_setup(setup)
        chain.boundary.set_local('ready_setup', setup)
        chain.mine(pay)
        first, second, height, signature = _selected_pair(chain, pay, keys, setup)
        source, target = first.block_hash(), second.block_hash()
        event = message(network, source.hex(), target.hex(), height, first.header.previous_hash.hex(),
                        [key.node_id for key in keys[:3]], signature)
        signatures = [bytes.fromhex(key.sign_once(event['slot'], event)) for key in keys[:3]]
        proof = {'message':event, 'left':compress(b''.join(s[:32] for s in signatures)),
                 'right':compress(b''.join(s[32:] for s in signatures))}
        attachment = {'domain':'sumuww-source-attachment-v1', **proof}
        owner = chain.boundary.identity()
        try:
            proof['source_receipt'] = owner.sign(attachment)
            proof['target_receipt'] = owner.sign({'domain':'sumuww-target-attachment-v1',
                'source_attachment':digest(attachment), 'source_receipt':proof['source_receipt']})
        finally:
            owner.close()
        chain.boundary.add_proof(proof)
        assert chain.boundary.all_proofs() == [proof]
        return target, proof


async def _network(root):
    from contextlib import ExitStack
    from .link_crypto import Identity

    source = root / 'source.sqlite'
    with ExitStack() as stack:
        keys = []
        for i in range(4):
            key = Identity(root / f'witness-{i}.sqlite')
            stack.callback(key.close)
            keys.append(key)
        tip, proof = _seed_with_proof(source, keys)

    nodes = []
    files = [source, root / 'relay.sqlite', root / 'late.sqlite']
    try:
        for db in files:
            node = PeerNode(db, boundary_activation=3, peers=[nodes[-1].address] if nodes else [],
                            discover_peers=False, dht_enabled=False, poll_interval=0.1, timeout=15)
            nodes.append(node)
            await node.start()
        async with asyncio.timeout(120):
            while not all(n.chain.tip_hash == tip and n.chain.boundary.all_proofs() == [proof] for n in nodes):
                await asyncio.sleep(0.1)
        for node in nodes:
            node.chain.boundary.verify_proof(proof)
            assert node._stats['internal_errors'] == 0
    finally:
        for node in reversed(nodes):
            await node.stop()
    for db in files:
        with Chain(db, boundary_activation=3) as reopened:
            assert reopened.tip_hash == tip and reopened.boundary.all_proofs() == [proof]
    return ['valid_selected_block_accepted_without_connection_proof', 'three_witness_signatures',
            'connection_proof_relayed_to_late_peer_over_tcp', 'persisted_proof_restart']


def run():
    checks=[]
    with TemporaryDirectory(prefix='sumuww-boundary-runtime-') as tmp:
        root=Path(tmp)
        with Chain(root/'public-profile.sqlite',network='dora') as chain:
            assert chain.boundary.activation==9000
        checks.append('public_activation_9000')
        keys=NodeKeys(root/'diagnostic-keys.sqlite','disposable-regtest')
        try:
            message=canonical({'domain':'sumuww-disposable-selftest-v1'})
            ticket=keys.ticket(message)
            assert vrf_verify(bytes.fromhex(keys.node_id),bytes.fromhex(ticket['proof']),message).hex()==ticket['output']
            signature=keys.sign_once('disposable',message)
            assert BLS.Verify(keys.public_key,message,signature)
            a,b=split_signature(signature);assert verify_split(signature,a,b)
            assert not BLS.Verify(keys.public_key,message+b'!',signature)
            assert not verify_split(signature,a,a)
            from py_ecc.bls.g2_primitives import G2_to_signature
            from py_ecc.optimized_bls12_381 import Z2
            identity=G2_to_signature(Z2)
            assert not verify_split(signature,signature,identity)
            assert not verify_split(signature,identity,signature)
            checks+=['real_ecvrf','real_bls_and_tamper_rejection','real_group_signature_split']
        finally:keys.close()
        checks+=asyncio.run(_network(root))
    return {'passed':True,'scope':'isolated_loopback_runtime_not_public_network','activation_height':9000,'checks':checks}

def run_json():return json.dumps(run())
