# Payment fees, reviewed transactions and compatibility

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.102 and wallet 1.1.13 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->
