# SUMUWW (SMW)

Validating full nodes and ordinary wallets enforce the connection-proof candidate certificate and renewal rules from **block 9,600**. English is the first-launch language on every operating-system language; a saved language choice remains in effect.

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

Ordinary wallet quotes include a change output only when viable change is created. The same selected inputs, outputs and fee are signed and retained for confirmation. Ordinary P2WPKH signatures have a maximum of 71 bytes including the hash-type byte. These are wallet policies; existing consensus signature validity, issuance and valid chain history are preserved. Fee-rate suggestions still use the local queue rather than Bitcoin's fee market or past-block fee samples.

**Android signing compatibility:** the node 0.6.103 and wallet 1.1.14 APKs use a new release key. They cannot update installations signed with a different certificate. Preserve the installed app and its data until an encrypted wallet backup and a working recovery method are secured. The previous Android signing lineage is not offered this package as an automatic in-place update. Both release APKs were installed over the previous same-certificate builds and launched on an Android 11 x86-64 emulator. Their packaged Python payment, signing and peer-recovery tests ran on that emulator. Physical phones and cellular carriers were outside this run.

Windows includes official i2pd 3.0.0. The recorded Defender diagnostic scan still detects the upstream I2P executable and ZIP; the three SUMUWW application executables were not detected in that scan. Local exceptions are not part of the public package and do not apply to another computer. Artifact provenance is not an independent security verdict.

The Windows full node and ordinary wallets retain local full validation, encrypted wallet backup and recovery, saved language preferences and all 34 UI languages. The desktop test record covers synchronization, transactions, reorganizations, mining controls and wallet behavior within its documented scope. P2P and Explorer retain their separate prerequisites and verification limits. An accepted pending transaction is not a block confirmation, and a short test does not establish uninterrupted public connectivity.

## Earlier node update: Windows 0.57.40 / Android 0.6.89

New proof jobs check responsiveness across the discovered identity inventory before selecting three witnesses. Valid replies survive retries and restarts; already selected jobs retain their original witnesses. PC public history shows all active-chain transactions and distinguishes nonselected lotteries, selected pending jobs, selected completed jobs and stored complete proofs. See the [repair verification and limits](Documentation/CONNECTION_PROOF_REPAIR_VERIFICATION.md). Completion still depends on the required participants being available.

## Previously published: Windows 0.57.38 / Android 0.6.88

[Windows 0.57.38 release](https://github.com/jack-cal/SUMUWW/releases/tag/pc-v0.57.38) and [Android 0.6.88 release](https://github.com/jack-cal/SUMUWW/releases/tag/android-v0.6.88) describe the previous published binaries.

Those packages introduced the All blocks browser, verified-contact recovery, corrected retry accounting, longer bounded waits for slow public peers and faster proof-history scheduling. Existing wallets, valid history and all 34 UI languages are retained.

**A remaining connection interruption was observed.** The phone synchronized and hashed with the PC app off, but its sole external connection closed once and recovered after 13.39 seconds. Uninterrupted connectivity is not claimed. See the [measured verification and limitations](Documentation/PEER_RECOVERY_VERIFICATION_0.57.38_0.6.88.md).

## SMW/BTC trading starts at SUMUWW block 9100

**Conditional exchange transactions are enabled from SUMUWW block 9100.** Both
P2P editions require a current synchronized local SUMUWW full node. Setup,
wallet creation can happen earlier. In P2P 0.3.6, posting requires confirmed
paying funds and fees on an active paying chain; it does not bypass activation. Reaching 9100 alone does not guarantee a working trade.

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

[Whitepaper](Documentation/Whitepaper/WHITEPAPER.md) · [Connection proofs](Documentation/Whitepaper/CONNECTION_PROOFS_9000.md) · [Current verification](Documentation/CONNECTION_PROOF_REPAIR_VERIFICATION.md) · [Publication and document status](Documentation/CURRENT_STATUS.md)

The original issuance and halving schedule is preserved. Valid history through 8999 remains usable. From 9000, every block requires a producer-key commitment; random connection events use a 20% probability, and DGW recalculates every ten blocks with a 24-block observation window. Completed signatures are not a mining or block-acceptance prerequisite. The exact-template HTLC spending rule activates at 9100.

English is the publication language and the default for a fresh app profile. All 34 UI languages remain selectable. Saved language preferences are preserved, and document menus open the English edition.

## Release status

These node packages publish the post-PoW design described above, with the recorded local and isolated-network checks. They do not establish independent security certification, network-wide adoption, worldwide candidate discovery or irreversible finality. Read-only local checks on 24 October observed an active chain beyond height 9100. Read the specific limitations in the verification report and specification.

Previously withdrawn node releases remain withdrawn; the [withdrawal record](Archive/withdrawal-20261020/README.md) is retained. New [ordinary wallets](Wallet/README.md), [Explorer](Explorer/README.md) and [P2P](P2P/README.md) use the current shared core. Withdrawn older wallet binaries remain withdrawn. See [component changes, migration and verification limits](Documentation/COMPONENT_SUITE.md).

[Automatic beacon recovery](Documentation/BEACON_RECOVERY.md) is included in this release.

[Wallet, P2P and explorer fixes: UI, language and physical-device verification](Documentation/UI_LANGUAGE_VERIFICATION.md).

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. Rate suggestions still use the local pending queue; matching Bitcoin's sizing approach does not mean using Bitcoin's fee rates.

## Windows I2P component and security checks

Windows packages include official i2pd 3.0.0 with matching hashes and reseed certificates. Defender still detects the upstream I2P executable and ZIP in the recorded test. A matching upstream hash does not prove safety or establish a false positive. Any local file exception applies only to the computer where it is registered and is not installed by the public package. Other computers may block the same files.

<!-- /payment-policy-20261116 -->
