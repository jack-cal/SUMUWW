# SUMUWW Windows 0.57.54

On restart, the node resumes from its last locally verified block and checks new blocks. If the saved verification record is missing or inconsistent, it checks the stored history again.

The node normally opens 10 outbound connections, mostly to relay blocks and transactions. It can use a verified backup for blocks and briefly open an 11th connection to discover peers. The overall limit is 125. Up to 117 inbound connections are possible, or 115 with 10 outbound connections. A temporary outbound probe can check another peer when a slot is free. Manually configured direct peers count toward the total. Use --max-peers and --outgoing-target with the node executable. The desktop node now shows the total number of connected peers.


Each miner builds its own blocks. The PC node relays completed blocks and rejects mobile mining jobs and solutions. The miner retries temporary SQLite write contention and records an error code and code location locally if a batch stops unexpectedly.

SUMUWW 0.57.48 — update before block 9,600. See UPGRADE_9600.md and the local 34-language upgrade9600 guide.

# SUMUWW PC 0.57.54

This release adds address validation and transaction decoding to the node API. The node provides signed-transaction validation and submission, block/transaction/UTXO queries, synchronization state and reorganization information. Existing wallet, mining and connection-proof features are retained. English is the default, with documentation in all 34 supported languages.

See [node interface](EXCHANGE_INTEGRATION.html) and [language editions](docs/index.html).

# SUMUWW Independent Coin

<!-- current-links-9000 -->
## 2026-10-22 · 9000 · 20% · DGW/10

Valid blocks through 8999 remain usable, including those sent together with an invalid later suffix. From 9000, every block needs a producer commitment. DGW uses 24 preceding blocks and recalculates at 9000, 9010, 9020…; intervening blocks keep the parent difficulty. The target interval remains 600 seconds. Connection events are random with probability 20%. Three discovered identities sign after PoW; mining and block acceptance do not wait for signatures. Cumulative work takes priority; valid, nonconflicting connections break work ties, followed by the smaller tip hash. Late evidence can change a tie. See the exact implementation and limitations below.

[Current protocol / exact format / limitations](CONNECTION_PROOFS_9000.html)
<!-- /current-links-9000 -->


SUMUWW has its own genesis, transaction history and proof-of-work consensus. Nodes independently validate transactions and blocks and select the chain with the greatest valid cumulative work.

## Coin documents

- [Whitepaper](WHITEPAPER.md)
- [Protocol specification](SUMUWW_PROTOCOL_SPEC.md)
- [Consensus comparison](docs/CONSENSUS_BASELINE.md)
- [Mining rewards and confirmations](docs/MINING_AND_CONFIRMATIONS.md)
- [P2P protocol](docs/NETWORK_PROTOCOL.md)
- [Coin promotion and registration](docs/COIN_PROMOTION_AND_REGISTRATION.md)

## Separate documentation

[PC program documentation](programs/PC/README.md)
