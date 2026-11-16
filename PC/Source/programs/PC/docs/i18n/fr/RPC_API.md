# SUMUWW · API RPC et HTTP

SUMUWW PC 0.57.51 · Le nœud valide, conserve, relaie et expose les données de la chaîne.

## API RPC et HTTP

validateaddress vérifie la somme de contrôle et le réseau choisi. decoderawtransaction renvoie decoded_only, sans attester la signature ni la confirmation. Les sorties OP_RETURN conservent les données destinées aux programmes externes . Le nœud ajoute la consultation des frais, la vérification avant envoi, le suivi des remplacements RBF et la lecture ordonnée des données de bloc. La validation précède toute suppression de transaction en attente. Les signatures multiples et les sorties verrouillées sont implémentées pour des essais isolés ; elles ne sont pas encore activées sur le réseau public.

## Authentification et limites

Activez explicitement RPC sur la boucle locale numérique `127.0.0.1:18443`, avec son jeton Bearer privé. Aucune fonction de déverrouillage ou de signature distante n’est exposée. Utilisez un service local ou un tunnel authentifié ; les requêtes de navigateur Origin/Referer sont refusées. JSON-RPC utilise POST `/rpc`, `params` objet/tableau et `id` ; les notifications renvoient HTTP 204. Limites : corps 8004096 octets, en-têtes 8192, lots 16, requêtes simultanées 16, délai 10 secondes ; pagination limit 1–1000, offset 0–1000000. Il existe 28 méthodes et 11 routes REST.

## Montants et sorties disponibles

`_units` désigne des unités minimales entières ; `_smw` une chaîne à 8 décimales ; `_dora` un alias compatible. Aucun champ monétaire `_sumuww` n’existe. 1 SMW = 100000000 unités. `gettxout` n’a pas de champ `spendable` et peut renvoyer une récompense immature. Une coinbase exige au moins 100 confirmations pour être dépensée au bloc suivant. Filtrez `listunspent` sur `spendable` ; le montant available de `getaddressbalance` exclut les fonds immatures ou engagés par des transactions en attente. Les nouvelles sorties du mempool ne sont pas confirmées. Vérifiez la pointe entre les pages et revalidez les entrées choisies.

1 SMW = 100 000 000 yugeon. Les frais automatiques proposent trois niveaux selon les observations locales, sans garantir le délai de confirmation. Vous pouvez saisir un taux en yugeon/vB. Vérifiez les frais définitifs et le total en SMW avant l’envoi. Une transaction refusée ne débite pas votre solde.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Les frais automatiques suivent le volume en attente, la capacité des blocs et la priorité des transactions, sans reprendre les frais passés. Si la file est peu chargée, le taux reste minimal. L’aperçu s’actualise ; la confirmation finale fixe les frais. Les observations concernent le nœud local connecté, pas tous les nœuds.

L’historique des remplacements observés par ce nœud est conservé après le redémarrage du portefeuille. Les transactions retirées ne modifient pas le solde.

L’historique de minage distingue l’émission nouvelle, les frais et la récompense totale de chaque bloc. Le montant reçu par votre portefeuille apparaît séparément. Une récompense partiellement réclamée ne permet pas d’attribuer les deux composantes. Le nœud fournit 28 méthodes RPC, dont l’estimation des frais, et valide et relaie les transactions signées.

## Recherche de transactions et de blocs

`getrawtransaction` recherche la chaîne active et le mempool, pas les seules branches orphelines. Les entrées désignent des sorties précédentes, pas une adresse d’expéditeur unique. `getblock` reçoit un `verbose` booléen ; un bloc inactif conservé a `active=false` et `confirmations=-1`. Ses transactions brutes restent accessibles par hash de bloc. `findspendingtransaction` ne cherche que les dépenses confirmées actives ; null ne prouve pas la disponibilité. Vérifiez `gettxout` avec `include_mempool=true`. Confirmations et état actif peuvent changer après réorganisation.

