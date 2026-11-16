"""Exercise delay, lost connections and recovery on test-owned TCP sockets."""
import io
import json
import unittest

cases = [
    'test_handshake_progress_deadline.HandshakeProgressTests.test_silent_peer_keeps_original_first_reply_deadline',
    'test_handshake_progress_deadline.HandshakeProgressTests.test_valid_progress_gets_next_reply_budget',
    'test_protocol_retry_recovery.ProtocolRetryRecoveryTests.test_transient_pre_version_closes_do_not_pin_modern_peer_to_v1',
    'test_peer_shutdown_v32.PeerShutdownTests.test_nonreading_outbound_peer_buffer_is_aborted',
    'test_peer_shutdown_v32.PeerShutdownTests.test_pre_handshake_connection_is_cancelled_before_server_wait',
    'test_short_synced_reconnect.ShortSyncedReconnectTests.test_address_handoff_retry_keeps_data_sync_until_rotation_opens',
    'test_short_synced_reconnect.ShortSyncedReconnectTests.test_reset_handoff_retry_keeps_data_sync_until_rotation_opens',
    'test_short_synced_reconnect.ShortSyncedReconnectTests.test_admission_wait_does_not_expire_pending_recovery',
    'test_peer_retry_recovery.RetrySocketTests.test_three_nodes_reconnect_after_failed_dial_without_new_hint',
]
stream = io.StringIO()
suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromName('pc_tests.' + name) for name in cases)
result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
if not result.wasSuccessful() or result.skipped or result.testsRun != len(cases):
    raise AssertionError(stream.getvalue())
report = json.dumps({'passed': True, 'scope': 'faults on isolated emulator TCP connections', 'cases': cases})
