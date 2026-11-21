package org.sumuww.miner
import android.os.Build
import androidx.test.platform.app.InstrumentationRegistry
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import java.io.File
import org.junit.Test

class MobileMiningFixTest {
 @Test fun synchronizedStartupAndPollRecovery() {
  check(Build.FINGERPRINT.startsWith("generic") || Build.MODEL.contains("Android SDK")) { "Disposable emulator required" }
  val ins=InstrumentationRegistry.getInstrumentation()
  val context=ins.targetContext
  if(!Python.isStarted()) Python.start(AndroidPlatform(context))
  val builtins=Python.getInstance().getModule("builtins")
  val globals=builtins.callAttr("dict")
  globals.callAttr("__setitem__","fixture_parent",context.cacheDir.absolutePath)
  for(name in listOf("test_app_mining_pause_v30","test_mobile_mining_start_wait","test_peer_poll_recovery","test_mobile_background_activity","test_links9000","test_history_prefix_reuse","test_mining_actor_fairness_v39","test_link_proof_responsiveness","test_links_transport")) {
   globals.callAttr("__setitem__",name,ins.context.assets.open(name+".py").bufferedReader().use{it.readText()})
  }
  builtins.callAttr("exec","""
   import io,json,sys,tempfile,types,unittest
   tempfile.tempdir=fixture_parent
   package=types.ModuleType('pc_tests');package.__path__=[];sys.modules['pc_tests']=package;sys.modules['tests']=package
   for name in ('test_app_mining_pause_v30','test_mobile_mining_start_wait','test_peer_poll_recovery','test_mobile_background_activity','test_links9000','test_history_prefix_reuse','test_mining_actor_fairness_v39','test_link_proof_responsiveness','test_links_transport'):
       module=types.ModuleType('pc_tests.'+name);sys.modules[module.__name__]=module
       setattr(package,name,module);exec(globals()[name],module.__dict__);sys.modules['tests.'+name]=module
   suite=unittest.TestSuite([
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_mobile_mining_start_wait'].MobileMiningStartWaitTests),
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_peer_poll_recovery'].PollRecoveryTests),
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_mobile_background_activity'].BackgroundActivityTests),
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_links9000'].LinkUpgradeTests),
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_history_prefix_reuse'].HistoryPrefixTests),
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_mining_actor_fairness_v39'].MiningActorFairnessTests),
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_link_proof_responsiveness'].ProofResponsivenessTests),
       unittest.defaultTestLoader.loadTestsFromTestCase(sys.modules['pc_tests.test_links_transport'].LinkTransportTests)])
   output=io.StringIO();result=unittest.TextTestRunner(stream=output,verbosity=2).run(suite)
   report=output.getvalue()
   assert result.testsRun==38 and result.wasSuccessful(),report
   import pc_runtime,mobile_controls_selftest
   pc_runtime.keystore._publish_no_replace=pc_runtime._publish_android
   controls=json.loads(mobile_controls_selftest.run())
   report+='\n'+json.dumps(controls)
   assert controls['success'],report
  """.trimIndent(),globals)
  File(context.getExternalFilesDir(null),"mobile-mining-fix.txt").writeText(globals.callAttr("get","report").toString())
 }
}
