"""Startup uses a locally validated tip; stored history can still be audited explicitly."""
from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from sumuww.chain import Chain
from sumuww.errors import StorageError
from sumuww.wallet import RegtestKey


class StartupCheckpointTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.db = Path(tmp.name) / 'node.sqlite'
        self.script = RegtestKey.from_int(1).script_pubkey
        with Chain(self.db) as chain:
            self.assertFalse(chain.resumed_from_checkpoint)
            chain.mine(self.script, 3)
            self.tip = chain.tip_hash
            self.utxos = chain.state_commitment()

    def test_restart_and_verified_extension_never_replay_the_prefix(self):
        with patch.object(Chain, '_replay', side_effect=AssertionError('historical replay')):
            with Chain(self.db) as first, Chain(self.db) as second:
                self.assertTrue(first.resumed_from_checkpoint and second.resumed_from_checkpoint)
                self.assertEqual(first.tip_hash, self.tip)
                self.assertEqual(first.state_commitment(), self.utxos)
                second.mine(self.script, 1)
                self.assertEqual(first.tip_hash, second.tip_hash)
            with Chain(self.db) as after:
                self.assertTrue(after.resumed_from_checkpoint)
                self.assertEqual(after.summary()['height'], 4)

    def test_migration_then_manual_full_verification(self):
        with closing(sqlite3.connect(self.db)) as db:
            db.execute('DROP TABLE validation_checkpoint')
            db.commit()
        with Chain(self.db) as migrated:
            self.assertFalse(migrated.resumed_from_checkpoint)
            self.assertEqual(migrated.state_commitment(), self.utxos)
        with Chain(self.db, full_verification=True) as checked:
            self.assertFalse(checked.resumed_from_checkpoint)
        with Chain(self.db) as restarted:
            self.assertTrue(restarted.resumed_from_checkpoint)

    def test_rolled_back_write_preserves_checkpoint(self):
        with closing(sqlite3.connect(self.db)) as db:
            db.execute('UPDATE utxos SET value=0')
            db.rollback()
        with Chain(self.db) as chain:
            self.assertTrue(chain.resumed_from_checkpoint)
            self.assertEqual(chain.state_commitment(), self.utxos)

    def test_schema_replacement_cannot_hide_unvalidated_edits(self):
        with closing(sqlite3.connect(self.db)) as db:
            name = 'resume_guard_utxos_update'
            sql = db.execute('SELECT sql FROM sqlite_master WHERE name=?', (name,)).fetchone()[0]
            db.execute(f'DROP TRIGGER {name}')
            db.execute('UPDATE utxos SET value=0')
            db.execute(sql)
            db.commit()
        with self.assertRaises(StorageError):
            Chain(self.db)

