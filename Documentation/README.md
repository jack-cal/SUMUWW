# SUMUWW documentation

[Current node documentation in 34 languages](../PC/Source/docs). The 26 October documentation archive remains available. [English whitepaper 2.4](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-Whitepaper-2.4.zip) and [documentation 20261026-r1](https://github.com/jack-cal/SUMUWW/releases/tag/docs-20261026-r1) are separate downloads.

- [Whitepaper 2.4](Whitepaper/WHITEPAPER.md) · [Changes](Whitepaper/CHANGELOG.md)
- [Connection-proof specification](Whitepaper/CONNECTION_PROOFS_9000.md)
- [Beacon recovery](BEACON_RECOVERY.md) · [HTLC reference](Whitepaper/HTLC_9100.md)
- [Component suite and migration](COMPONENT_SUITE.md)
- [Historical whitepaper 2.1 archive](https://github.com/jack-cal/SUMUWW/releases/tag/whitepaper-v2.1-en)
- [P2P Full/Light comparison](../P2P/Source/EDITIONS.md) · [Bitcoin and block-9100 setup](../P2P/Source/BITCOIN_SETUP.md)

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate.

<!-- /payment-policy-20261116 -->
