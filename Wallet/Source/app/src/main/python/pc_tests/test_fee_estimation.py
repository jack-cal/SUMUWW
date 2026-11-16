"""Automatic wallet suggestions, stable snapshots and real payment sizing."""
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
import unittest

from sumuww.__main__ import create_payment
from sumuww.chain import Chain
from sumuww.fees import estimate_payment_fee, virtual_size, MAX_AUTO_FEE_UNITS
from sumuww.primitives import COIN
from sumuww.wallet import RegtestKey


class FeeEstimationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = TemporaryDirectory(prefix='sumuww-fee-base-')
        cls.base = Path(cls.fixtures.name)/'base.sqlite'
        cls.alice, cls.bob = RegtestKey.from_int(1), RegtestKey.from_int(2)
        with Chain(cls.base) as chain:
            chain.mine(cls.alice.script_pubkey, 105)

    @classmethod
    def tearDownClass(cls):cls.fixtures.cleanup()

    def setUp(self):
        self.directory = TemporaryDirectory(prefix='sumuww-fee-estimation-')
        path = Path(self.directory.name)/'chain.sqlite'
        shutil.copy2(self.base,path)
        self.chain = Chain(path)

    def tearDown(self):
        self.chain.close()
        self.directory.cleanup()

    def quote(self,amount=COIN):
        return estimate_payment_fee(self.chain,self.alice.script_pubkey,self.bob.script_pubkey,amount)

    def test_no_samples_uses_initial_rate_and_bounds_actual_signed_size(self):
        quote=self.quote()
        self.assertEqual(quote['estimated_vsize'],quote['fee_units'])
        self.assertEqual('live_mempool',quote['source'])
        self.assertFalse(quote['capped'])
        signed=create_payment(self.chain,self.alice,self.bob.script_pubkey,COIN,quote['fee_units'])
        self.assertLessEqual(virtual_size(signed),quote['estimated_vsize'])
        self.chain.submit_transaction(signed)

    def test_change_boundary_with_a_single_spendable_coin(self):
        from sumuww.mempool_policy import MempoolPolicy
        self.chain.mempool_policy = MempoolPolicy()
        self.chain.submit_transaction(create_payment(
            self.chain, self.alice, self.bob.script_pubkey, COIN, 1000))
        self.chain.mine(self.alice.script_pubkey)
        def quote(remainder, **kwargs):
            return estimate_payment_fee(self.chain, self.bob.script_pubkey,
                                        self.alice.script_pubkey, COIN - remainder, **kwargs)

        for remainder, expected_fee, output_count in ((110, 110, 1), (115, 115, 1),
                                                       (141, 141, 1), (142, 142, 1),
                                                       (1120, 1120, 1), (1121, 141, 2)):
            with self.subTest(remainder=remainder):
                estimate = quote(remainder)
                self.assertEqual(expected_fee, estimate['fee_units'])
                self.assertEqual(110 if output_count == 1 else 141, estimate['estimated_vsize'])
                tx = create_payment(self.chain, self.bob, self.alice.script_pubkey,
                                    COIN - remainder, expected_fee)
                self.assertEqual(output_count, len(tx.outputs))
                self.assertTrue(self.chain.test_mempool_accept(tx)['allowed'])
        with self.assertRaisesRegex(ValueError, 'Insufficient mature'):
            quote(100)
        self.assertEqual(275, quote(275, rate='2.5')['fee_units'])
        tx = create_payment(self.chain, self.bob, self.alice.script_pubkey,
                            COIN - 110, quote(110)['fee_units'])
        self.chain.submit_transaction(tx)
        self.chain.mine(self.alice.script_pubkey)
        self.assertEqual(0, self.chain.balance(self.bob.script_pubkey))

    def test_change_plan_uses_the_same_outputs_for_pricing_and_signing(self):
        from sumuww.fees import plan_payment, minimum_viable_change
        from sumuww.transaction import TxOutput
        from fractions import Fraction

        change = TxOutput(0, self.alice.script_pubkey)
        self.assertEqual(980, minimum_viable_change(change))
        self.assertEqual(294, minimum_viable_change(change, long_term_rate=Fraction(1)))
        self.assertEqual(490, minimum_viable_change(change, long_term_rate=Fraction(5)))
        for rate, remainder, expected_change in (
                ('1', 142, 0), ('1', 1120, 0), ('1', 1121, 980),
                ('2', 1261, 0), ('2', 1262, 980), ('5', 1685, 980)):
            amount = 50 * COIN - remainder
            plan = plan_payment(self.chain, self.alice.script_pubkey, self.bob.script_pubkey,
                                amount, rate=rate)
            tx = plan.sign(self.alice)
            self.assertEqual(plan.transaction.outputs, tx.outputs)
            self.assertEqual(expected_change, tx.outputs[1].value if len(tx.outputs) == 2 else 0)
            self.assertEqual(50 * COIN - sum(o.value for o in tx.outputs), plan.quote['fee_units'])
        # A user-specified fee is also reviewed with the signed set of outputs.
        plan = plan_payment(self.chain, self.alice.script_pubkey, self.bob.script_pubkey,
                            50 * COIN - 142, fixed_fee=141)
        self.assertEqual((1, 142), (len(plan.sign(self.alice).outputs), plan.quote['fee_units']))

    def test_multi_input_wallet_size_matches_low_r_witness_bound(self):
        from sumuww.fees import plan_payment
        from sumuww.wallet import verify_p2wpkh
        from hashlib import sha256

        # This fixture must exercise a retry as well as the first-signature path.
        digests = [sha256(bytes([i])).digest() for i in range(32)]
        self.assertTrue(any(self.alice.sign_digest(h)[3] == 33 for h in digests))
        for h in digests:
            sig = self.alice.sign_digest(h, low_r=True)
            self.assertLessEqual(sig[3], 32)
            self.assertLessEqual(len(sig), 70)
        for amount, count, outputs, size, fee in (
                (50 * COIN - 110, 1, 1, 110, 110),
                (60 * COIN, 2, 2, 208, 208),
                (100 * COIN - 178, 2, 1, 177, 178),
                (120 * COIN, 3, 2, 276, 276)):
            plan = plan_payment(self.chain, self.alice.script_pubkey, self.bob.script_pubkey,
                                amount, rate='1')
            tx = plan.sign(self.alice)
            self.assertEqual((count, outputs, size, fee),
                             (len(tx.inputs), len(tx.outputs), plan.quote['estimated_vsize'],
                              plan.quote['fee_units']))
            self.assertLessEqual(virtual_size(tx), size)
            self.assertTrue(all(verify_p2wpkh(tx, i, prev) for i, prev in enumerate(plan.prevouts)))
            self.assertTrue(self.chain.test_mempool_accept(tx)['allowed'])

    def test_exact_payment_does_not_pull_another_available_input(self):
        quote = self.quote(50 * COIN - 110)
        tx = create_payment(self.chain, self.alice, self.bob.script_pubkey,
                            50 * COIN - 110, quote['fee_units'])
        self.assertEqual((1, 1, 110), (len(tx.inputs), len(tx.outputs), quote['fee_units']))

    def test_small_backlog_and_confirmed_high_fee_do_not_raise_quote(self):
        tx=create_payment(self.chain,self.alice,self.bob.script_pubkey,COIN,10_000)
        self.chain.submit_transaction(tx)
        pending=self.quote()
        self.assertEqual('live_mempool',pending['source'])
        self.assertEqual(1,pending['sample_count'])
        self.assertEqual(pending['fee_units'],pending['estimated_vsize'])
        self.chain.mine(self.alice.script_pubkey,1)
        confirmed=self.quote()
        self.assertEqual('live_mempool',confirmed['source'])
        self.assertEqual(pending['fee_units'],confirmed['fee_units'])
        self.assertEqual(0,confirmed['sample_count'])

    def test_zero_fee_samples_do_not_create_a_positive_fee_prediction(self):
        self.chain.submit_transaction(create_payment(self.chain,self.alice,self.bob.script_pubkey,COIN,0))
        self.assertEqual('live_mempool',self.quote()['source'])
        self.chain.mine(self.alice.script_pubkey,1)
        self.assertEqual(self.quote()['estimated_vsize'],self.quote()['fee_units'])

    def test_large_fee_in_quiet_pool_does_not_trigger_auto_cap(self):
        self.chain.submit_transaction(create_payment(self.chain,self.alice,self.bob.script_pubkey,COIN,COIN))
        automatic=self.quote()
        self.assertFalse(automatic['capped'])
        self.assertEqual(automatic['estimated_vsize'],automatic['fee_units'])
        manual=create_payment(self.chain,self.alice,self.bob.script_pubkey,COIN,2*COIN)
        self.chain.submit_transaction(manual)

    def test_fee_percentiles_do_not_raise_price_without_capacity_pressure(self):
        for fee in (1000,2000,3000,4000):
            self.chain.submit_transaction(create_payment(self.chain,self.alice,self.bob.script_pubkey,COIN,fee))
        quote=self.quote()
        self.assertEqual(quote['estimated_vsize'],quote['fee_units'])

    def test_quote_excludes_pending_spends_and_immature_rewards(self):
        self.chain.submit_transaction(create_payment(self.chain,self.alice,self.bob.script_pubkey,49*COIN,1000))
        with self.assertRaisesRegex(ValueError,'Insufficient mature'):
            self.quote(251*COIN)

    def test_amount_can_change_without_fee_being_a_percentage(self):
        self.assertEqual(self.quote(COIN)['fee_units'],self.quote(2*COIN)['fee_units'])

    def test_live_queue_follows_reorganization(self):
        original=self.chain.tip_hash
        tx=create_payment(self.chain,self.alice,self.bob.script_pubkey,COIN,10_000)
        self.chain.submit_transaction(tx)
        self.chain.mine(self.alice.script_pubkey,1)
        self.assertEqual('live_mempool',self.quote()['source'])
        side=self.chain.make_block(self.bob.script_pubkey,transactions=(),parent_hash=original)
        self.chain.accept_block(side)
        extension=self.chain.make_block(self.bob.script_pubkey,transactions=(),parent_hash=side.block_hash())
        self.chain.accept_block(extension)
        # The disconnected signed transaction returns to the pool; it is now
        # pending and must not remain cached as active confirmed history.
        quote=self.quote()
        self.assertEqual('live_mempool',quote['source'])
        self.assertEqual(1,quote['sample_count'])

    def cli_payment(self,*options):
        import contextlib
        import io
        import json
        from unittest.mock import patch
        from coincurve import PrivateKey
        from sumuww.__main__ import main
        from sumuww.address import encode_address
        from sumuww.keystore import WalletKey
        from sumuww.profiles import REGTEST
        key=WalletKey(PrivateKey((1).to_bytes(32,'big')),REGTEST)
        output=io.StringIO()
        arguments=['--database',str(self.chain.database),'wallet-send',
                   '--wallet',str(Path(self.directory.name)/'test-key-only.json'),
                   '--to-address',encode_address(self.bob.script_pubkey,network=REGTEST),
                   '--amount','1',*options]
        with patch('sumuww.__main__._password',return_value='fixture-only'),patch('sumuww.__main__.load_wallet',return_value=key),contextlib.redirect_stdout(output):
            self.assertEqual(0,main(arguments))
        return json.loads(output.getvalue())

    def test_cli_defaults_to_auto_and_reports_actual_fee_and_total(self):
        result=self.cli_payment()
        self.assertEqual('automatic',result['fee_mode'])
        self.assertEqual('live_mempool',result['fee_source'])
        self.assertEqual('0.00000141',result['fee_smw'])
        self.assertEqual('1.00000141',result['total_smw'])

    def test_cli_manual_zero_remains_supported(self):
        result=self.cli_payment('--fee','0')
        self.assertEqual('manual',result['fee_mode'])
        self.assertEqual('0.00000000',result['fee_smw'])
        self.assertEqual('1.00000000',result['total_smw'])


if __name__=='__main__':unittest.main()
