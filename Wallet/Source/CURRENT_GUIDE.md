SUMUWW Wallet Current 1.1.6 — Android

Ordinary wallet with send, receive, transaction history, encrypted backups,
recovery words, automatic lock, and 34 offline interface languages. English is
the first-launch default. Existing artwork and wallet UI are retained.

This is a separate application, org.sumuww.wallet.current. It does not overwrite
or uninstall the withdrawn org.sumuww.wallet application. The old application's
signing key was not found in this workspace, so an in-place update cannot be
claimed. Keep the old application and its data. Import an encrypted backup or
restore the recovery words in the new app to retain the same address and keys.
Never share a password or recovery phrase. The original wallet is not modified.

The wallet uses SUMUWW PC 0.57.46 / Android 0.6.95 validation code validation code. Valid legacy
blocks through 8999 are retained; old-rule blocks at 9000 and later are rejected.
Post-PoW connection events use a 20% probability. A block producer collects three
witness signatures after mining, splits each into two parts and binds evidence
to the exact parent/child pair. Mining and block acceptance never wait for this
proof. Valid cumulative work stays primary. Completed evidence can resolve equal
work; it does not guarantee finality. Threshold beacon recovery is included.
DGW uses a 24-block window and adjusts at 9000, 9010, 9020, and so on. Existing
issuance and halving rules remain unchanged. HTLC spending activates at 9100.

This is a validating wallet without mining controls, not an SPV/light client.
It synchronizes and stores the chain locally. A peer connection is required for
new blocks and transactions. Public-money swaps are not part of this wallet.

Build with JDK 17, Gradle 8.10.2, Python 3.13, Android SDK 35, NDK 27.2.12479018
and CMake 3.22.1. Set local.properties and DORA_BUILD_PYTHON locally, then run
assembleRelease and testDebugUnitTest. Private signing material is never included.
This update retains the SUMUWW Wallet Current 1.1.0 signing
identity, different from the original standalone-wallet certificate. Future
Current updates must retain this key. Private signing material stays outside
source and releases. Set SUMUWW_WALLET_SIGNING_DIR and ANDROID_SDK_ROOT, then
use tools/sign_release.py to sign a prepared release APK.

Host tests: tools/check_wallet_host.py, plus the current pc_tests protocol suite.
Android instrumentation: CurrentLinksTest uses disposable files in the cache.
Older V4 tests are historical fixtures and are not the current activation design.
Do not treat a successful build or host test as physical Android verification.

Version 1.1.2 (versionCode 13) updates Wallet Current 1.1.0 in place with the
same application ID and certificate. See the repository UI_LANGUAGE_VERIFICATION
report for historical physical-device and multilingual caption checks.
Those earlier device results are not a physical-device test of version 1.1.2.
See RELEASE_NOTES.txt for the current build and verification scope.

## 1.1.6

1 SMW = 100,000,000 yugeon. Automatic fees offer slow, normal and fast presets based on local observations; they do not guarantee confirmation times. You can enter a rate in yugeon/vB manually. Review the final fee and total in SMW before sending. A rejected transaction does not debit your balance.

For a 1 SMW input, the fee depends on whether the transaction needs change. With P2WPKH inputs and outputs at 1 yugeon/vB, sending 0.99999890 SMW costs 110 yugeon and leaves no change. Sending 0.8 SMW from the same input creates a change output and costs 141 yugeon. The wallet creates change only if the amount left after paying the fee meets the minimum for a change output. This minimum accounts for the cost of spending the change later. A smaller remainder goes into the fee shown before you confirm. For a native SegWit wallet input (P2WPKH), the estimate allows up to 71 bytes for the signature, including its hash type.


[Current features in 34 languages](docs/features/index.html).

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. Rate suggestions still use the local pending queue; matching Bitcoin's sizing approach does not mean using Bitcoin's fee rates.

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.103 and wallet 1.1.14 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized. The built-in diagnostic accepts a valid proof-of-work block before a connection proof is available, then checks the proof's three witness signatures, relay and persistence after restart.
