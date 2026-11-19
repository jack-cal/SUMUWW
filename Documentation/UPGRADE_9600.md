# SUMUWW connection proof upgrade at source block 9,600

Update every validating node and ordinary wallet before block 9,600. This is a block-height deadline, not a guaranteed calendar date. The new required rule applies to proofs whose source block is at least 9,600. Earlier valid proofs and chain history remain valid. Proof absence never blocks ordinary PoW mining or block acceptance. Equal-work branch selection can differ on old versions; do not keep operating an old validating client after activation.

The existing beacon, 20% event probability and three-witness sampler remain unchanged. After activation, each candidate supplies a signed activity response bound to the source, target, recent round and nonce. More than two thirds of the PoW-anchored beacon generation must approve the complete responder list they independently observed. Validators recompute the sampled witnesses from that certificate. The certificate proves this quorum's observations, not independent human ownership or universal Internet reachability. Byzantine-quorum control and identity concentration remain security assumptions.

Before activation, old proof rules remain in force. Once activated, unfinished old jobs may move to a newly certified activity round while preserving their exact original block pair and archiving earlier witness messages and replies. Missing upgraded quorum members or a missing target producer can still delay completion. Failed jobs back off up to 15 minutes and retain their next retry across restart. All history exposes pending phases and witness reply counts. No private key or signature material is returned by the progress API.

Multipart messages are limited to 16 MiB each, 64 MiB of declared concurrent payloads and 120 seconds total duration. Inventory sync pages the complete list without limiting the discovered candidate population.

P2P 0.3.5 estimates network fees from the current queue, supports manual positive rates and reviewed child transactions to increase pending package fees without replacing agreed funding references. Agreed amounts and HTLC fee reserves remain fixed. Higher claim/refund fees can use additional owned inputs. Definite preflight rejection does not mark a new operation submitted; unknown broadcast outcomes remain reserved. Canceling unsubmitted previews releases their input reservations. Refunds depend only on the chain holding the user's funds. Fee estimates are local observations and do not guarantee confirmation times.

Versions: Windows node 0.57.47; Android node 0.6.96 (156); Windows wallet 1.0.8; Android Wallet Current 1.1.7 (18); P2P Full and Light 0.3.5. Explorer 0.4.11 fixes wrapped navigation and locale formatting; it remains a read-only chain browser.    

