# SUMUWW Wallet 1.0.15

The node normally opens 10 outbound connections, mostly to relay blocks and transactions. It can use a verified backup for blocks and briefly open an 11th connection to discover peers. The overall limit is 125. Up to 117 inbound connections are possible, or 115 with 10 outbound connections.

Core version label now reads the bundled runtime version. Release 1.0.8: https://github.com/jack-cal/SUMUWW/releases/tag/wallet-pc-v1.0.8.

SUMUWW 1.0.8 — update before block 9,600. See UPGRADE_9600.md and the local 34-language upgrade9600 guide.

# SUMUWW Wallet for Windows 1.0.15

An ordinary wallet with receive, send, activity, encrypted backup, recovery,
automatic lock and 34 offline interface languages. English is the first-launch
default. Existing SUMUWW artwork is retained.

Extract the complete Windows ZIP and run `SUMUWW-Wallet.exe`. Python is included.
Data is stored separately in `%LOCALAPPDATA%/SUMUWW/Wallet-PC`. The full node can
run alongside it. Import an encrypted wallet backup or restore its recovery
words to use an existing address. Originals are never overwritten. Keep both the
encrypted backup and its password. Recovery words are displayed only on request.

This wallet synchronizes and validates the chain locally with core 0.57.47. It
does not offer mining controls or depend on a remote server to sign payments.
It is not a lightweight/SPV client. Initial synchronization requires peers and
storage for the blockchain. Settings allows adding a reachable peer address.

Before sending, inspect the complete recipient, amount, fee and total in the
confirmation dialog. A confirmed action consumes one expiring quote. No automatic
payment retry is performed. A local submission is not a confirmed transaction.

Valid legacy history through height 8,999 remains usable. From 9,000 inclusive,
old-rule blocks are rejected. The 20% post-PoW proof event, DGW every ten blocks,
original issuance/halvings and asynchronous proof recovery match the full node.

For source execution use Windows Python 3.12 with the pinned dependencies in
`../../PC/Source/requirements.txt`, then `python run.py`. Build with PyInstaller
using `SUMUWW-Wallet.spec`. Desktop tests use disposable regtest wallets only.
The executable is not publisher-code-signed.

## 1.0.8

1 SMW = 100,000,000 yugeon. Automatic fees offer slow, normal and fast presets based on local observations; they do not guarantee confirmation times. You can enter a rate in yugeon/vB manually. Review the final fee and total in SMW before sending. A rejected transaction does not debit your balance.

[Current features in 34 languages](docs/features/index.html).

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. Rate suggestions still use the local pending queue; matching Bitcoin's sizing approach does not mean using Bitcoin's fee rates.

## Windows I2P component and security checks

Windows packages include official i2pd 3.0.0 with matching hashes and reseed certificates. Defender still detects the upstream I2P executable and ZIP in the recorded test. A matching upstream hash does not prove safety or establish a false positive. Any local file exception applies only to the computer where it is registered and is not installed by the public package. Other computers may block the same files.

<!-- /payment-policy-20261116 -->
