# SUMUWW · Release notes

For a 1 SMW input, the fee depends on whether the transaction needs change. With P2WPKH inputs and outputs at 1 yugeon/vB, sending 0.99999890 SMW costs 110 yugeon and leaves no change. Sending 0.8 SMW from the same input creates a change output and costs 141 yugeon. The wallet creates change only if the amount left after paying the fee meets the minimum for a change output. This minimum accounts for the cost of spending the change later. A smaller remainder goes into the fee shown before you confirm. For a native SegWit wallet input (P2WPKH), the estimate allows up to 71 bytes for the signature, including its hash type.

0.57.61 · Changing the language also updates the Windows taskbar icon while the app is running.

The node normally opens 10 outbound connections, mostly to relay blocks and transactions. It can use a verified backup for blocks and briefly open an 11th connection to discover peers. The overall limit is 125. Up to 117 inbound connections are possible, or 115 with 10 outbound connections. The desktop node now shows the total number of connected peers. Each miner builds its own blocks. The PC node relays completed blocks and rejects mobile mining jobs and solutions.

On restart, the node resumes from its last locally verified block and checks new blocks. If the saved verification record is missing or inconsistent, it checks the stored history again.

SUMUWW PC 0.57.61 · The node validates, stores, relays and exposes chain data.

## Signing format

The optional source SDK assembles transactions and checks supplied signatures without keys or network access. It is not a signer or node command. Its P2WPKH payment restriction applies to the example format, not the node. The existing personal wallet remains available.

## RPC and HTTP API

validateaddress checks the checksum and selected network. decoderawtransaction returns decoded_only, not signature validity or confirmation. Existing OP_RETURN outputs preserve data for external programs. The node adds fee queries, submission checks, RBF replacement status and ordered block data records. Replacements are validated before any pending transaction is removed. Multisig and output locks are implemented for isolated activation tests; they are not yet active on the public network.

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

<!-- /payment-policy-20261116 -->
