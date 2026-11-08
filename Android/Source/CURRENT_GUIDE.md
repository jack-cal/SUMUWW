# SUMUWW Android 0.6.98

Fee recommendations appear when the connected node supplies them. The wallet shows a pending balance change when it can verify the full amount.

The phone connects to a SUMUWW full node running version 0.57.49 or later. It checks the reward and calculates the proof of work on the phone. It does not download the chain’s transaction history. Only blocks mined by this phone appear here. Open a record to see its reward and confirmations.

A reachable compatible full node supplies balances and the active chain used to check confirmations. Wallet keys and transaction signing stay on the phone. A previous chain database stays on disk. Older rewards can be identified when the device has a matching local producer job.

## Earlier versions

# SUMUWW Android 0.6.96

Install the signed APK over org.sumuww.miner without clearing its data. Existing wallets, valid blocks and earlier proofs are preserved. English remains the default and saved language preferences remain available.

Update before source block 9,600. From that height, connection proofs must verify a certified selection of active witnesses. After activation, an unfinished job may retry with a newly certified round while retaining its original block pair and earlier records. Missing updated participants can still delay completion. Mining does not wait for proof completion.

More > All history shows all validated blocks, stored connection proofs and pending job details. More > Help > Documentation opens the [offline Android guide](docs/integration/docs/i18n/en/ANDROID.html). Read [34-language upgrade notices](docs/integration/docs/upgrade9600/index.html) and [exact upgrade rules](UPGRADE_9600.md). The app has no RPC configuration screen. The API specification describes the embedded node core.

This release is prepared as an installation file. Physical-phone installation and public completion of pending jobs are not claimed.
