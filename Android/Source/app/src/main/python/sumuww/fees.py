"""Live local queue fee estimates, separate from consensus and signed quotes.

No confirmed-transaction fee history or fee percentiles are used. Price the
space needed by the pending ancestor packages ahead of a new transaction.
Targets are block-capacity budgets (fast 1, normal 3, slow 6), not deadlines.
Only this node's accepted mempool is observable; peers may see a different pool.
"""
from dataclasses import dataclass
from fractions import Fraction
from math import ceil
from weakref import WeakKeyDictionary
from collections import deque
import time

from .block import MAX_BLOCK_WEIGHT, build_coinbase
from .primitives import MAX_MONEY, checked_amount_sum, coinbase_is_mature, require_int, hash_to_display
from .transaction import Transaction, TxInput, TxOutput

INITIAL_RATE = Fraction(1)
MAX_MANUAL_FEE_UNITS = 100_000_000
MAX_AUTO_FEE_UNITS = 1_000_000
TARGET_BLOCKS = {'slow': 6, 'normal': 3, 'fast': 1}
_books = WeakKeyDictionary()
_observations = WeakKeyDictionary()


def virtual_size(transaction):
    return (transaction.weight() + 3) // 4


def _members(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def _pending_book(chain):
    """Snapshot-keyed package order; no signatures, private keys or history scan.

    Recalculate remaining ancestor costs after selecting each package, matching
    mining's package prioritization. A high-fee child cannot omit its parent.
    SQLite's change token invalidates this cache on admissions, RBF and reorgs,
    including writes made by another connection.
    """
    token = (*chain._path_cache_token(), chain.tip_hash)
    cached = _books.get(chain)
    if cached is not None and cached[0] == token:
        return cached[1]
    pool = chain.mempool_transactions()
    indexes = {tx.txid(): i for i, tx in enumerate(pool)}
    needed = list({(item.prev_txid, item.prev_index) for tx in pool for item in tx.inputs
                   if item.prev_txid not in indexes})
    values = {}
    # Read only the confirmed inputs referenced by this bounded pool.
    for offset in range(0, len(needed), 400):
        batch = needed[offset:offset+400]
        placeholders = ','.join('(?,?)' for _ in batch)
        rows = chain.connection.execute(
            'WITH requested(txid,idx) AS (VALUES '+placeholders+') '
            'SELECT u.txid,u.idx,u.value FROM utxos u JOIN requested r '
            'ON u.txid=r.txid AND u.idx=r.idx', [v for point in batch for v in point])
        values.update({(txid, index): value for txid, index, value in rows})
    # Preload outputs so persisted ordering cannot affect fee reconstruction.
    for tx in pool:
        digest = tx.txid()
        values.update({(digest, i): out.value for i, out in enumerate(tx.outputs)})
    costs, masks = [], []
    unresolved = set(range(len(pool)))
    ancestors = [None] * len(pool)
    parents = [{indexes[i.prev_txid] for i in tx.inputs if i.prev_txid in indexes} for tx in pool]
    while unresolved:
        ready = [i for i in sorted(unresolved) if all(ancestors[p] is not None for p in parents[i])]
        if not ready:
            raise ValueError('Invalid mempool dependency graph')
        for i in ready:
            mask = 1 << i
            for parent in parents[i]:mask |= ancestors[parent]
            ancestors[i] = mask
            unresolved.remove(i)
    for tx in pool:
        incoming = checked_amount_sum(values[(i.prev_txid, i.prev_index)] for i in tx.inputs)
        outgoing = checked_amount_sum(o.value for o in tx.outputs)
        if incoming < outgoing:raise ValueError('Invalid mempool fee')
        costs.append((incoming-outgoing, virtual_size(tx), chain._transaction_sigops_cost(tx)))
    masks = ancestors.copy()
    totals = [[sum(costs[j][k] for j in _members(mask)) for k in range(3)] for mask in masks]
    remaining = set(range(len(pool)))
    ordered = []
    while remaining:
        best = max(sorted(remaining), key=lambda i: Fraction(totals[i][0], totals[i][1]))
        mask = masks[best]
        fee, size, sigops = totals[best]
        ordered.append((Fraction(fee, size), size, sigops))
        remaining.difference_update(_members(mask))
        for i in remaining:
            removed = masks[i] & mask
            masks[i] &= ~mask
            for j in _members(removed):
                for k in range(3):totals[i][k] -= costs[j][k]
    path = chain._path(chain.tip_hash)
    coinbase = build_coinbase(len(path), bytes(22), 0, 0, bytes(32), bytes(32))
    coinbase = chain.boundary.template_coinbase(coinbase, path)
    # Header plus maximum compact transaction counter, and current coinbase.
    capacity = (MAX_BLOCK_WEIGHT - coinbase.weight() - 85*4) // 4
    sigops_capacity = 80_000 - chain._transaction_sigops_cost(coinbase)
    book = {'packages': tuple(ordered), 'pending_vsize': sum(c[1] for c in costs),
            'pending_sigops': sum(c[2] for c in costs), 'pending_count': len(pool),
            'block_vsize_capacity': capacity, 'block_sigops_capacity': sigops_capacity,
            'tip': hash_to_display(chain.tip_hash)}
    _books[chain] = (token, book)
    return book


def _queue_rate(book, floor, mode, size):
    if mode not in TARGET_BLOCKS:raise ValueError('Unknown fee mode')
    blocks = TARGET_BLOCKS[mode]
    vbudget = book['block_vsize_capacity'] * blocks - size
    sbudget = book['block_sigops_capacity'] * blocks - 4
    used_vsize = used_sigops = 0
    for price, vsize, sigops in book['packages']:
        # Transactions below the wallet's floor do not compete at that floor.
        if price < floor:continue
        used_vsize += vsize
        used_sigops += sigops
        if used_vsize > vbudget or used_sigops > sbudget:
            # Strictly beat this package, including an exactly equal-rate tie.
            milli = price.numerator * 1000 // price.denominator + 1
            return max(floor, Fraction(milli, 1000))
    return floor


def _suggestion(chain, mode='normal', size=140):
    book = _pending_book(chain)
    floor = max(INITIAL_RATE, Fraction(chain.mempool_policy.minimum_rate, 1000))
    return _queue_rate(book, floor, mode, size), 'live_mempool', book['pending_count']


def fee_overview(chain):
    """Read-only live rate preview, refreshed by each application's status poll.

    Backlog growth is measured over up to 60 seconds of this process's actual
    observations. It is diagnostic only: no extrapolated traffic or historical
    prices are added to the fee. Long observation gaps reset it.
    """
    with chain.read_snapshot():
        book = _pending_book(chain)
        now = time.monotonic()
        observations = _observations.setdefault(chain, deque(maxlen=120))
        if observations and (now < observations[-1][0] or now-observations[-1][0] > 15):
            observations.clear()
        if not observations or now-observations[-1][0] >= .5:
            observations.append((now, book['pending_vsize']))
        while len(observations)>1 and now-observations[0][0] > 60:observations.popleft()
        elapsed = now-observations[0][0]
        growth = None if elapsed < 1 else round((book['pending_vsize']-observations[0][1])/elapsed, 3)
        floor = max(INITIAL_RATE, Fraction(chain.mempool_policy.minimum_rate, 1000))
        return {k:v for k,v in book.items() if k != 'packages'} | {
            'source': 'live_mempool', 'scope': 'local_node', 'amount_unit': 'yugeon',
            'observed_at': int(time.time()), 'backlog_change_vb_per_second': growth,
            'observation_seconds': round(elapsed, 3), 'preview_vsize': 140,
            'rates': {mode:rate_text(_queue_rate(book, floor, mode, 140)) for mode in TARGET_BLOCKS},
            'target_blocks': dict(TARGET_BLOCKS), 'confirmation_time_guaranteed': False}


# Bitcoin Core v31.0 wallet defaults, in smallest units per virtual byte.
WALLET_DISCARD_RATE = Fraction(10)
DUST_RELAY_RATE = Fraction(3)


def minimum_viable_change(output, *, discard_rate=WALLET_DISCARD_RATE,
                          long_term_rate=None, dust_relay_rate=DUST_RELAY_RATE):
    """Wallet change policy for the P2WPKH outputs this wallet can spend."""
    if len(output.script_pubkey) != 22 or output.script_pubkey[:2] != b'\x00\x14':
        raise ValueError('Unsupported wallet change script')
    # Core's GetDiscardRate uses the wallet discard rate when no long-term
    # confirmation estimate is available. SUMUWW estimates its live queue.
    if long_term_rate:
        discard_rate = min(discard_rate, long_term_rate)
    discard_rate = max(discard_rate, dust_relay_rate)
    # Core policy discounts the witness in its 67-vB dust spend template.
    # The wallet estimates 68 vB for a signed P2WPKH input.
    dust = ceil(discard_rate * (len(output.serialize()) + 67))
    return max(dust, ceil(discard_rate * 68) + 1)


@dataclass(frozen=True)
class PaymentPlan:
    transaction: Transaction
    prevouts: tuple
    quote: dict

    def sign(self, key):
        from .wallet import sign_p2wpkh
        tx = self.transaction
        for index, output in enumerate(self.prevouts):
            tx = sign_p2wpkh(tx, index, output, key, low_r=True)
        return tx


def plan_payment(chain, wallet_script, recipient_script, amount_units, *,
                 mode='normal', rate=None, fixed_fee=None, discard_rate=WALLET_DISCARD_RATE):
    """Select inputs and decide outputs once, before signing the reviewed payment."""
    require_int(amount_units, 1, MAX_MONEY)
    if not isinstance(wallet_script, bytes) or not isinstance(recipient_script, bytes):
        raise TypeError('Payment scripts must be bytes')
    from .wallet import LOW_R_SIGNATURE_WITH_HASHTYPE_SIZE
    automatic = fixed_fee is None and rate is None
    cap = MAX_AUTO_FEE_UNITS if automatic else MAX_MANUAL_FEE_UNITS
    with chain.read_snapshot():
        if fixed_fee is not None:
            require_int(fixed_fee, 0, MAX_MONEY)
            if fixed_fee > cap:
                raise ValueError('Manual fee exceeds the wallet fee limit')
            chosen_rate, source, samples = None, 'manual', 0
        elif automatic:
            chosen_rate, source, samples = _suggestion(chain, mode)
        else:
            chosen_rate, source, samples = parse_rate(rate, chain), 'manual_rate', 0

        def requested_fee(size):
            return fixed_fee if fixed_fee is not None else ceil(chosen_rate * size)

        recipient = TxOutput(amount_units, recipient_script)
        change_template = TxOutput(0, wallet_script)
        minimum_change = minimum_viable_change(change_template, discard_rate=discard_rate)
        change_bytes = len(change_template.serialize())
        pending = {i.outpoint() for tx in chain.mempool_transactions() for i in tx.inputs}
        height = chain.info()['height'] + 1
        inputs, prevouts = [], []
        total = 0
        for outpoint, coin in chain.list_utxos(wallet_script):
            txin = TxInput(*outpoint)
            if txin.outpoint() in pending or (coin.coinbase and not coinbase_is_mature(coin.height, height)):
                continue
            inputs.append(txin)
            prevouts.append(coin.output)
            total = checked_amount_sum((total, coin.output.value))
            available = total - amount_units
            if available < 0:
                continue
            # A signed input's maximum witness is used for the estimate only.
            witness = (bytes(LOW_R_SIGNATURE_WITH_HASHTYPE_SIZE), bytes(33))
            padded = tuple(TxInput(i.prev_txid, i.prev_index, witness=witness) for i in inputs)
            size = virtual_size(Transaction(2, padded, (recipient,)))
            single_requested = requested_fee(size)
            if not automatic and single_requested > cap:
                raise ValueError('Manual fee exceeds the wallet fee limit')
            # Core selects on effective input values: size each P2WPKH input
            # separately, then charge the non-input part and change output.
            # Keep the signed-size bound for the fee finally shown to the user.
            selection_fee = fixed_fee
            change_creation_fee = 0
            if fixed_fee is None:
                selection_fee = (len(inputs) * requested_fee(68)
                                 + requested_fee(11 + len(recipient.serialize())))
                change_creation_fee = requested_fee(change_bytes)
            if available < min(max(single_requested, selection_fee), cap):
                continue
            change_requested = requested_fee(size + change_bytes)
            change_fee = min(change_requested, cap)
            selection_change = available - min(selection_fee + change_creation_fee, cap)
            change = available - change_fee
            if min(selection_change, change) >= minimum_change:
                outputs = (recipient, TxOutput(change, wallet_script))
                fee, requested = change_fee, change_requested
                size += change_bytes
            else:
                outputs = (recipient,)
                fee, requested = available, single_requested
            if fee > cap:
                # Another input can make viable change without exceeding the cap.
                continue
            if not automatic and requested > cap:
                raise ValueError('Manual fee exceeds the wallet fee limit')
            if fixed_fee is None and fee < chain.mempool_policy.required_fee(size):
                raise ValueError('Relay minimum exceeds the automatic fee limit')
            quote = {'fee_units': fee, 'estimated_vsize': size, 'source': source,
                     'capped': requested > cap, 'sample_count': samples,
                     'auto_fee_cap_units': MAX_AUTO_FEE_UNITS,
                     'rate_yugeon_per_vb': rate_text(Fraction(fee, size)),
                     'mode': mode, 'amount_unit': 'yugeon',
                     'target_blocks': TARGET_BLOCKS.get(mode) if automatic else None}
            return PaymentPlan(Transaction(2, tuple(inputs), outputs), tuple(prevouts), quote)
        raise ValueError('Insufficient mature confirmed funds after pending spends')


def estimate_payment_fee(chain, wallet_script, recipient_script, amount_units, *, mode='normal', rate=None):
    return plan_payment(chain, wallet_script, recipient_script, amount_units, mode=mode, rate=rate).quote


def rate_text(rate):
    milli = (rate.numerator * 1000 + rate.denominator - 1) // rate.denominator
    return f'{milli // 1000}.{milli % 1000:03d}'.rstrip('0').rstrip('.')


def parse_rate(text, chain):
    import re
    if type(text) is not str or re.fullmatch(r'[0-9]{1,8}(?:\.[0-9]{1,3})?', text) is None:
        raise ValueError('Enter a fee rate in yugeon/vB with at most three decimals')
    rate = Fraction(text)
    minimum = max(Fraction(1), Fraction(chain.mempool_policy.minimum_rate, 1000))
    if not minimum <= rate <= 100_000:
        raise ValueError('Fee rate is outside the wallet limits')
    return rate


def estimate_fee(chain, size=140, mode='normal'):
    require_int(size, 1, 1_000_000)
    with chain.read_snapshot():
        rate, source, samples = _suggestion(chain, mode, size)
        requested = (rate.numerator * size + rate.denominator - 1) // rate.denominator
        fee = min(MAX_AUTO_FEE_UNITS, requested)
        if fee < chain.mempool_policy.required_fee(size):
            raise ValueError('Relay minimum exceeds the automatic fee limit')
        return {'fee_units': fee, 'amount_unit': 'yugeon', 'vsize': size,
                'rate_yugeon_per_vb': rate_text(Fraction(fee, size)),
                'source': source, 'mode': mode, 'sample_count': samples,
                'capped': requested > fee, 'auto_fee_cap_units': MAX_AUTO_FEE_UNITS,
                'confirmation_time_guaranteed': False,
                'target_blocks': TARGET_BLOCKS[mode], 'congestion': fee_overview(chain)}