| method | params |
|---|---|
| `getblockchaininfo` | `{} / []` |
| `gethtlcinfo` | `{} / []` |
| `getspendinginfo` | `{} / []` |
| `getdatarecords` | `blockhash, offset=0, limit=100` |
| `decodescript` | `hex` |
| `gettxout` | `txid, index, include_mempool=true` |
| `findspendingtransaction` | `txid, index, start_height=0` |
| `getnetworkinfo` | `{} / []` |
| `getblockcount` | `{} / []` |
| `getbestblockhash` | `{} / []` |
| `getblockhash` | `height` |
| `getblock` | `hash, verbose=true` |
| `getrawmempool` | `{} / []` |
| `getmempoolinfo` | `{} / []` |
| `getmempoolpolicy` | `{} / []` |
| `estimatefee` | `vsize=140, mode=normal` |
| `testmempoolaccept` | `hex` |
| `getmempoolentry` | `txid` |
| `gettransactionstatus` | `txid` |
| `getrawtransaction` | `txid, verbose=true` |
| `decoderawtransaction` | `hex` |
| `validateaddress` | `address` |
| `listunspent` | `address, limit=100, offset=0` |
| `getaddressbalance` | `address` |
| `sendrawtransaction` | `hex` |
| `submitblock` | `hex` |
| `getblocktemplate` | `address` |
| `help` | `{} / []` |

| HTTP | URI | JSON |
|---|---|---|
| `GET` | `/api/v1/info` | `—` |
| `GET` | `/api/v1/network` | `—` |
| `GET` | `/api/v1/mempool` | `—` |
| `GET` | `/api/v1/mempool/info` | `—` |
| `GET` | `/api/v1/blocks/{height-or-hash}` | `—` |
| `GET` | `/api/v1/transactions/{txid}` | `—` |
| `GET` | `/api/v1/addresses/{address}/balance` | `—` |
| `GET` | `/api/v1/addresses/{address}/utxos?limit=100&offset=0` | `—` |
| `POST` | `/api/v1/transactions` | `{"hex":"..."}` |
| `POST` | `/api/v1/blocks` | `{"hex":"..."}` |
| `POST` | `/api/v1/mining/template` | `{"address":"..."}` |

[Documentation](README.html) · [Interface du nœud](EXCHANGE_INTEGRATION.html) · [Exploitation du nœud](NETWORK_RUNBOOK.html) · [Notes de version](RELEASE_NOTES.html) · [Vérification](EXCHANGE_EXAMPLES.html)

[Référence détaillée en anglais](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Frais, transaction vérifiée et compatibilité

Les frais correspondent à la somme des entrées moins celle des sorties. L’estimation ne compte une sortie de monnaie rendue que si le portefeuille crée effectivement une monnaie rendue suffisante. Un reliquat inférieur au seuil du portefeuille est ajouté aux frais ; les frais réels et le débit total sont présentés pour vérification. Le tarif s’exprime en yugeon/vB. La taille virtuelle est le poids de la transaction divisé par quatre, arrondi à l’entier supérieur.

Le portefeuille choisit les entrées et les sorties une seule fois, puis signe cette même transaction. La confirmation transmet la transaction signée conservée, sans la reconstruire ni recalculer ses frais. Une estimation expirée ou des entrées déjà dépensées imposent une nouvelle vérification. L’acceptation dans la file locale ne signifie pas une confirmation dans un bloc.

Pour un paiement P2WPKH ordinaire, le portefeuille produit des signatures low-R et low-S de 71 octets au maximum, octet SIGHASH_ALL compris. Il s’agit d’une politique de signature et d’estimation, pas d’une nouvelle limite de consensus pour les autres signatures valides. Une signature plus courte peut réduire la taille virtuelle réelle. Les tarifs restent calculés à partir de la file locale : la méthode de dimensionnement ne reprend pas les tarifs du réseau Bitcoin.

## Composant I2P de Windows et contrôles de sécurité

Les paquets Windows contiennent i2pd 3.0.0 officiel, avec ses empreintes et certificats d’amorçage à jour. Dans le contrôle consigné, Defender détecte encore l’exécutable I2P et le ZIP officiels. Une empreinte identique à celle de l’éditeur ne prouve ni l’innocuité ni un faux positif. Une éventuelle exclusion locale ne concerne que le PC où elle est enregistrée ; le paquet public ne la configure pas. D’autres PC peuvent bloquer ces fichiers.

<!-- /payment-policy-20261116 -->
