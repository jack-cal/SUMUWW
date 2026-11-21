package org.sumuww.miner

import android.os.Build
import androidx.test.platform.app.InstrumentationRegistry
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import java.io.File
import org.junit.Test

/** Run the polling regression against packaged Python, on a disposable emulator. */
class MiningPollRecoveryTest {
    @Test fun pollingRecoversWithoutBypassingValidation() {
        check(Build.FINGERPRINT.startsWith("generic") || Build.MODEL.contains("Android SDK")) {
            "Disposable emulator required"
        }
        val instrumentation = InstrumentationRegistry.getInstrumentation()
        val context = instrumentation.targetContext
        if (!Python.isStarted()) Python.start(AndroidPlatform(context))
        val builtins = Python.getInstance().getModule("builtins")
        val globals = builtins.callAttr("dict")
        globals.callAttr("__setitem__", "fixture_parent", context.cacheDir.absolutePath)
        globals.callAttr("__setitem__", "fixture_source", instrumentation.context.assets.open(
            "mining_poll_recovery.py").bufferedReader().use { it.readText() })
        builtins.callAttr("exec", """
            import io, sys, tempfile, types, unittest
            tempfile.tempdir = fixture_parent
            module = types.ModuleType('packaged_poll_recovery')
            sys.modules[module.__name__] = module
            exec(fixture_source, module.__dict__)
            output = io.StringIO()
            result = unittest.TextTestRunner(stream=output, verbosity=2).run(
                unittest.defaultTestLoader.loadTestsFromTestCase(module.PollRecoveryTests))
            report = output.getvalue()
            assert result.testsRun == 3 and result.wasSuccessful(), report
        """.trimIndent(), globals)
        File(context.getExternalFilesDir(null), "mining-poll-recovery.txt").writeText(
            globals.callAttr("get", "report").toString())
    }
}
