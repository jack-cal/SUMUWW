

# Wallet recovery and distribution repair — 2026-10-24

## Code changes

The Windows wallet is rebuilt against the current shared desktop core. Android
receives the corresponding Android chain, link_runtime, peer, peer_discovery,
wire and core-version modules; platform adapters and app identity are retained.
Verified peers survive temporary failures; failure accounting is not duplicated
or converted into success after a response timeout. Missing inbound listener
hints are independently verified before sharing. Public outgoing handshakes and
responses have bounded 120-second waits while partial frames keep short deadlines.
Validated ancestry is reused only for a matching snapshot, height and hash.
Background proof-history work yields between jobs.

Wallet formats, addresses, balances, valid history and consensus are unchanged.

All 34 UI language catalogs and saved language preferences are retained.  

## Dependency and packaging corrections

Five Windows declarations now match the bundled versions: cffi 2.1.1,
cytoolz 1.2.0, eth-typing 6.0.0, eth-utils 6.0.0 and pycparser 3.12.
The lock includes the complete 16-package runtime closure, including Pydantic
dependencies.  Both Windows build entry points
reject a version mismatch between requirements, the hash lock and the environment.
Android has separate ABI-specific pins; matching Windows versions is not required.

 Broken relative
document/license links are repaired.  
Each local component checksum file uses paths relative to its own directory.
The root SHA256SUMS.txt covers every distribution file except itself and
FILE_HASHES.json. FILE_HASHES.json additionally covers SHA256SUMS.txt and excludes
only itself, so nested checksum files are included.

