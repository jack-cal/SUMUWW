# Connection-proof repair — PC 0.57.40 / Android 0.6.89

The old runtime sampled historical contacts without a fresh availability check.

## Repair and compatibility

New jobs probe the entire discovered inventory using authenticated nonce echoes,
including relayed participants, then select three responsive identities using
the verified beacon. Silent contacts are retained for later attempts. This is
a local availability policy, not a consensus membership or admission rule.
Existing selected jobs preserve their exact message and three witnesses.
Valid partial replies are stored immediately and reused after failures and
restarts. Invalid saved replies are discarded and requested again. Phase,
missing-witness and error details persist. PC public history labels local job
outcomes separately from stored complete proofs. 

The attachment format, 20% event, three-signature validation, signature locks,
PoW, chain choice, wallet format and existing history are unchanged. Existing
v2 peers understand the probe. Old jobs may remain pending until their original
witnesses return. A new participant can also go offline after responding.
Ordinary wallets keep the prior repair versions, PC 1.0.2 / Android 1.1.2;
this producer-job repair does not require rebuilding those ordinary wallets.

