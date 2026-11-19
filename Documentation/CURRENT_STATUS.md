# SUMUWW current program versions — 16 November 2026

| Program | Version |
|---|---|
| Windows full node | 0.57.61 |
| Android full node | 0.6.103 |
| Windows ordinary wallet | 1.0.15 |
| Android ordinary wallet | 1.1.14 |
| Explorer | 0.4.11 |
| P2P Full / Light | 0.3.6 |

Android 0.6.103 starts its own validating node and CPU miner. After the first local verification it resumes at the last verified block. It rechecks the stored history if the record is missing or inconsistent. The first check can take several minutes.

The Windows full node and both ordinary wallets aim for 10 outbound peers. Most connections relay blocks and transactions. A verified backup can relay blocks, and a spare slot can briefly check an 11th peer. Up to 117 inbound connections are possible, or 115 with 10 outbound. The default limit is 125 in total.

P2P 0.3.6 adds funded order checks, per-order Trade buttons and automatic encrypted trading connections. 

[Downloads and matching sources](../README.md) · [Installation](COMPONENT_SUITE.md)

Update validating full nodes and ordinary wallets before block **9,600**. The source-block 9,600 rule certifies the active candidate set used to select three connection-proof witnesses. After activation, pending jobs can renew their activity round while retaining their original block pair and event beacon. Earlier valid history and proofs remain valid. Missing proofs do not prevent ordinary proof-of-work block acceptance. Old and upgraded software can select different equal-work branches.

 Saved language preferences and all 34 selectable languages are preserved. 

Mining history distinguishes new issuance, transaction fees, total rewards and the amount received by the wallet. Automatic fee suggestions use the connected node's current pending queue, not past-block fee samples. One yugeon is 0.00000001 SMW; vB is a data-size unit.

[Current payment policy](PAYMENT_POLICY.md) · [16 November release notes](RELEASE_NOTES_20261116.md)

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized. 
