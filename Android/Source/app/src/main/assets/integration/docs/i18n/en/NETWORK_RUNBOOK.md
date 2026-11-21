# SUMUWW Android 0.7.8 · Node operation

On restart, the node resumes from its last locally verified block and checks new blocks. If the saved verification record is missing or inconsistent, it checks the stored history again.

SUMUWW Android 0.7.8 · The node validates, stores, relays and exposes chain data.

## Network and addresses

The public network is `sumuww`; `dora` is its internal alias. Check the genesis hash below. Native addresses use witness v0 P2WPKH and HASH160 of a compressed secp256k1 public key. There is no mandatory memo or tag. Reject wrong-network addresses and invalid checksums. Record each HD receive/change branch and index; do not assume Bitcoin's derivation path.

## Transaction and block lookup

`getrawtransaction` searches the active chain and mempool, not orphan-only transactions. Inputs identify outpoints, not a unique sender address. `getblock` takes Boolean `verbose`; inactive stored blocks have `active=false` and `confirmations=-1`. Their raw transactions remain available by block hash. `findspendingtransaction` searches confirmed active-chain spends only; null does not prove availability. Check `gettxout` with `include_mempool=true`. All confirmations and active flags can change after a reorganization.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.103 and wallet 1.1.14 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized.

<!-- poll-recovery-20261119 -->

Synchronization refresh now retries after an internal error. A failed peer no longer stops refreshes for other peers. Mining still requires a recently verified peer; an open connection alone is not enough. Mobile mining now waits for synchronization at startup instead of stopping immediately. Fixed network stalls during connection-proof verification and history queries. Background mining remains active.
