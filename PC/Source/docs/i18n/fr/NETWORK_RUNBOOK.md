# SUMUWW · Exploitation du nœud

Le nœud ouvre normalement 10 connexions sortantes. La plupart relaient les blocs et les transactions. Une connexion de secours vérifiée peut relayer les blocs et une 11e connexion peut servir brièvement à découvrir d’autres pairs. La limite totale est de 125. Le nœud accepte jusqu’à 117 connexions entrantes, ou 115 avec 10 connexions sortantes. L’application de bureau affiche désormais uniquement le nombre total de nœuds connectés. Chaque appareil de minage construit ses propres blocs. Le nœud sur PC relaie les blocs terminés et refuse les demandes de travail de minage et les solutions envoyées par le téléphone.

Au redémarrage, le nœud repart du dernier bloc vérifié localement et vérifie les nouveaux blocs. Si la trace de vérification enregistrée est absente ou incohérente, il vérifie à nouveau l’historique stocké.


SUMUWW PC 0.57.61 · Le nœud valide, conserve, relaie et expose les données de la chaîne.

## Réseau et adresses

Le réseau public est `sumuww`, avec l’alias interne `dora`. Vérifiez le hash de genèse ci-dessous. Les adresses natives utilisent P2WPKH witness v0 et HASH160 d’une clé publique secp256k1 compressée. Aucun mémo ni tag n’est obligatoire. Rejetez les adresses d’un autre réseau et les sommes de contrôle invalides. Notez la branche réception/monnaie et l’index HD ; ne supposez pas le chemin de dérivation de Bitcoin.

## Authentification et limites

Activez explicitement RPC sur la boucle locale numérique `127.0.0.1:18443`, avec son jeton Bearer privé. Aucune fonction de déverrouillage ou de signature distante n’est exposée. Utilisez un service local ou un tunnel authentifié ; les requêtes de navigateur Origin/Referer sont refusées. JSON-RPC utilise POST `/rpc`, `params` objet/tableau et `id` ; les notifications renvoient HTTP 204. Limites : corps 8004096 octets, en-têtes 8192, lots 16, requêtes simultanées 16, délai 10 secondes ; pagination limit 1–1000, offset 0–1000000. Il existe 28 méthodes et 11 routes REST.

## Recherche de transactions et de blocs

`getrawtransaction` recherche la chaîne active et le mempool, pas les seules branches orphelines. Les entrées désignent des sorties précédentes, pas une adresse d’expéditeur unique. `getblock` reçoit un `verbose` booléen ; un bloc inactif conservé a `active=false` et `confirmations=-1`. Ses transactions brutes restent accessibles par hash de bloc. `findspendingtransaction` ne cherche que les dépenses confirmées actives ; null ne prouve pas la disponibilité. Vérifiez `gettxout` avec `include_mempool=true`. Confirmations et état actif peuvent changer après réorganisation.

## Vérification

Exécutez python examples/node_contract.py depuis les sources après installation des dépendances. Des clés publiques de test et un regtest temporaire vérifient soumission, rejet, confirmations, réorganisation et conservation. Aucun fonds réel, profil personnel ou dispositif de signature matériel n’est utilisé.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Documentation](README.html) · [Interface du nœud](EXCHANGE_INTEGRATION.html) · [API RPC et HTTP](RPC_API.html) · [Notes de version](RELEASE_NOTES.html) · [Vérification](EXCHANGE_EXAMPLES.html)

[Référence détaillée en anglais](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Frais, transaction vérifiée et compatibilité

Les frais correspondent à la somme des entrées moins celle des sorties. L’estimation ne compte une sortie de monnaie rendue que si le portefeuille crée effectivement une monnaie rendue suffisante. Un reliquat inférieur au seuil du portefeuille est ajouté aux frais ; les frais réels et le débit total sont présentés pour vérification. Le tarif s’exprime en yugeon/vB. La taille virtuelle est le poids de la transaction divisé par quatre, arrondi à l’entier supérieur.

Le portefeuille choisit les entrées et les sorties une seule fois, puis signe cette même transaction. La confirmation transmet la transaction signée conservée, sans la reconstruire ni recalculer ses frais. Une estimation expirée ou des entrées déjà dépensées imposent une nouvelle vérification. L’acceptation dans la file locale ne signifie pas une confirmation dans un bloc.

Pour un paiement P2WPKH ordinaire, le portefeuille produit des signatures low-R et low-S de 71 octets au maximum, octet SIGHASH_ALL compris. Il s’agit d’une politique de signature et d’estimation, pas d’une nouvelle limite de consensus pour les autres signatures valides. Une signature plus courte peut réduire la taille virtuelle réelle. Les tarifs restent calculés à partir de la file locale : la méthode de dimensionnement ne reprend pas les tarifs du réseau Bitcoin.

## Composant I2P de Windows et contrôles de sécurité

Les paquets Windows contiennent i2pd 3.0.0 officiel, avec ses empreintes et certificats d’amorçage à jour. Dans le contrôle consigné, Defender détecte encore l’exécutable I2P et le ZIP officiels. Une empreinte identique à celle de l’éditeur ne prouve ni l’innocuité ni un faux positif. Une éventuelle exclusion locale ne concerne que le PC où elle est enregistrée ; le paquet public ne la configure pas. D’autres PC peuvent bloquer ces fichiers.

<!-- /payment-policy-20261116 -->

Après une réponse de version valide, le nœud laisse au pair le temps d’envoyer son accusé de réception. Si deux connexions sortantes mènent au même nœud, il conserve un chemin disponible jusqu’à la synchronisation. Le diagnostic intégré accepte un bloc à preuve de travail valide avant l’arrivée de la preuve de connexion. Il vérifie ensuite les signatures des trois témoins, la transmission de cette preuve et sa conservation après redémarrage.
