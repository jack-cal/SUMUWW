"""Mobile PoW client. Keeps local work receipts, never opens the full chain."""
import asyncio
import json
import secrets
import sqlite3
import time
from contextlib import nullcontext
from fractions import Fraction
from pathlib import Path

from sumuww import privacy
from sumuww.address import decode_address
from sumuww.app_service import AppService, AppServiceError, _finish, _safe_error
from sumuww.block import mine_header
from sumuww.chain import Coin
from sumuww.fees import MAX_AUTO_FEE_UNITS, MAX_MANUAL_FEE_UNITS
from sumuww.lan_discovery import LanDiscovery
from sumuww.link_crypto import Identity, PRODUCER_TAG, producer_output
from sumuww.managed_privacy import ManagedRouter
from sumuww.network_settings import _atomic_json, save_settings
from sumuww.peerd import endpoint
from sumuww.primitives import (Header, hash_from_display, hash_to_display, format_amount,
                               parse_amount, sha256d, subsidy, valid_target)
from sumuww.rewards import reward_amounts
from sumuww.transaction import Transaction, TxOutput
from sumuww.wire import decode_version, read_frame, write_frame
from sumuww.__main__ import create_payment
from mobile_mining_metrics import metrics


class ListenOnlyDiscovery(LanDiscovery):
    async def _announce(self):
        # A phone has no full-node listener to advertise.
        return


class SpendableCoins:
    """One wallet's spendable outputs at one upstream tip, for the native signer."""
    def __init__(self, script, rows, height):
        self.script, self.rows, self.height = script, rows, height

    def read_snapshot(self):
        return nullcontext()

    def list_utxos(self, script):
        if script != self.script:
            raise ValueError('Wrong wallet')
        return self.rows

    def info(self):
        return {'height': self.height}

    def mempool_transactions(self):
        return ()


