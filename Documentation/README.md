# SUMUWW documentation

[Current node documentation in 34 languages](../PC/Source/docs). The 26 October documentation archive remains available. [English whitepaper 2.4](https://github.com/jack-cal/SUMUWW/releases/download/updates-20261116/SUMUWW-Whitepaper-2.4.zip) and [documentation 20261026-r1](https://github.com/jack-cal/SUMUWW/releases/tag/docs-20261026-r1) are separate downloads.

- [Current versions, publication states and bundled-document erratum](CURRENT_STATUS.md)
- [Whitepaper 2.4](Whitepaper/WHITEPAPER.md) · [Changes](Whitepaper/CHANGELOG.md)
- [Connection-proof specification](Whitepaper/CONNECTION_PROOFS_9000.md)
- [Beacon recovery](BEACON_RECOVERY.md) · [HTLC reference](Whitepaper/HTLC_9100.md)
- [Historical build verification: PC 0.57.46 / Android 0.6.95](RELEASE_VERIFICATION_20261025.json)
- [Earlier connection repair verification](CONNECTION_PROOF_REPAIR_VERIFICATION.md)
- [Component suite and migration](COMPONENT_SUITE.md)
- [Historical whitepaper 2.1 archive](https://github.com/jack-cal/SUMUWW/releases/tag/whitepaper-v2.1-en)
- [P2P Full/Light comparison](../P2P/Source/EDITIONS.md) · [Bitcoin and block-9100 setup](../P2P/Source/BITCOIN_SETUP.md)

## Earlier verification records

- [Wallet/dependency repair](LOCAL_REPAIR_VERIFICATION.md)
- [PC 0.57.38 / Android 0.6.88 recovery](PEER_RECOVERY_VERIFICATION_0.57.38_0.6.88.md)
- [UI, language and physical-device checks, 22 October](UI_LANGUAGE_VERIFICATION.md)
- [Beacon recovery, PC 0.57.34 / Android 0.6.84](BEACON_RECOVERY_VERIFICATION.md)
- [PC 0.57.33 / Android 0.6.83](VERIFICATION.md)
- [Earlier withdrawal record](../Archive/withdrawal-20261020/Documentation/README.md)

Historical reports apply to their named versions and test environments, not to
every later build. A published document or application does not mean it was installed.

[Block-9,600 upgrade](UPGRADE_9600_STATUS.md) · [Current verification](RELEASE_VERIFICATION_20261026.md). Publication does not install an update on other users’ devices.

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. Rate suggestions still use the local pending queue; matching Bitcoin's sizing approach does not mean using Bitcoin's fee rates.

## Windows I2P component and security checks

Windows packages include official i2pd 3.0.0 with matching hashes and reseed certificates. Defender still detects the upstream I2P executable and ZIP in the recorded test. A matching upstream hash does not prove safety or establish a false positive. Any local file exception applies only to the computer where it is registered and is not installed by the public package. Other computers may block the same files.

<!-- /payment-policy-20261116 -->
