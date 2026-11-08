"""Bounded mobile requests on the native listener. A light client is never a sync peer."""
import json
import time
from collections import deque

from .address import decode_address
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
        self.calls = deque()
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
        if op in ('work', 'solve'):
            raise ValueError('Remote mining is unavailable')
        chain = self.node.chain
        if op == 'send':
            tx = Transaction.deserialize(bytes.fromhex(req['hex']))
            return {'txid': hash_to_display(chain.submit_transaction(tx))}
        with chain.read_snapshot():
            height = chain._row(chain.tip_hash)[2]
            tip = hash_to_display(chain.tip_hash)
            if op == 'coinbaseproof':
                from .primitives import hash_from_display
                digest = hash_from_display(req['hash'])
                block = chain.get_block(digest)
                coinbase = block.transactions[0].serialize()
                if len(coinbase) > (MAX_REPLY - 8192) // 2:
                    # The ordinary P2P getdata request can carry this one
                    # larger block and does not require any earlier bodies.
                    return {'use_block': True}
                return {'coinbase': coinbase.hex(), 'count': len(block.transactions),
                        'branch': coinbase_branch(block)}
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
            raise ValueError('Unknown operation')

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
