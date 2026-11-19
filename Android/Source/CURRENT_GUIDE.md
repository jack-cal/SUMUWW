# SUMUWW Android 0.6.96

For a 1 SMW input, the fee depends on whether the transaction needs change. With P2WPKH inputs and outputs at 1 yugeon/vB, sending 0.99999890 SMW costs 110 yugeon and leaves no change. Sending 0.8 SMW from the same input creates a change output and costs 141 yugeon. The wallet creates change only if the amount left after paying the fee meets the minimum for a change output. This minimum accounts for the cost of spending the change later. A smaller remainder goes into the fee shown before you confirm. For a native SegWit wallet input (P2WPKH), the estimate allows up to 71 bytes for the signature, including its hash type.

Install the signed APK over org.sumuww.miner without clearing its data. Existing wallets, valid blocks and earlier proofs are preserved. 

Update before source block 9,600. From that height, connection proofs must verify a certified selection of active witnesses. After activation, an unfinished job may retry with a newly certified round while retaining its original block pair and earlier records. Missing updated participants can still delay completion. Mining does not wait for proof completion.

More > All history shows all validated blocks, stored connection proofs and pending job details. More > Help > Documentation opens the [offline Android guide](docs/integration/docs/i18n/en/ANDROID.html). Read [34-language upgrade notices](docs/integration/docs/upgrade9600/index.html) and [exact upgrade rules](UPGRADE_9600.md). The app has no RPC configuration screen. The API specification describes the embedded node core.

This release is prepared as an installation file. Physical-phone installation and public completion of pending jobs are not claimed.

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.103 and wallet 1.1.14 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized. 
