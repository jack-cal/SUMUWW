"""Mobile mining waits for verified synchronization without dispatching hashes."""
import time
import importlib.util
import threading
import types
from unittest.mock import patch

from pc_tests.test_app_mining_pause_v30 import MiningPauseLifecycleTests, eventually


class MobileMiningStartWaitTests(MiningPauseLifecycleTests):
    def test_android_batch_survives_initial_sync_wait(self):
        spec = importlib.util.find_spec('pc_runtime')
        host = types.ModuleType('isolated_mobile_start_wait')
        exec(spec.loader.get_code('pc_runtime'), host.__dict__)
        host._batch.update(running=True, completed=0)
        self.ready.clear()
        with patch('sumuww.app_service._mine_block', self.worker):
            thread = threading.Thread(target=host._run_batch, args=(self.service, 1))
            thread.start()
            try:
                eventually(lambda: self.service.status().result(timeout=5)['mining']['state'] == 'waiting')
                self.assertTrue(host._batch['running'])
                self.assertEqual(0, self.calls)
                self.ready.set()
                eventually(lambda: self.calls == 1)
                self.accept.set()
                thread.join(5)
                self.assertFalse(thread.is_alive())
                self.assertIsNone(host._batch['last_error'])
                self.assertEqual(1, host._batch['completed'])
            finally:
                self.service.cancel_mining()
                thread.join(5)

    def test_mobile_start_waits_then_hashes_once_synchronized(self):
        self.ready.clear()
        with patch('sumuww.app_service._mine_block', self.worker):
            future = self.service.mine_one(wait_for_sync=True)
            eventually(lambda: self.service.status().result(timeout=5)['mining']['state'] == 'waiting')
            time.sleep(.2)
            self.assertFalse(future.done())
            self.assertEqual(0, self.calls)
            self.assertTrue(self.service.status().result(timeout=5)['mining']['reserved'])
            self.ready.set()
            eventually(lambda: self.calls == 1)
            self.accept.set()
            result = future.result(timeout=5)
        self.assertFalse(result['cancelled'])
        self.assertGreater(result['network_wait_seconds'], .15)
        self.assertEqual(1, self.maximum)

    def test_stop_before_initial_sync_cannot_restart_mining(self):
        self.ready.clear()
        with patch('sumuww.app_service._mine_block', self.worker):
            future = self.service.mine_one(wait_for_sync=True)
            eventually(lambda: self.service.status().result(timeout=5)['mining']['state'] == 'waiting')
            self.service.cancel_mining().result(timeout=5)
            result = future.result(timeout=5)
            self.ready.set()
            time.sleep(.15)
        self.assertTrue(result['cancelled'])
        self.assertEqual('user_stop', result['cancel_reason'])
        self.assertEqual(0, self.calls)

    def test_wallet_lock_during_initial_sync_preserves_wallet_and_stops(self):
        self.ready.clear()
        with patch('sumuww.app_service._mine_block', self.worker):
            future = self.service.mine_one(wait_for_sync=True)
            eventually(lambda: self.service.status().result(timeout=5)['mining']['state'] == 'waiting')
            wallet = self.service.lock_wallet().result(timeout=5)
            result = future.result(timeout=5)
        self.assertEqual(self.fixture_key.address, wallet['address'])
        self.assertFalse(wallet['unlocked'])
        self.assertTrue(result['cancelled'])
        self.assertEqual('wallet_change', result['cancel_reason'])
        self.assertEqual(0, self.calls)

    def test_shutdown_during_initial_sync_releases_reservation(self):
        self.ready.clear()
        with patch('sumuww.app_service._mine_block', self.worker):
            future = self.service.mine_one(wait_for_sync=True)
            eventually(lambda: self.service.status().result(timeout=5)['mining']['state'] == 'waiting')
            self.service.stop().result(timeout=5)
            result = future.result(timeout=5)
        self.assertTrue(result['cancelled'])
        self.assertEqual('shutdown', result['cancel_reason'])
        self.assertEqual(0, self.calls)
