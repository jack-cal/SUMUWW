package org.sumuww.wallet

import androidx.test.platform.app.InstrumentationRegistry
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import org.junit.Test

class PaymentAndPeerRegressionTest {
    @Test fun paymentSignaturesAndPeerRecoveryOnAndroid() {
        val app = InstrumentationRegistry.getInstrumentation().targetContext
        if (!Python.isStarted()) Python.start(AndroidPlatform(app))
        val builtins = Python.getInstance().getModule("builtins")
        val scope = builtins.callAttr("dict")
        scope.callAttr("__setitem__", "cache", app.cacheDir.absolutePath)
        builtins.callAttr("exec", """
            import io, sys, tempfile, unittest, pc_tests
            tempfile.tempdir = cache
            sys.modules['tests'] = pc_tests
            cases = ['test_fee_estimation', 'test_signature_size_bound', 'test_handshake_progress_deadline', 'test_phone_alias_handshake_race', 'test_protocol_retry_recovery', 'test_short_synced_reconnect']
            suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromName('pc_tests.' + case) for case in cases)
            stream = io.StringIO()
            result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
            if not result.wasSuccessful() or result.skipped:
                raise AssertionError(stream.getvalue())
        """.trimIndent(), scope)
    }
}
