# SUMUWW Android 0.7.8

Update every validating full node and ordinary wallet before **block 9,600**. The connection-proof candidate certificate and renewal rules activate at that height.

The Android app starts its own validating node and CPU miner. After the first local verification it resumes at the last verified block. It rechecks the stored history if the record is missing or inconsistent. The first check can take several minutes.

The node validates and synchronizes the SUMUWW chain, provides a personal wallet and optional CPU mining, and retains peer recovery and asynchronous connection proofs.

Mining history separates block issuance, transaction fees, total rewards and the wallet's own received amount. Automatic fees use the connected node's current pending queue and block capacity; previous block fees are not sampled. Manual rates and a final fee review remain available. One yugeon is 0.00000001 SMW.

The API supports address and transaction inspection, signed-transaction checks and submission, UTXOs, confirmation and replacement state, reorganization information and ordered data outputs. Multisig and output-lock public activation is not scheduled.

All 34 UI languages remain available. Preserve encrypted wallets and valid chain history. The existing height-9000 rules and height-9100 HTLC activation remain unchanged.

The APK uses package `org.sumuww.miner`. Preserve the installed app and its data when changing signing identities. The app has no RPC configuration screen.

[Release and checksums](https://github.com/jack-cal/SUMUWW/releases/tag/updates-20261122) · [Source](Source) · [Node interface](Source/docs/integration/docs/i18n/en/ANDROID.html)

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate.

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.103 and wallet 1.1.14 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->
