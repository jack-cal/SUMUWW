"""Power monitoring stays independent of pending chain queries."""
import importlib.util
import json
import threading
import types
import unittest


class BackgroundActivityTests(unittest.TestCase):
    def test_activity_remains_readable_while_node_query_is_blocked(self):
        host = types.ModuleType('isolated_background_activity')
        exec(importlib.util.find_spec('pc_runtime').loader.get_code('pc_runtime'), host.__dict__)
        blocked = threading.Event()
        entered = threading.Event()

        class BusyNode:
            def status(self):
                entered.set()
                blocked.wait(5)

        host._service = BusyNode()
        query = threading.Thread(target=host._service.status)
        mining = threading.Thread(target=blocked.wait)
        host._worker = mining
        host._batch['running'] = True
        query.start()
        mining.start()
        try:
            self.assertTrue(entered.wait(2))
            self.assertTrue(json.loads(host.mining_activity())['running'])
            self.assertTrue(query.is_alive())
            host._batch['running'] = False
            self.assertFalse(json.loads(host.mining_activity())['running'])
        finally:
            blocked.set()
            query.join(2)
            mining.join(2)
        host._batch['running'] = True
        self.assertFalse(json.loads(host.mining_activity())['running'])


if __name__ == '__main__':
    unittest.main()
