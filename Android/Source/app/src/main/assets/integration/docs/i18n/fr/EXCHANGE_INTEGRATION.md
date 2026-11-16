# SUMUWW Android 0.6.103 · Interface du nœud

SUMUWW Android 0.6.103 · Le nœud valide, conserve, relaie et expose les données de la chaîne.

La spécification API décrit le cœur du nœud intégré. L’application Android n’a pas d’écran de configuration RPC.

## Réseau et adresses

Le réseau public est `sumuww`, avec l’alias interne `dora`. Vérifiez le hash de genèse ci-dessous. Les adresses natives utilisent P2WPKH witness v0 et HASH160 d’une clé publique secp256k1 compressée. Aucun mémo ni tag n’est obligatoire. Rejetez les adresses d’un autre réseau et les sommes de contrôle invalides. Notez la branche réception/monnaie et l’index HD ; ne supposez pas le chemin de dérivation de Bitcoin.

## API RPC et HTTP

validateaddress vérifie la somme de contrôle et le réseau choisi. decoderawtransaction renvoie decoded_only, sans attester la signature ni la confirmation. Les sorties OP_RETURN conservent les données destinées aux programmes externes . Le nœud ajoute la consultation des frais, la vérification avant envoi, le suivi des remplacements RBF et la lecture ordonnée des données de bloc. La validation précède toute suppression de transaction en attente. Les signatures multiples et les sorties verrouillées sont implémentées pour des essais isolés ; elles ne sont pas encore activées sur le réseau public.

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

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Frais, transaction vérifiée et compatibilité

Les frais correspondent à la somme des entrées moins celle des sorties. L’estimation ne compte une sortie de monnaie rendue que si le portefeuille crée effectivement une monnaie rendue suffisante. Un reliquat inférieur au seuil du portefeuille est ajouté aux frais ; les frais réels et le débit total sont présentés pour vérification. Le tarif s’exprime en yugeon/vB. La taille virtuelle est le poids de la transaction divisé par quatre, arrondi à l’entier supérieur.

Le portefeuille choisit les entrées et les sorties une seule fois, puis signe cette même transaction. La confirmation transmet la transaction signée conservée, sans la reconstruire ni recalculer ses frais. Une estimation expirée ou des entrées déjà dépensées imposent une nouvelle vérification. L’acceptation dans la file locale ne signifie pas une confirmation dans un bloc.

Pour un paiement P2WPKH ordinaire, le portefeuille produit des signatures low-R et low-S de 71 octets au maximum, octet SIGHASH_ALL compris. Il s’agit d’une politique de signature et d’estimation, pas d’une nouvelle limite de consensus pour les autres signatures valides. Une signature plus courte peut réduire la taille virtuelle réelle. Les tarifs restent calculés à partir de la file locale : la méthode de dimensionnement ne reprend pas les tarifs du réseau Bitcoin.

## Compatibilité de la signature Android

Le format des fichiers du portefeuille, les adresses et les pièces existantes ne changent pas. La sauvegarde chiffrée existante peut être restaurée dans la nouvelle application pour retrouver le même portefeuille. Le nœud Android 0.6.103 et le portefeuille 1.1.14 utilisent une nouvelle clé de signature de publication. Ils ne peuvent pas remplacer une installation signée avec une autre clé. Conservez l’ancienne application et ses données jusqu’à disposer d’une sauvegarde chiffrée du portefeuille et d’un moyen de restauration fonctionnel. Ne désinstallez pas l’ancienne application uniquement pour forcer l’installation.

<!-- /payment-policy-20261116 -->
