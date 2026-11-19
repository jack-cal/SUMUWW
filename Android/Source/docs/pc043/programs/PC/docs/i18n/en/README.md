# SUMUWW · Documentation

SUMUWW PC 0.57.46 · The node validates, stores, relays and exposes chain data.

## Signing format

The optional source SDK assembles transactions and checks supplied signatures without keys or network access. It is not a signer or node command. Its P2WPKH payment restriction applies to the example format, not the node. The existing personal wallet remains available.

## RPC and HTTP API

validateaddress checks the checksum and selected network. decoderawtransaction returns decoded_only, not signature validity or confirmation. Existing OP_RETURN outputs preserve data for external programs. The node adds fee queries, submission checks, RBF replacement status and ordered block data records. Replacements are validated before any pending transaction is removed. Multisig and output locks are implemented for isolated activation tests; they are not yet active on the public network.

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.102 and wallet 1.1.13 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->
