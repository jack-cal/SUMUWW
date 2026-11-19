# SUMUWW public transaction vectors

These deterministic regtest vectors describe the optional key-free source reference in `sdk/sumuww_integration`. The node accepts serialized signed transactions, not these packages. Keys used to produce fixtures are public test constants. There is no runtime exchange command or deposit observer.

Run `python examples/node_contract.py` from the PC source root after installing dependencies. See [node integration](../../EXCHANGE_INTEGRATION.html).

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

<!-- /payment-policy-20261116 -->
