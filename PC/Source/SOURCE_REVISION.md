# SUMUWW Windows 0.57.54

On restart, the node resumes from its last locally verified block and checks new blocks. If the saved verification record is missing or inconsistent, it checks the stored history again.

The node normally opens 10 outbound connections, mostly to relay blocks and transactions. It can use a verified backup for blocks and briefly open an 11th connection to discover peers. The overall limit is 125. Up to 117 inbound connections are possible, or 115 with 10 outbound connections. A temporary outbound probe can check another peer when a slot is free. Manually configured direct peers count toward the total. Use --max-peers and --outgoing-target with the node executable. The desktop node now shows the total number of connected peers.

# SUMUWW Windows 0.57.49

Each miner builds its own blocks. The PC node relays completed blocks and rejects mobile mining jobs and solutions. The miner retries temporary SQLite write contention and records an error code and code location locally if a batch stops unexpectedly.

# Release source — Windows 0.57.48

Includes the source-block-9600 upgrade and the PC mining path cleanup. This source archive is distributed with the matching Windows application release. SOURCE_FILES.json records SHA-256 for each included source file; SOURCE_COMMIT.txt identifies the source commit.
