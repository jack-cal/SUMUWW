# SUMUWW · Node operation

The node normally opens 10 outbound connections, mostly to relay blocks and transactions. It can use a verified backup for blocks and briefly open an 11th connection to discover peers. The overall limit is 125. Up to 117 inbound connections are possible, or 115 with 10 outbound connections. The desktop node now shows the total number of connected peers. Each miner builds its own blocks. The PC node relays completed blocks and rejects mobile mining jobs and solutions.

On restart, the node resumes from its last locally verified block and checks new blocks. If the saved verification record is missing or inconsistent, it checks the stored history again.

SUMUWW PC 0.57.61 · The node validates, stores, relays and exposes chain data.

## Network and addresses

The public network is `sumuww`; `dora` is its internal alias. Check the genesis hash below. Native addresses use witness v0 P2WPKH and HASH160 of a compressed secp256k1 public key. There is no mandatory memo or tag. Reject wrong-network addresses and invalid checksums. Record each HD receive/change branch and index; do not assume Bitcoin's derivation path.

## Authentication and limits

Enable RPC explicitly at numeric loopback `127.0.0.1:18443` with its private Bearer token. No wallet unlock or remote signing is exposed. Use a local service or authenticated tunnel; browser Origin/Referer requests are rejected. JSON-RPC uses POST `/rpc`, an object/array `params` and an `id`; notifications return HTTP 204. Limits: body 8004096 bytes, headers 8192 bytes, batch 16, concurrent requests 16, deadline 10 seconds; pagination limit 1–1000 and offset 0–1000000. There are 28 methods and 11 REST routes.

## Transaction and block lookup

`getrawtransaction` searches the active chain and mempool, not orphan-only transactions. Inputs identify outpoints, not a unique sender address. `getblock` takes Boolean `verbose`; inactive stored blocks have `active=false` and `confirmations=-1`. Their raw transactions remain available by block hash. `findspendingtransaction` searches confirmed active-chain spends only; null does not prove availability. Check `gettxout` with `include_mempool=true`. All confirmations and active flags can change after a reorganization.

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

<!-- /payment-policy-20261116 -->

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized. 
