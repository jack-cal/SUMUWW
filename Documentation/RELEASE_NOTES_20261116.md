# SUMUWW update — 16 November 2026

| Component | Version |
|---|---|
| Windows validating node and miner | 0.57.61 |
| Windows ordinary wallet | 1.0.15 |
| Android validating node and miner | 0.6.103 |
| Android ordinary wallet | 1.1.14 |
| Whitepaper | 2.4 |

- **Fee quotes:** an extra change output was counted when no change was created. Quotes now count only the actual outputs.
- **Payment confirmation:** rebuilding a payment could change the transaction after review. Confirmation now submits the exact signed transaction shown for review.
- **P2WPKH signatures:** signatures are limited to 71 bytes including the hash-type byte, matching the fee-quote size limit.
- **Peer connections:** a connection could close before acknowledgment or synchronization completed. The node now waits for acknowledgment and retains a usable route during synchronization.

## Android: changed signing identity

The Android node and wallet packages in this update are signed with a newly generated release key. They cannot update an older installation signed with a different certificate. The node package is `org.sumuww.miner`; the ordinary wallet is `org.sumuww.wallet.current`. The new certificate SHA-256 is:

`e609c42039cd7b9aa47d921d016ed305b6091dd0b7bb5a820f7b373c3ad66f38`

Keep the installed app and its data until an encrypted wallet backup and a working recovery method are secured. Do not uninstall an old application merely to force installation.

## Documentation

Whitepaper 2.4 and the affected protocol, wallet and operating explanations distinguish actual transaction fees, fee-rate suggestions, change policy, quote reuse and local signature limits.

Existing issuance, valid chain history, block acceptance, difficulty and connection-proof activation rules are preserved. P2P Full/Light trading and Explorer retain their separate documented scope.
