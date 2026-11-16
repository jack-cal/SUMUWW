# SUMUWW update — 16 November 2026

| Component | Reviewed version |
|---|---|
| Windows validating node and miner | 0.57.61 |
| Windows ordinary wallet | 1.0.15 |
| Android validating node and miner | 0.6.103 |
| Android ordinary wallet | 1.1.14 |
| Whitepaper | 2.4 |

Ordinary payment quotes now include a change output only when viable change is actually created. The same selected inputs, exact outputs and fee are signed and retained for confirmation; submission does not reconstruct the transaction. Ordinary wallet P2WPKH signatures use low-R/low-S and a maximum 71-byte signature item including its hash-type byte. This is wallet policy, not a new consensus limit. See [the detailed payment policy](PAYMENT_POLICY.md).

Windows packages use official i2pd 3.0.0 with updated hashes and reseed certificates. In the recorded Microsoft Defender component check, the three SUMUWW application executables were not detected, while the official I2P executable and upstream ZIP were still detected. Matching official hashes confirm the compared artifact identity, not a malware verdict or an independent audit. Local file exceptions are machine settings and are not installed or exported by the public packages. Other computers may block the same I2P files.

## Android: changed signing identity

The Android node and wallet packages in this update are signed with a newly generated release key. They cannot update an older installation signed with a different certificate. The node package is `org.sumuww.miner`; the ordinary wallet is `org.sumuww.wallet.current`. The new certificate SHA-256 is:

`e609c42039cd7b9aa47d921d016ed305b6091dd0b7bb5a820f7b373c3ad66f38`

Keep the installed app and its data until an encrypted wallet backup and a working recovery method are secured. Do not uninstall an old application merely to force installation. The new signing identity is not advertised as an automatic in-place update to the previous Android signing lineage. Both release APKs were installed over the previous same-certificate builds and launched on an Android 11 x86-64 emulator. Their packaged Python payment, signing and peer-recovery tests ran on that emulator. Physical phones and cellular carriers were outside this run.

## Documentation and verification

Whitepaper 2.4 and the affected protocol, wallet and operating explanations distinguish actual transaction fees, fee-rate suggestions, change policy, quote reuse and local signature limits. The changed explanations and compatibility notices are directly authored in all 34 languages. English remains the primary publication language and the first-launch UI default; saved language choices are retained.

Existing issuance, valid chain history, block acceptance, difficulty and connection-proof activation rules are preserved. P2P Full/Light trading and Explorer retain their separate documented scope. Test results and remaining verification limitations accompany this release; local or isolated-network checks do not prove uninterrupted public-network availability.

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized. The built-in diagnostic accepts a valid proof-of-work block before a connection proof is available, then checks the proof's three witness signatures, relay and persistence after restart.
