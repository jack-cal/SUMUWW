# SUMUWW Android user guide

For a 1 SMW input, the fee depends on whether the transaction needs change. With P2WPKH inputs and outputs at 1 yugeon/vB, sending 0.99999890 SMW costs 110 yugeon and leaves no change. Sending 0.8 SMW from the same input creates a change output and costs 141 yugeon. The wallet creates change only if the amount left after paying the fee meets the minimum for a change output. This minimum accounts for the cost of spending the change later. A smaller remainder goes into the fee shown before you confirm. For a native SegWit wallet input (P2WPKH), the estimate allows up to 71 bytes for the signature, including its hash type.

## Wallet and installation

Install or update using the signed APK. Keep an encrypted wallet backup and recovery words before updating or changing devices. Open an existing wallet, create one or restore it through Wallet management. Never share wallet passwords, private keys or recovery words.

The phone operates its own node and wallet. A PC wallet is not required. Connect to a compatible peer and complete synchronization before main-network mining.

## Main screens and transfers

Home, Mining, Wallet and More display the current node and wallet status. Send shows the recipient, amount, fee and total debit before submission. Receive provides the wallet address for copying or sharing. History distinguishes pending and confirmed transactions. A transfer is confirmed only after inclusion in the active chain; its confirmation count can change after a chain reorganization.

Newly issued mining rewards require a spending block height at least 100 greater than their creation height. An ordinary transfer of a mature reward does not impose another 100-block maturity period on the recipient.

## Mining and protection

Start and Stop control the current mining batch. Total elapsed time includes preparation and waiting. Search duration measures wall time inside nonce search, including operating-system scheduling delays. H/s reports attempted hashes and does not predict when a reward will be found. Network waiting accumulates across the batch.

Android scheduling and power management can reduce background speed or interrupt operation. The battery floor defaults to 15 percent, and mining stops at or below the configured floor. Battery and thermal protections also stop mining when their conditions are met. Restarting after a protection stop is manual. Allowing background operation does not guarantee the same speed as foreground operation.

## Language and appearance

Settings provide 34 languages, light/dark appearance, colors and seasonal themes. Traditional Mongolian uses vertical text. Node connections, mining controls, backup, recovery and help are available in the app settings.

## Permissions and consent

Review before using SUMUWW. Required agreements must be accepted before the node starts. Mining starts only when you press Start.

[Required] Device mining and background operation: CPU, battery and mobile data are used. Heat and reduced performance are possible. Mining and node traffic can continue while another app is open or the screen is off. Stop from SUMUWW or its notification.

[Required] Peer communication: blocks and transactions are exchanged over the Internet. Peers can see your connection IP. Addresses and confirmed transactions are public on the blockchain; never disclose your password or recovery words.

Withdrawing required consent stops the node and mining and returns to the consent screen. Wallet and chain files are preserved.

## IP protection

Tor and I2P are optional and bundled with SUMUWW. Only the selected router runs; Direct runs neither. No separate router installation or port setting is needed. If a private connection fails, it does not switch to Direct. I2P requires b32.i2p peers.

Local router port: Tor SOCKS5 `127.0.0.1:9050`; I2P SAM `127.0.0.1:7656`.

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

## Android signing compatibility

Wallet file formats, addresses and existing coins are unchanged. The existing encrypted wallet backup can be restored in the new app to use the same wallet. Android node 0.6.103 and wallet 1.1.14 use a newly generated release signing key. They cannot replace an installation signed with a different key. Keep the existing app and its data until an encrypted wallet backup and a working recovery method are available. Do not uninstall an old app merely to make an update install.

<!-- /payment-policy-20261116 -->

After a valid version reply, the node gives its peer time to acknowledge it. If two outgoing connections reach the same node, it keeps an available route until one has synchronized. 
