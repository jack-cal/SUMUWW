"""Bounded mobile requests on the native listener. A light client is never a sync peer."""
import json
import secrets
import time
from collections import OrderedDict, deque
from dataclasses import replace

from .address import decode_address
from .block import Block
from .fees import estimate_payment_fee, fee_overview
from .primitives import hash_to_display, sha256d
from .rpc import RpcServer
from .transaction import Transaction

MAX_REQUEST = 65536
MAX_REPLY = 131072


def coinbase_branch(block):
    level = [tx.txid() for tx in block.transactions]
    branch = []
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        branch.append(level[1].hex())
        level = [sha256d(a + b) for a, b in zip(level[::2], level[1::2])]
    return branch


class MobileRequests:
    def __init__(self, node):
        self.node = node
        self.jobs = OrderedDict()
        self.calls = deque()
        self.templates = deque()
        self.alert_token = None
        self.alert_rows = {}

    def allow(self, queue, seconds, limit):
        now = time.monotonic()
        while queue and queue[0] <= now - seconds:
            queue.popleft()
        if len(queue) >= limit:
            raise ValueError('Busy')
        queue.append(now)

    def handle(self, body):
        self.allow(self.calls, 1, 24)
        if len(body) > MAX_REQUEST:
            raise ValueError('Oversized request')
        req = json.loads(body)
        if not isinstance(req, dict) or req.get('genesis') != self.node.genesis.hex():
            raise ValueError('Wrong network')
        op = req['op']
        chain = self.node.chain
        if op == 'solve':
            job = self.jobs.get(req['job'])
            nonce = req['nonce']
            if type(nonce) is not int or not 0 <= nonce <= 0xffffffff:
                raise ValueError('Invalid nonce')
            if not job or job[0] < time.monotonic() or chain.tip_hash != job[1].header.previous_hash:
                return {'stale': True}
            block = Block(replace(job[1].header, nonce=nonce), job[1].transactions)
            from .primitives import valid_target
            if int.from_bytes(block.block_hash(), 'little') > valid_target(block.header.bits, chain.network.pow_limit):
                raise ValueError('Insufficient work')
            accepted = chain.accept_block(block)
            self.jobs.pop(req['job'], None)
            return {'accepted': accepted, 'hash': hash_to_display(block.block_hash())}
        if op == 'send':
            tx = Transaction.deserialize(bytes.fromhex(req['hex']))
            return {'txid': hash_to_display(chain.submit_transaction(tx))}
        with chain.read_snapshot():
            height = chain._row(chain.tip_hash)[2]
            tip = hash_to_display(chain.tip_hash)
            if op == 'check':
                points = req['points']
                if not isinstance(points, list) or len(points) > 200:
                    raise ValueError('Too many heights')
                path = chain._path(chain.tip_hash)
                return {'tip': tip, 'height': height, 'hashes': [
                    hash_to_display(path[n][0][0]) if type(n) is int and 0 <= n <= height else None for n in points]}
            address = req.get('address')
            script = decode_address(address, network=chain.network) if address else None
            if op == 'status':
                ready = self.node.synchronization_info()['mining_ready']
                balance = self.coins(chain, 'getaddressbalance', address) if script else None
                return {'tip': tip, 'height': height, 'mining_ready': ready, 'fees': fee_overview(chain), 'balance': balance}
            if script is None:
                raise ValueError('Address required')
            if op == 'alerts':
                rows = self.transfer_alerts(chain, script)
                offset = req['offset']
                if type(offset) is not int or offset < 0:
                    raise ValueError('Invalid offset')
                return {'height': height, 'tip': tip, 'total': len(rows),
                        'floor': max(0,height-144), 'transactions': rows[offset:offset+100]}
            if op == 'quote':
                dest = decode_address(req['to'], network=chain.network)
                estimate = estimate_payment_fee(chain, script, dest, req['amount'], mode=req['mode'], rate=req.get('rate'))
                return {'fee_units': estimate['fee_units'], 'tip': tip}
            if op == 'coins':
                offset = req['offset']
                if type(offset) is not int or not 0 <= offset <= 1000000:
                    raise ValueError('Invalid offset')
                return dict(self.coins(chain, 'listunspent', address, offset=offset, limit=100), tip=tip)
            if op != 'work':
                raise ValueError('Unknown operation')
            if chain.network.name == 'dora' and not self.node.synchronization_info()['mining_ready']:
                return {'waiting': True}
            self.allow(self.templates, 5, 8)
            from .link_crypto import BEACON_TAG, PRODUCER_TAG, producer_output
            from .primitives import merkle_root
            identity_output = producer_output(req['producer'])
            block = chain._block_template(script, extra_nonce=secrets.randbits(32))
            original = block.transactions[0]
            outputs = tuple(identity_output if o.script_pubkey.startswith(b'\x6a\x25' + PRODUCER_TAG)
                            else o for o in original.outputs)
            if len(original.serialize()) > 48000:
                # The optional beacon can exceed a mobile reply budget.
                outputs = tuple(o for o in outputs if not (o.value == 0 and o.script_pubkey[:2] == bytes((106,77))
                                                            and o.script_pubkey[4:9] == BEACON_TAG))
            coinbase = replace(original, outputs=outputs)
            transactions = (coinbase,) + block.transactions[1:]
            root, _ = merkle_root([tx.txid() for tx in transactions])
            block = Block(replace(block.header, merkle_root=root), transactions)
            job_id = secrets.token_hex(16)
            self.jobs[job_id] = (time.monotonic() + 300, block)
            while len(self.jobs) > 8:
                self.jobs.popitem(last=False)
            return {'job': job_id, 'height': height + 1, 'header': block.header.serialize().hex(),
                    'coinbase': block.transactions[0].serialize().hex(), 'branch': coinbase_branch(block)}

    def transfer_alerts(self, chain, script):
        # Build a shared window once per chain/mempool revision. The phone gets only
        # wallet-matching ordinary transfers. A separate stream carries mining receipts.
        token = (chain.tip_hash, chain.connection.execute('SELECT COUNT(*), MAX(id) FROM mempool').fetchone())
        if token != self.alert_token:
            path = chain._path(chain.tip_hash)
            height = len(path)-1
            recent = [(tx,row[2]) for row,block in path[-145:] for tx in block.transactions[1:]]
            recent += [(tx,None) for tx in chain.mempool_transactions()]
            needed = {i.prev_txid for tx,_ in recent for i in tx.inputs}
            inputs = {}
            def collect(tx):
                txid = tx.txid()
                if txid in needed:
                    inputs[txid] = tx.outputs
                    needed.remove(txid)
            for tx,_ in recent:
                collect(tx)
            if needed:
                for _,block in reversed(path):
                    for tx in block.transactions:
                        collect(tx)
                    if not needed:
                        break
            grouped = {}
            for tx,n in reversed(recent):
                delta = {}
                for i in tx.inputs:
                    prev = inputs.get(i.prev_txid, ())
                    if i.prev_index >= len(prev):
                        break
                    out = prev[i.prev_index]
                    delta[out.script_pubkey] = delta.get(out.script_pubkey, 0) - out.value
                else:
                    for out in tx.outputs:
                        delta[out.script_pubkey] = delta.get(out.script_pubkey, 0) + out.value
                    for destination,amount in delta.items():
                        if amount:
                            grouped.setdefault(destination, []).append(dict(txid=hash_to_display(tx.txid()),
                                coinbase=False, net_amount=amount, height=n,
                                status='pending' if n is None else 'confirmed',
                                confirmations=0 if n is None else height-n+1))
            self.alert_token, self.alert_rows = token, grouped
        return self.alert_rows.get(script, [])

    @staticmethod
    def coins(chain, method, address, **fields):
        # Keep address, availability and maturity identical to the local RPC.
        class View:
            _address = staticmethod(RpcServer._address)
        return RpcServer._coins(View(), chain, method, dict(address=address, **fields))
