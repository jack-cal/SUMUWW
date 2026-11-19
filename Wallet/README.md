# SUMUWW ordinary wallets

Update every validating full node and ordinary wallet before **block 9,600**. The connection-proof candidate certificate and renewal rules activate at that height.

[All components](../README.md) · [Installation and compatibility](../Documentation/COMPONENT_SUITE.md)

| Platform | Version | Download | Source |
|---|---|---|---|
| Windows | 1.0.15 | [Windows ZIP](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-Wallet-PC-1.0.15-Windows.zip) | [Desktop source](Desktop) |
| Android | 1.1.14 | [Signed APK](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-Wallet-Android-1.1.14.apk) | [Android source](Source) |

Receive, send, review transactions, back up and restore existing encrypted wallets.
34 offline UI languages remain available.
These wallets validate and synchronize the blockchain locally and have no mining
controls. They are separate from the full-node/miner interface, not SPV clients.

Android wallet 1.1.14 uses `org.sumuww.wallet.current` and a new release signing key. It cannot update an installation signed with a different key. Keep the installed app and its data until an encrypted wallet backup and a working recovery method are secured.

## Rules from block 9,000

The current rules apply at height **9,000 inclusive**. Blocks produced by legacy
software under the old rules at height 9,000 or above are rejected by upgraded
nodes and cannot extend the upgraded chain. Update miners and validating nodes.
Valid legacy blocks through **8,999 remain usable**, including the valid prefix
of a mixed synchronization batch. Wallet keys, valid coins, issuance and halvings
are preserved. Validation follows block rules, not an advertised version string.

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate.

<!-- /payment-policy-20261116 -->
