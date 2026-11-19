# Ordinary wallet payment policy

Reviewed on 16 November 2026 for Windows node 0.57.60, Windows wallet 1.0.14, Android node 0.6.102 and Android wallet 1.1.13. These rules describe the ordinary native P2WPKH payment path. They do not redefine HTLC transaction fees or consensus signature validity.

## Amounts, fees and virtual size

One SMW is 100,000,000 yugeon. The transaction fee is the sum of the spent output values minus the sum of the new output values. A fee transfers existing coins and does not create new issuance. The recipient receives the requested amount; the sender also pays the reviewed fee.

A rate is expressed in yugeon per virtual byte, or yugeon/vB. Transaction weight is three times the non-witness serialized size plus the full serialized size. Virtual size is `(weight + 3) // 4`. Fractional-rate calculations round the required fee upward to whole yugeon.

The wallet prices the selected input count and the outputs it will actually create. It does not unconditionally add a change output. With compressed public keys and the wallet's 71-byte signature bound, illustrative size bounds are:

| P2WPKH inputs | P2WPKH outputs | Estimated upper size |
|---:|---:|---:|
| 1 | 1 | 110 vB |
| 1 | 2 | 141 vB |
| 2 | 1 | 177 vB |
| 2 | 2 | 208 vB |
| 3 | 2 | 276 vB |

These are size bounds, not a promise that the final fee always equals the displayed rate times this table. Input selection rounds marginal input costs separately. A remainder intentionally not returned as change is also part of the fee. A shorter valid signature may make the actual virtual size smaller than its bound; the already reviewed fee is not reduced or the transaction rebuilt afterward.

## Change selection

The planner first evaluates a payment without change. It adds a change output only when the remaining value covers that output's creation cost and reaches the wallet's minimum viable change. The input selection and change decision use the same confirmed-UTXO snapshot, excluding immature coinbase outputs and inputs already spent by accepted pending transactions.

The current P2WPKH change template is 31 serialized bytes. With the default discard rate of 10 yugeon/vB, `minimum_viable_change` returns 980 yugeon. The calculation also respects the dust-relay floor and the estimated future spending cost. These values are wallet policy, not consensus restrictions on arbitrary transaction outputs.

If the remainder cannot support viable change, no change output is created and the remainder becomes part of the actual fee. The quote reports that actual fee and the full debit. The wallet's automatic fee cap is 1,000,000 yugeon and its manual cap is 100,000,000 yugeon. If the selected coins cannot satisfy the applicable policy and cap, preparation fails rather than silently sending a different payment.

## One reviewed transaction

`plan_payment` returns one `PaymentPlan`: selected inputs, exact outputs, spent-output values and the quote. Its signing method adds witnesses to that plan without selecting new coins or changing outputs. The service retains the resulting signed transaction under one expiring, single-use quote identifier. Confirming the quote submits those retained signed bytes; it does not call the planner or signer again.

Preparation may produce signatures before the confirmation dialog is accepted. The invariant is that the displayed amounts and fee describe the same signed transaction that confirmation submits. This is not a claim that signing happens only after the user clicks Confirm.

A replaced or expired quote, a locked or changed wallet, a changed node instance, a conflicting pending spend or a reorganization can prevent submission. The user must prepare and review a fresh quote. There is no automatic payment retry. Acceptance into the local mempool is not a block confirmation; confirmations can also change during a reorganization.

## Local signature size policy

For ordinary payment plans, the signer uses libsecp256k1's deterministic low-R retry procedure together with low-S ECDSA. DER encoding is at most 70 bytes before the one-byte `SIGHASH_ALL` suffix, giving a maximum of 71 bytes for the witness signature item. The public key is compressed. The signer rejects a result that exceeds the bound used to price the plan.

This changes local signing and size estimation only. The verifier's rules for other supported, valid external signatures are not tightened to 71 bytes. Existing valid coins, transaction history, issuance, difficulty and connection-proof rules are unchanged.

## Fee-rate suggestions remain SUMUWW-specific

Slow, normal and fast suggestions use this node's accepted pending transactions and ancestor packages. Their capacity budgets are six, three and one blocks respectively, not confirmation deadlines. The estimator does not sample recent confirmed block fees and does not observe every node's mempool. Manual rate entry remains available.
