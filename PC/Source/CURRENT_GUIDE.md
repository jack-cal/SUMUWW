SUMUWW 0.57.48 — update before block 9,600. See UPGRADE_9600.md and the local 34-language upgrade9600 guide.

# SUMUWW PC 0.57.61

1 yugeon = 0.00000001 SMW. Wallet fees support slow, normal and fast suggestions or a manual yugeon/vB rate, with the exact total shown before confirmation. The node adds signed-transaction preflight, bounded atomic replacement and block data record queries.

For a 1 SMW input, the fee depends on whether the transaction needs change. With P2WPKH inputs and outputs at 1 yugeon/vB, sending 0.99999890 SMW costs 110 yugeon and leaves no change. Sending 0.8 SMW from the same input creates a change output and costs 141 yugeon. The wallet creates change only if the amount left after paying the fee meets the minimum for a change output. This minimum accounts for the cost of spending the change later. A smaller remainder goes into the fee shown before you confirm. For a native SegWit wallet input (P2WPKH), the estimate allows up to 71 bytes for the signature, including its hash type.


Multisig and output-lock validation is implemented for explicitly activated isolated test chains; public activation is not scheduled.

[Node features](NODE_FEATURES.html) · [API](EXCHANGE_INTEGRATION.html) · [34 language editions](docs/index.html).

Automatic fees use current pending volume, block capacity and transaction priority. Past block fees are not used. A quiet queue keeps the minimum rate. The preview refreshes; the final confirmation fixes the fee. Observations cover the connected local node, not every node.

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. Rate suggestions still use the local pending queue; matching Bitcoin's sizing approach does not mean using Bitcoin's fee rates.

## Windows I2P component and security checks

Windows packages include official i2pd 3.0.0 with matching hashes and reseed certificates. Defender still detects the upstream I2P executable and ZIP in the recorded test. A matching upstream hash does not prove safety or establish a false positive. Any local file exception applies only to the computer where it is registered and is not installed by the public package. Other computers may block the same files.

<!-- /payment-policy-20261116 -->

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized. The built-in diagnostic accepts a valid proof-of-work block before a connection proof is available, then checks the proof's three witness signatures, relay and persistence after restart.
