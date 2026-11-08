"""Exercise the production node with disposable regtest blocks on Android."""
import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

from sumuww.chain import Chain
from sumuww.errors import StorageError
from sumuww.wallet import RegtestKey


def run_checks(mode, root):
    directory = Path(root)
    directory.mkdir(exist_ok=True)
    script = RegtestKey.from_int(1).script_pubkey
    if mode in ('interrupt', 'recover'):
        db = directory / 'interrupted.sqlite'
        if mode == 'interrupt':
            # Use a fresh fixture even if a previous verification was interrupted.
            for suffix in ('', '-wal', '-shm'):
                Path(str(db) + suffix).unlink(missing_ok=True)
            with Chain(db) as chain:
                chain.mine(script, 3)
                (directory / 'committed-state').write_text(str(chain.state_commitment()))
            def terminate(stage):
                if stage == 'after_tip_saved':
                    os._exit(77)
            with Chain(db, fault_hook=terminate) as chain:
                chain.mine(script, 1)
            raise AssertionError('The simulated interruption was not reached')
        with patch.object(Chain, '_replay', side_effect=AssertionError('Unexpected historical replay')):
            with Chain(db) as chain:
                assert chain.resumed_from_checkpoint and chain.summary()['height'] == 3
                assert str(chain.state_commitment()) == (directory / 'committed-state').read_text()
                chain.mine(script, 1)
                return chain.summary()['height']

    assert mode == 'normal'
    with tempfile.TemporaryDirectory(dir=directory) as tmp:
        db = Path(tmp) / 'node.sqlite'
        with Chain(db) as chain:
            chain.mine(script, 3)
            tip = chain.tip_hash
            state = chain.state_commitment()
        # Model the schema of a database created before resume records existed.
        with closing(sqlite3.connect(db)) as conn:
            conn.execute('DROP TABLE validation_checkpoint')
            conn.commit()
        with Chain(db) as chain:
            assert not chain.resumed_from_checkpoint and chain.state_commitment() == state
        with patch.object(Chain, '_replay', side_effect=AssertionError('Unexpected historical replay')):
            with Chain(db) as node, Chain(db) as miner:
                assert node.resumed_from_checkpoint and miner.resumed_from_checkpoint
                assert node.tip_hash == tip
                assert node.state_commitment() == state
                miner.mine(script, 1)
                assert node.tip_hash == miner.tip_hash
        with Chain(db, full_verification=True) as chain:
            assert not chain.resumed_from_checkpoint and chain.summary()['height'] == 4
        with closing(sqlite3.connect(db)) as conn:
            conn.execute('UPDATE utxos SET value=0')
            conn.commit()
        try:
            Chain(db).close()
        except StorageError:
            return 4
        raise AssertionError('The modified balance was accepted')
