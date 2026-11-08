package org.sumuww.miner

import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import java.io.File

@RunWith(AndroidJUnit4::class)
class RestartCheckpointTest {
    @Test fun restartFromLocalState() {
        val instrumentation = InstrumentationRegistry.getInstrumentation()
        val app = instrumentation.targetContext
        assertTrue(app.packageName.endsWith(".audit"))
        if (!Python.isStarted()) Python.start(AndroidPlatform(app))
        val python = Python.getInstance()
        val builtins = python.getModule("builtins")
        val scope = builtins.callAttr("dict")
        val code = instrumentation.context.assets.open("restart_checkpoint.py")
            .bufferedReader().use { it.readText() }
        builtins.callAttr("exec", code, scope)
        val mode = InstrumentationRegistry.getArguments().getString("restartPhase", "normal")
        val directory = File(app.filesDir, "restart-test")
        val height = scope.callAttr("__getitem__", "run_checks").call(mode, directory.absolutePath)
        assertEquals(4, height.toInt())
    }
}