class LightService(AppService):
    def __init__(self, *args, network_provider=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._network_provider = network_provider
        self._network_route = None

    async def _start_components(self):
        self.directory.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.directory / 'mobile-mined.sqlite')
        self.db.execute('CREATE TABLE IF NOT EXISTS mined (hash TEXT PRIMARY KEY, address TEXT NOT NULL, '
                        'height INTEGER NOT NULL, txid TEXT NOT NULL, amount INTEGER NOT NULL, '
                        'stamp INTEGER NOT NULL, active INTEGER, checked TEXT)')
        self.db.execute('CREATE INDEX IF NOT EXISTS mine_address_height ON mined(address,height DESC)')
        identity = Identity(self.database.with_name(self.database.name + '.link-keys.sqlite'))
        try:
            self.producer = identity.node_id
        finally:
            identity.close()
        self.remote = {}
        self.job_parent = self.job_bits = None
        self.peer = self.discovery = self.router = self.transport = None
        self.hints = []
        self._privacy_epoch = 0
        self.last_good = 0
        self._refresh_task = asyncio.create_task(self._poll())
        self._migration = asyncio.create_task(asyncio.to_thread(self._import_previous))
        self._quote = None

    def _import_previous(self):
        from contextlib import closing
        from sumuww.address import encode_address
        from sumuww.block import Block
        from sumuww.link_crypto import producer
        if not self.database.is_file():
            return
        keys_path = self.database.with_name(self.database.name + '.link-keys.sqlite')
        with closing(sqlite3.connect(self.directory/'mobile-mined.sqlite')) as out:
            if out.execute('PRAGMA user_version').fetchone()[0] >= 1:
                return
            # Legacy releases created local signing jobs for this producer. Read only
            # the public block identifiers, never the job contents or wallet secrets.
            with closing(sqlite3.connect(keys_path.as_uri()+'?mode=ro',uri=True)) as keys, closing(
                    sqlite3.connect(self.database.as_uri()+'?mode=ro',uri=True)) as chain, out:
                for (name,) in keys.execute("SELECT name FROM link_private WHERE name GLOB 'job:*'"):
                    raw_hash = bytes.fromhex(name[4:])
                    row = chain.execute('SELECT height,raw FROM blocks WHERE hash=?',(raw_hash,)).fetchone()
                    if not row:
                        continue
                    b = Block.deserialize(row[1])
                    if b.block_hash() != raw_hash or producer(b) != self.producer:
                        continue
                    cb = b.transactions[0]
                    try:
                        address = encode_address(cb.outputs[0].script_pubkey, network=self.network)
                    except ValueError:
                        continue
                    out.execute('INSERT OR IGNORE INTO mined VALUES (?,?,?,?,?,?,NULL,NULL)',
                                (hash_to_display(raw_hash),address,row[0],hash_to_display(cb.txid()),cb.outputs[0].value,b.header.timestamp))
                out.execute('PRAGMA user_version=1')

    async def _run(self):
        try:
            await super()._run()
        finally:
            task = getattr(self, '_refresh_task', None)
            if task:
                task.cancel()
                await asyncio.gather(task, return_exceptions=True)
            await self._close_network()
            migration = getattr(self, '_migration', None)
            if migration:
                await migration
            if hasattr(self, 'db'):
                self.db.close()

    async def _close_network(self):
        for name in ('discovery', 'transport', 'router'):
            obj = getattr(self, name, None)
            if obj is not None:
                await obj.stop()
                setattr(self, name, None)

    def _hint(self, target):
        if target not in self.hints:
            self.hints = ([target] + self.hints)[:32]

    async def _refresh_network(self):
        mode = self._privacy_options['mode']
        if mode != 'direct':
            if self.router is None:
                self.router = ManagedRouter(mode, self.directory)
            port = await self.router.ensure_running()
            if self.transport is None or self.transport.options['port'] != port:
                if self.transport:
                    await self.transport.stop()
                self.transport = privacy.Transport(privacy.settings(mode, port))
            return
        from sumuww.self_address import async_enumerate_ipv4_interfaces
        interfaces = tuple(i.host for i in await async_enumerate_ipv4_interfaces())
        route = self._network_provider() if self._network_provider else None
        if self.discovery and self._interfaces == interfaces and self._network_route == route:
            return
        if self.discovery:
            await self.discovery.stop()
        self._interfaces = interfaces
        self._network_route = route
        self.discovery = ListenOnlyDiscovery(self.network, 18444, secrets.randbits(64), self._hint, interfaces)
        await self.discovery.start()

    def _targets(self):
        targets = []
        for name in self._settings['peers']:
            targets.append(endpoint(name, allow_zero=False, allow_lan=True, allow_internet=True))
        cache = self.database.with_name(self.database.name + '.peers.json')
        if cache.is_file() and cache.stat().st_size <= 131072:
            try:
                saved = json.loads(cache.read_bytes())
                for row in saved.get('peers', [])[:32]:
                    targets.append((row['host'], int(row['port'])))
            except (ValueError, TypeError, OSError, KeyError):
                pass
        if self._privacy_options['mode'] == 'direct':
            targets += self.hints
        candidates = ([self.peer] if self.peer else []) + targets
        return list(dict.fromkeys(candidates))

    async def _request(self, target, op, **fields):
        writer = None
        try:
            mode = self._privacy_options['mode']
            if mode == 'direct':
                reader, writer = await asyncio.open_connection(*target)
            else:
                if not self.transport or self.transport.mode != mode:
                    raise OSError('Private transport unavailable')
                reader, writer = await self.transport.open(target)
            magic = self.network.message_magic
            hello = await read_frame(reader, magic=magic, timeout=20)
            if hello.command != 'version':
                raise ValueError('Expected SUMUWW peer')
            version = decode_version(hello.payload)
            genesis = self.network.genesis.block_hash()
            if version.genesis != genesis or version.profile != self.network.profile_id:
                raise ValueError('Unexpected network')
            msg = json.dumps(dict(fields, op=op, genesis=genesis.hex()), separators=(',', ':')).encode()
            await write_frame(writer, 'smwlight', msg, magic=magic)
            # A syncing full node may need to validate its tip before serving a job.
            frame = await read_frame(reader, magic=magic, timeout=25)
            if frame.command != 'smwreply':
                raise ValueError('Peer does not support mobile work')
            data = json.loads(frame.payload)
            if not isinstance(data, dict) or 'error' in data:
                raise ValueError('Full node rejected the request')
            return data
        finally:
            await privacy.close(writer)

    async def query(self, target, op, **fields):
        if not target:
            raise AppServiceError('Waiting for a compatible full node')
        return await asyncio.wait_for(self._request(target, op, **fields), 30)

    async def _poll(self):
        next_discovery = 0
        cursor = 0
        while True:
            try:
                if time.monotonic() >= next_discovery:
                    next_discovery = time.monotonic() + 20
                    try:
                        await self._refresh_network()
                    except (ValueError, RuntimeError, OSError):
                        pass
                targets = self._targets()
                if targets:
                    target = self.peer or targets[cursor % len(targets)]
                    cursor += 1
                    owner, epoch = self._address, self._privacy_epoch
                    reply = await self.query(target, 'status', address=owner)
                    hash_from_display(reply['tip'])
                    if type(reply.get('height')) is not int or reply['height'] < 0:
                        raise ValueError('Invalid node height')
                    if (owner, epoch) == (self._address, self._privacy_epoch):
                        self.remote, self.peer, self.last_good = reply, target, time.monotonic()
                        if owner and reply.get('balance'):
                            await self._read_pending(target, owner, reply)
                        await self._page(0, 10)
            except (ValueError, TypeError, KeyError, OSError, RuntimeError):
                self.peer = None
            await asyncio.sleep(3)

    async def _read_pending(self, target, address, snapshot):
        """Use one coherent wallet observation. Never display a partial total."""
        if snapshot.get('fees', {}).get('pending_count') == 0:
            snapshot['pending_units'] = 0
            return
        try:
            page = await self.query(target, 'alerts', address=address, offset=0)
            if page['tip'] != snapshot['tip']:
                return
            # The full node sends pending transfers first, followed by confirmed ones.
            rows = page['transactions']
            if len(rows) < page['total'] and all(row['status'] == 'pending' for row in rows):
                return
            delta = sum(row['net_amount'] for row in rows if row['status'] == 'pending')
            if type(delta) is int:
                snapshot['pending_units'] = delta
        except (OSError, ValueError, RuntimeError, KeyError, TypeError):
            return

    def _status(self):
        online = bool(self.peer and time.monotonic() - self.last_good < 20)
        data = self.remote
        ready = online and data.get('mining_ready') is True
        wallet = self._public_wallet() if self._address else None
        balance = data.get('balance')
        if wallet and online and balance and balance.get('address') == self._address:
            for key, field in [('total','confirmed'), ('available','available'), ('spendable','mature'), ('immature','immature')]:
                wallet[key + '_smw'] = balance[field + '_smw']
            delta = data.get('pending_units')
            if delta is not None:
                wallet['pending_smw'] = ('-' if delta < 0 else '') + format_amount(abs(delta))
        return {'node': {'running': True, 'peers': int(online), 'height': data.get('height',-1),
                         'synchronized_peers': int(ready),
                         **({'next_bits': self.job_bits} if online and self.job_parent == data.get('tip') and self.job_bits else {}),
                         'tip': data.get('tip'), 'mining_ready': ready, 'sync_state': 'ready' if ready else 'waiting'},
                'wallet': wallet, 'fees': data.get('fees', {}) if online else {},
                'connection': {'peers': self._settings['peers'], 'privacy': self._privacy_options},
                'mining': {'state': self._mining_state, 'reserved': self._mining_reserved},
                'transactions': self._local_page(0,10)['transactions']}

    def _local_page(self, offset, limit, query=''):
        if offset < 0 or not 1 <= limit <= 200 or len(query) > 64:
            raise ValueError('Invalid history page')
        args = (self._address, query.lower())
        where = ' FROM mined WHERE address=? AND instr(txid,?)>0'
        total = self.db.execute('SELECT COUNT(*)' + where,args).fetchone()[0]
        rows = self.db.execute('SELECT hash,height,txid,amount,stamp,active,checked' + where +
                               ' ORDER BY height DESC, hash LIMIT ? OFFSET ?',args + (limit,offset))
        tip, height = self.remote.get('tip',''), self.remote.get('height',-1)
        items = []
        for digest,n,txid,amount,stamp,active,checked in rows:
            current = bool(tip and checked == tip and self.peer)
            status = ('confirmed' if active else 'orphaned') if current else 'unverified'
            items.append(dict(block_hash=digest, height=n, txid=txid, timestamp=stamp, net_amount=amount,
                              coinbase=True, status=status, confirmations=height-n+1 if status=='confirmed' else 0,
                              mining_reward=reward_amounts(amount,n,max(0,amount-subsidy(n)))))
        return dict(transactions=items, offset=offset, limit=limit, total=total,
                    height=height, tip=tip, address=self._address or '')

    async def _page(self, offset, limit, query=''):
        page = self._local_page(offset,limit,query)
        items = page['transactions']
        if items and self.peer and any(x['status']=='unverified' for x in items):
            r = await self.query(self.peer,'check',points=[x['height'] for x in items])
            if r['tip'] == page['tip'] and len(r['hashes']) == len(items):
                with self.db:
                    self.db.executemany('UPDATE mined SET active=?,checked=? WHERE hash=?',
                                        [(v==x['block_hash'],r['tip'],x['block_hash']) for x,v in zip(items,r['hashes'])])
                page = self._local_page(offset,limit,query)
        return page

    def _select_wallet(self, key, path):
        self._quote = None
        self.remote.pop('balance', None)
        return super()._select_wallet(key, path)

    async def _execute(self, op, args):
        if op == 'transaction_history':
            return await self._page(*args)
        if op == 'transfer_alerts':
            if not self._address:
                raise AppServiceError('Select a wallet')
            return await self.query(self.peer, 'alerts', address=self._address, offset=args[0])
        if op == 'mined_search':
            return await self._page(*args)
        if op == 'peer':
            endpoint(args[0], allow_zero=False, allow_lan=True, allow_internet=True)
            peers = list(dict.fromkeys(self._settings['peers'] + [args[0]]))
            new = dict(self._settings, peers=peers)
            save_settings(self.directory, new)
            self._settings = new
            return {'peer': args[0]}
        if op == 'configure_privacy':
            if self._mining_reserved:
                raise AppServiceError('Stop mining before changing privacy settings')
            opts = privacy.settings(*args)
            self._refresh_task.cancel()
            await asyncio.gather(self._refresh_task, return_exceptions=True)
            await self._close_network()
            _atomic_json(self.directory / privacy.SETTINGS_NAME, opts)
            self._privacy_options = opts
            self.peer, self.remote, self._quote = None, {}, None
            self._privacy_epoch += 1
            self._refresh_task = asyncio.create_task(self._poll())
            return {}
        if op == 'prepare_payment':
            return await self._prepare_light(*args)
        if op == 'submit_payment':
            quote, self._quote = self._quote, None
            if (not quote or quote[0] != args[0] or quote[1] < time.monotonic()
                    or self._key is None or quote[2] is not self._key):
                raise AppServiceError('Payment quote expired')
            tx = quote[3]
            result = await self.query(quote[4], 'send', hex=tx.serialize().hex())
            if result.get('txid') != hash_to_display(tx.txid()):
                raise OSError('Payment submission outcome is unknown')
            return result
        if op == 'lock':
            self._quote = None
        return await super()._execute(op,args)

    async def _prepare_light(self, to, amount_text, fee_option):
        self._quote = None
        if self._key is None:
            raise AppServiceError('Unlock wallet before sending')
        recipient = decode_address(to, network=self.network)
        amount = parse_amount(amount_text)
        mode, rate = 'normal', None
        if fee_option and fee_option.startswith('rate:'):
            rate = fee_option[5:]
            if not 0 < Fraction(rate) <= 100000:
                raise ValueError('Invalid manual fee rate')
        elif fee_option:
            mode = fee_option.removeprefix('auto:')
            if mode not in ('slow','normal','fast'):
                raise ValueError('Invalid fee mode')
        target = self.peer
        result = await self.query(target,'quote',address=self._address,to=to,amount=amount,mode=mode,rate=rate)
        fee = result['fee_units']
        if type(fee) is not int or not 0 < fee <= (MAX_MANUAL_FEE_UNITS if rate else MAX_AUTO_FEE_UNITS):
            raise ValueError('Fee exceeds wallet limits')
        coins, seen, pos, total = [], set(), 0, 0
        while total < amount + fee:
            page = await self.query(target,'coins',address=self._address,offset=pos)
            batch = page['utxos']
            if page['tip'] != result['tip'] or len(batch)>100:
                raise ValueError('Payment quote changed')
            for row in batch:
                if row.get('spendable') is not True:
                    continue
                point = (hash_from_display(row['txid']), row['index'])
                if point in seen or bytes.fromhex(row['script_pubkey']) != self._script:
                    raise ValueError('Invalid wallet output')
                seen.add(point)
                output = TxOutput(row['value_units'], self._script)
                coins.append((point,Coin(output,row['height'],row['coinbase'])))
                total += output.value
                if total >= amount + fee:
                    break
            pos += len(batch)
            if not batch or pos >= page['total']:
                break
        tx = create_payment(SpendableCoins(self._script,coins,page['height']), self._key,recipient,amount,fee)
        token = secrets.token_hex(16)
        self._quote = (token,time.monotonic()+120,self._key,tx,target)
        return dict(quote_id=token,amount_smw=format_amount(amount),fee_smw=format_amount(fee),total_smw=format_amount(amount+fee))

    async def _mine(self, future):
        value = error = None
        try:
            if not self._script:
                raise AppServiceError('Select a wallet before mining')
            while not self._mining_cancel.is_set():
                peer = self.peer
                if not peer:
                    self._mining_state = 'waiting'
                    await asyncio.sleep(.5)
                    continue
                try:
                    job = await self.query(peer,'work',address=self._address,producer=self.producer)
                except (OSError,ValueError):
                    await asyncio.sleep(2)
                    continue
                if job.get('waiting'):
                    await asyncio.sleep(1)
                    continue
                header = Header.deserialize(bytes.fromhex(job['header']))
                height = job['height']
                if type(height) is not int or height < 1 or len(job['branch'])>32:
                    raise ValueError('Invalid mining job')
                valid_target(header.bits,self.network.pow_limit)
                cb = Transaction.deserialize(bytes.fromhex(job['coinbase']))
                if not cb.is_coinbase() or cb.outputs[0].script_pubkey != self._script:
                    raise ValueError('Template pays another wallet')
                if any(o.value for o in cb.outputs[1:]) or cb.outputs[0].value < subsidy(height):
                    raise ValueError('Invalid reward')
                if any(o.script_pubkey.startswith(b'\x6a\x25'+PRODUCER_TAG) for o in cb.outputs) and producer_output(self.producer) not in cb.outputs:
                    raise ValueError('Wrong mining identity')
                root = cb.txid()
                for sibling in job['branch']:
                    digest = bytes.fromhex(sibling)
                    if len(digest)!=32:
                        raise ValueError('Invalid coinbase proof')
                    root = sha256d(root+digest)
                if root != header.merkle_root:
                    raise ValueError('Coinbase proof mismatch')
                self.job_parent = hash_to_display(header.previous_hash)
                self.job_bits = f'{header.bits:08x}'
                self._mining_state = 'running'
                start = time.monotonic()
                def interrupted():
                    return (self._mining_cancel.is_set() or time.monotonic()-start>45 or
                            (self.remote.get('tip') and self.remote['tip']!=hash_to_display(header.previous_hash)))
                try:
                    solved = await asyncio.to_thread(metrics.wrap(mine_header),header,1<<32,
                                                     pow_limit=self.network.pow_limit,cancel_check=interrupted)
                except RuntimeError:
                    if not interrupted():
                        raise
                    continue
                digest = hash_to_display(solved.digest())
                with self.db:
                    self.db.execute('INSERT OR IGNORE INTO mined VALUES (?,?,?,?,?,?,NULL,NULL)',
                                    (digest,self._address,height,hash_to_display(cb.txid()),cb.outputs[0].value,solved.timestamp))
                try:
                    res = await self.query(peer,'solve',job=job['job'],nonce=solved.nonce)
                except (OSError,ValueError):
                    # A dropped reply can follow acceptance; check the same height.
                    check = await self.query(peer,'check',points=[height])
                    res = {'accepted':check['hashes']==[digest],'hash':digest}
                if res.get('accepted') and res.get('hash')==digest:
                    value = {'block_hash':digest,'cancelled':False}
                    break
            if value is None:
                value = {'cancelled':True}
        except Exception as exc:
            error = _safe_error(exc)
        finally:
            with self._control:
                self._mining_reserved = False
                self._mining_state = 'idle'
            _finish(future,value,error)
