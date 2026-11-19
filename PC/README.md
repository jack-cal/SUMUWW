# SUMUWW Windows 0.57.61

Update every validating full node and ordinary wallet before **block 9,600**. The connection-proof candidate certificate and renewal rules activate at that height.

The Windows full node and both ordinary wallets aim for 10 outbound peers. Most connections relay blocks and transactions. A verified backup can relay blocks, and a spare slot can briefly check an 11th peer. Up to 117 inbound connections are possible, or 115 with 10 outbound. The default limit is 125 in total.

On restart, the Windows node resumes from the last locally verified block and validates new blocks. The first upgrade from an older database performs a full local check. The node also checks the stored history if its verification record is missing or inconsistent.

The Windows node mines locally, validates completed blocks received from peers and relays them. It rejects mobile mining work requests and solution submissions.

The node validates and synchronizes the SUMUWW chain, provides a personal wallet and optional CPU mining, and retains peer recovery and asynchronous connection proofs.

Mining history separates block issuance, transaction fees, total rewards and the wallet's own received amount. Automatic fees use the connected node's current pending queue and block capacity; previous block fees are not sampled. Manual rates and a final fee review remain available. One yugeon is 0.00000001 SMW.

The API supports address and transaction inspection, signed-transaction checks and submission, UTXOs, confirmation and replacement state, reorganization information and ordered data outputs. Multisig and output-lock public activation is not scheduled.

All 34 UI languages remain available. Preserve encrypted wallets and valid chain history. The existing height-9000 rules and height-9100 HTLC activation remain unchanged.

Extract the complete Windows ZIP and run SUMUWW.exe.

[Release and checksums](https://github.com/jack-cal/SUMUWW/releases/tag/updates-20261116) · [Source](Source) · [Current specification](Source/NODE_FEATURES.md)

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate.

<!-- /payment-policy-20261116 -->
