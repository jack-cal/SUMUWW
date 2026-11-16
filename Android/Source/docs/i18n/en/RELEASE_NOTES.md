# SUMUWW Android 0.6.103 · Release notes

For a 1 SMW input, the fee depends on whether the transaction needs change. With P2WPKH inputs and outputs at 1 yugeon/vB, sending 0.99999890 SMW costs 110 yugeon and leaves no change. Sending 0.8 SMW from the same input creates a change output and costs 141 yugeon. The wallet creates change only if the amount left after paying the fee meets the minimum for a change output. This minimum accounts for the cost of spending the change later. A smaller remainder goes into the fee shown before you confirm. For a native SegWit wallet input (P2WPKH), the estimate allows up to 71 bytes for the signature, including its hash type.


On restart, the node resumes from its last locally verified block and checks new blocks. If the saved verification record is missing or inconsistent, it checks the stored history again.

SUMUWW Android 0.6.103 · The node validates, stores, relays and exposes chain data.

[Documentation](../../integration/docs/i18n/en/RELEASE_NOTES.html)

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. Rate suggestions still use the local pending queue; matching Bitcoin's sizing approach does not mean using Bitcoin's fee rates.

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.103 and wallet 1.1.14 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->
