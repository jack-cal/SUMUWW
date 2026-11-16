import unittest
from unittest.mock import patch
from sumuww.wallet import RegtestKey, sign_p2wpkh
from sumuww.transaction import Transaction, TxInput, TxOutput
from sumuww.errors import InvalidTransaction

class SignatureSizeBoundTests(unittest.TestCase):
    def test_wallet_rejects_signer_exceeding_quoted_bound(self):
        key = RegtestKey.from_int(1)
        prevout = TxOutput(10000, key.script_pubkey)
        tx = Transaction(2, (TxInput(bytes(32), 0),), (TxOutput(9000, key.script_pubkey),))
        with patch.object(RegtestKey, 'sign_digest', return_value=bytes(71)):
            with self.assertRaisesRegex(InvalidTransaction, '71-byte bound'):
                sign_p2wpkh(tx, 0, prevout, key, low_r=True)
