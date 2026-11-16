"""Copy only active public blocks to a fresh test database and validate them."""
from contextlib import closing
from pathlib import Path
import sqlite3
from sumuww.block import Block
from sumuww.chain import Chain

def public_chain_fixture(source_path, target_path):
    with closing(sqlite3.connect(Path(source_path).as_uri() + '?mode=ro', uri=True)) as source:
        source.execute('PRAGMA query_only=ON')
        source.execute('BEGIN')
        tip = source.execute("SELECT value FROM metadata WHERE name='tip'").fetchone()[0]
        rows = source.execute("""
            WITH RECURSIVE active(hash, parent, height) AS (
                SELECT hash, parent, height FROM blocks WHERE hash=?
                UNION ALL
                SELECT b.hash, b.parent, b.height FROM blocks b
                  JOIN active a ON b.hash=a.parent WHERE a.height>0
            )
            SELECT b.raw FROM active a JOIN blocks b ON b.hash=a.hash
             WHERE a.height>0 ORDER BY a.height
        """, (tip,))
        with Chain(target_path, network='sumuww') as target:
            for (raw,) in rows:
                target.accept_block(Block.deserialize(raw))
            if target.tip_hash != tip:
                raise ValueError('The public block fixture did not reconstruct the source tip')
