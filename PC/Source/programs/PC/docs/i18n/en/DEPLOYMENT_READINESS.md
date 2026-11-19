# Deployment readiness and failure handling

This is a program operating guide, not a change to SUMUWW consensus or a promise of Internet-scale reliability. The developer need not operate a central control service. Each node independently verifies its ledger and applies local resource limits. Peers must actually exist and be reachable; discovery cannot create connectivity through every firewall or NAT.

## Existing protections checked

- The node normally opens 10 outbound connections, mostly to relay blocks and transactions. It can use a verified backup for blocks and briefly open an 11th connection to discover peers. The overall limit is 125. Up to 117 inbound connections are possible, or 115 with 10 outbound connections.
- Per-peer allowances for request work, transaction hints, validation bytes and outgoing bytes. These are protocol allowances, not a fixed operating-system CPU percentage or a universal memory-use guarantee.
- Frame, handshake, response and write deadlines; incomplete or non-reading peers cannot wait forever. Invalid-data cooldowns use actual remote IPs. Healthy existing sessions sharing an IP are retained; new sessions sharing a blocked NAT IP can still be affected.
- At most 1,000 pending transactions and 4,000,000 serialized bytes. Full-pool rejection does not confirm or debit a rejected transfer. The limit is local node policy, not total network transaction capacity.
- An unverified backup does not suspend mining when a fresh verified anchor remains. Normal live block receipt preserves mining on the last validated tip until the new block is fully checked. No fresh verified anchor means mining waits; a user stop remains terminal.
- Validation is required before ledger activation. PoW, contextual difficulty, reward amounts, maturity, signatures and spending constraints are not bypassed during overload or recovery.
- Block storage, UTXO changes and selected-tip updates commit atomically. Restart verifies stored state. 

## Symptoms and response

| Symptom | Safe response |
|---|---|
| Connected peers are zero | Preserve the wallet/chain. Check Internet permission and automatic discovery, then optionally provide a reachable operating peer. Do not create a new wallet to repair networking. |
| Connections exist but mining is waiting | Check validated synchronization/freshness, not just socket count. A raw TCP connection does not prove a usable chain. |
| Pending pool is full | A refused transfer is not confirmed. Check transaction status before retrying; avoid repeatedly generating payments for the same intended transfer. |
| Connections or responses degrade under load | Inspect the bounded node counters and peer state; keep protocol limits enabled. No extra coin issuance or validation bypass is an acceptable workaround. |
| Application terminated unexpectedly | Restart and allow stored-state validation/synchronization. Do not delete wallet or chain files. If validation fails, retain them for diagnosis and recover from a verified backup rather than overwrite them. |
| A software defect is reproduced | Publish a compatible corrective release with tests and release notes. Each user chooses whether to update; there is no remote administrator key to force an update. Consensus changes require separate compatibility analysis. |

For optional authenticated local RPC, `getnetworkinfo` exposes peer/resource counters, `getblockchaininfo` includes synchronization readiness, and `getmempoolinfo` exposes local pending capacity. Keep RPC tokens private; do not publicly expose the RPC port to diagnose ordinary P2P connectivity. General users can view node and synchronization status in the application.

## Rollout boundary

