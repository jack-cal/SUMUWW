# SUMUWW release verification — 9 November 2026

Android full node 0.6.99 is based on the independent 0.6.96 full node and CPU miner. A Galaxy S24 Ultra retained its application data during the upgrade, opened the existing encrypted wallet, synchronized with peers and showed the same receiving address and confirmed balance as the pre-upgrade wallet and the Windows node, respectively.

| Component | Checks performed |
|---|---|
| Windows full node 0.57.54 | Ran the node test suite. Re-ran the recovery-word and seed-dialog modules with the checked-in word list and the startup-summary module with the current restart expectation. Verified mining, reopening and full validation with the packaged executable on a disposable chain. |
| Android full node 0.6.99 | Verified release signing and the installed APK hash. The emulator exercised database migration, normal restart, process loss during a block write, recovery, wallet identity, transaction submission, reorganization, fee controls, update checks, language lookup and offline documents. |
| Windows wallet 1.0.10 | Passed 11 wallet tests and the packaged application's self-check. |
| Android wallet 1.1.10 | Passed 15 wallet runtime tests and seven emulator UI tests, including send review, confirmed receipt and language changes. The send test enters a fee rate in yugeon/vB. |
| Explorer 0.4.11 | Passed 158 Python tests and 47 JavaScript UI tests. The Windows executable served the homepage and returned the expected genesis block through its overview API. |
| P2P Full and Light 0.3.6 | Exercised funded orders, confirmation, claim, refund and recovery with isolated SUMUWW and Bitcoin networks. Both packaged applications passed their self-checks. Checked the 76 files in the vendored source manifest and re-ran its integrity test with the recorded line endings. |
| Whitepaper 2.3, documentation revision 2 | Checked all 117 listed files in the release archive, desktop distribution and source tree. The two genesis examples reproduce the mainnet hash, header and block. Checked local documentation links in eight binary and whitepaper packages, including the 34 Android language editions. |

The Windows node independently verified stored mainnet connection proofs at source heights 11,259, 11,273 and 11,277, including the witness selection certificates and signatures. Test transfers and atomic swaps used disposable funds.

The test environment skipped checks requiring a separate private-IPv4 LAN interface or Windows symbolic-link privileges. The completed runs establish the observed behavior on these devices and fixtures.

[Android release and checksums](https://github.com/jack-cal/SUMUWW/releases/tag/android-v0.6.99)
