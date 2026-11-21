# SUMUWW 0.7.8

- Mining could stop immediately before synchronization completed. It now waits for a verified connection.
- A peer refresh error could stop synchronization updates. Refreshes now retry and continue for other peers.
- Connection-proof verification and history queries could stall network processing and background mining. Verification now runs separately, unchanged history is reused, and mining keeps its wake lock during status queries.
