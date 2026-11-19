# SUMUWW Explorer 0.4.11

Run start-explorer.cmd after extracting the complete Windows ZIP. The explorer
reads a local SUMUWW node database in read-only mode and writes only its own,
separate index. Use --database to select another node.sqlite. It does not
independently synchronize or validate the chain. Displayed history is the
selected node's active chain, including rewards and transactions from all nodes.
Address searches narrow the view to that address; they do not limit the main
block or transaction lists to your wallet.

## Current release

Explorer 0.4.11 fixes wrapping menus at intermediate widths and deterministic locale fallback. Download version 0.4.11 from https://github.com/jack-cal/SUMUWW/releases/tag/explorer-v0.4.11. Validating nodes and ordinary wallets must be updated for the source-block 9,600 rule. This read-only explorer does not itself select the network chain.

## Proof scope

The explorer's proof download is a TXID Merkle inclusion proof for a transaction
inside a block. It is not the asynchronous connection proof created by three
witnesses, and the explorer currently has no connection-job completion counter.
Use the full node's public history/status for those separate job/proof counters.
An inclusion proof does not establish consensus validity or irreversible finality.

## Trading applications

P2P Full and Light are separate applications. Both require a synchronized
SUMUWW node and HTLC activation at height 9100. Full also requires synchronized,
unpruned Bitcoin Core with txindex. Light verifies Bitcoin headers and proofs
and depends on available honest servers for complete histories. An advertisement
or reservation does not transfer funds.

## 0.4.11

The explorer shows fee rates in yugeon/vB. When the local node has recorded a transaction replacement, the transaction page links to the replacement. Confirmed chain records take precedence; local replacement history is limited.

[Current features in 34 languages](docs/features/index.html).
