# SUMUWW (SMW)

Validating full nodes and ordinary wallets enforce the connection-proof candidate certificate and renewal rules from **block 9,600**.

SUMUWW is an independent SHA-256d proof-of-work coin with asynchronous connection proofs. Valid cumulative work remains the primary chain-selection rule. Existing wallets, valid chain history, issuance and halvings are preserved.

## Donations

[Support SUMUWW development](Donations/README.md)

## Current downloads — 16 November 2026

| Component | Version | Download | Source |
|---|---|---|---|
| Windows full node, wallet and miner | 0.57.61 | [Download](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-PC-0.57.61.zip) | [Source](PC/Source) |
| Android full node, wallet and miner — new signing identity | 0.6.103 | [Download](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-Android-0.6.103.apk) | [Source](Android/Source) |
| Windows ordinary wallet | 1.0.15 | [Download](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-Wallet-PC-1.0.15-Windows.zip) | [Source](Wallet/Desktop) |
| Android ordinary wallet — new signing identity | 1.1.14 | [Download](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-Wallet-Android-1.1.14.apk) | [Source](Wallet/Source) |
| Local block explorer | 0.4.11 | [Release](https://github.com/jack-cal/SUMUWW/releases/tag/explorer-v0.4.11) | [Source](Explorer/Source) |
| P2P Full — SMW/BTC trading | 0.3.6 | [Release](https://github.com/jack-cal/SUMUWW/releases/tag/p2p-full-v0.3.6) | [Source](P2P/Source) |
| P2P Light — SMW/BTC trading | 0.3.6 | [Release](https://github.com/jack-cal/SUMUWW/releases/tag/p2p-light-v0.3.6) | [Source](P2P/Source) |

[Release notes](Documentation/RELEASE_NOTES_20261116.md) · [Payment policy](Documentation/PAYMENT_POLICY.md) · [Whitepaper 2.4](Documentation/Whitepaper/WHITEPAPER.md) · [34-language reading editions](Documentation/Whitepaper/i18n/index.html) · [Installation and compatibility](Documentation/COMPONENT_SUITE.md)

## Latest changes

- **Fee quotes:** an extra change output was counted even when no change was created. Quotes now count only the outputs the wallet creates.
- **Payment confirmation:** the reviewed transaction could be rebuilt before submission. Confirmation now submits the same signed inputs, outputs and fee shown for review.
- **P2WPKH signatures:** the size limit is 71 bytes including the hash-type byte, matching the size used for the fee quote.
- **Peer connections:** connections could close before acknowledgment or synchronization finished. The node now waits for acknowledgment and retains a usable route while synchronization completes.

**Android signing compatibility:** the node 0.6.103 and wallet 1.1.14 APKs use a new release key. They cannot update installations signed with a different certificate. Preserve the installed app and its data until an encrypted wallet backup and a working recovery method are secured.

The Windows full node and ordinary wallets retain local full validation, encrypted wallet backup and recovery, saved language preferences and all 34 UI languages.

## SMW/BTC trading starts at SUMUWW block 9100

**Conditional exchange transactions are enabled from SUMUWW block 9100.** Both
P2P editions require a current synchronized local SUMUWW full node. Setup,
wallet creation can happen earlier. In P2P 0.3.6, posting requires confirmed
paying funds and fees on an active paying chain.

**Full requires your own synchronized, unpruned Bitcoin Core with `txindex=1`.**
It downloads and retains Bitcoin history in addition to the trading application.
**Light does not require a local Bitcoin full node**; it verifies headers and
transaction inclusion proofs supplied by TLS servers and has different trust
and availability limits. Full and Light participants can trade with each other.

Read the **[Bitcoin full-node setup, disk requirements, Light setup and block-9100
guide](P2P/Source/BITCOIN_SETUP.md)** before funding. It explains configuration,
authentication, synchronization, operating costs, cancellation and recovery.

## Rules from block 9,000

The upgraded consensus rules apply at height **9,000 inclusive**. Blocks produced by legacy software under the old, pre-upgrade rules at height 9,000 or above are rejected by upgraded nodes and cannot extend the upgraded chain. Continued mining on a legacy branch does not make those blocks acceptable.

Valid historical blocks through **8,999 remain usable**, including the valid prefix of a mixed synchronization batch whose later legacy continuation is invalid. Existing wallets, coins, valid history, issuance and halvings are preserved. Update both miners and validating nodes before activation. This is validation by block rules, not a blanket rejection based only on an advertised software version.

## Protocol and documentation

[Whitepaper](Documentation/Whitepaper/WHITEPAPER.md) · [Connection proofs](Documentation/Whitepaper/CONNECTION_PROOFS_9000.md)

The original issuance and halving schedule is preserved. Valid history through 8999 remains usable. From 9000, every block requires a producer-key commitment; random connection events use a 20% probability, and DGW recalculates every ten blocks with a 24-block observation window. Completed signatures are not a mining or block-acceptance prerequisite. The exact-template HTLC spending rule activates at 9100.

All 34 UI languages remain selectable. Saved language preferences are preserved.

[Ordinary wallets](Wallet/README.md) · [Explorer](Explorer/README.md) · [P2P](P2P/README.md) · [Installation and compatibility](Documentation/COMPONENT_SUITE.md)

[Automatic beacon recovery](Documentation/BEACON_RECOVERY.md) is included in this release.
