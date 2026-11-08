# SUMUWW Android 0.6.98

Fee recommendations appear when the connected node supplies them. The wallet shows a pending balance change when it can verify the full amount.

The phone connects to a SUMUWW full node running version 0.57.49 or later. It checks the reward and calculates the proof of work on the phone. It does not download the chain’s transaction history. Only blocks mined by this phone appear here. Open a record to see its reward and confirmations.

A reachable compatible full node supplies balances and the active chain used to check confirmations. Wallet keys and transaction signing stay on the phone. A previous chain database stays on disk. Older rewards can be identified when the device has a matching local producer job.

Install over the existing org.sumuww.miner app with the same signing certificate. Wallet formats, older local chain files and public-network consensus rules are preserved. The node core supports signed transaction validation/submission, block/transaction/UTXO queries and reorganization state. The Android app has no RPC configuration screen. See [Android node interface](docs/integration/docs/i18n/en/ANDROID.html).

Tests run in the separate .audit package on disposable regtest data. The test fixture is included only in the instrumentation APK. The production APK contains the application modules and offline documents.
