# SUMUWW Android 0.7.8 · Exploitation du nœud

Au redémarrage, le nœud repart du dernier bloc vérifié localement et vérifie les nouveaux blocs. Si la trace de vérification enregistrée est absente ou incohérente, il vérifie à nouveau l’historique stocké.

SUMUWW Android 0.7.8 · Le nœud valide, conserve, relaie et expose les données de la chaîne.

## Réseau et adresses

Le réseau public est `sumuww`, avec l’alias interne `dora`. Vérifiez le hash de genèse ci-dessous. Les adresses natives utilisent P2WPKH witness v0 et HASH160 d’une clé publique secp256k1 compressée. Aucun mémo ni tag n’est obligatoire. Rejetez les adresses d’un autre réseau et les sommes de contrôle invalides. Notez la branche réception/monnaie et l’index HD ; ne supposez pas le chemin de dérivation de Bitcoin.

## Recherche de transactions et de blocs

`getrawtransaction` recherche la chaîne active et le mempool, pas les seules branches orphelines. Les entrées désignent des sorties précédentes, pas une adresse d’expéditeur unique. `getblock` reçoit un `verbose` booléen ; un bloc inactif conservé a `active=false` et `confirmations=-1`. Ses transactions brutes restent accessibles par hash de bloc. `findspendingtransaction` ne cherche que les dépenses confirmées actives ; null ne prouve pas la disponibilité. Vérifiez `gettxout` avec `include_mempool=true`. Confirmations et état actif peuvent changer après réorganisation.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Frais, transaction vérifiée et compatibilité

Les frais correspondent à la somme des entrées moins celle des sorties. L’estimation ne compte une sortie de monnaie rendue que si le portefeuille crée effectivement une monnaie rendue suffisante. Un reliquat inférieur au seuil du portefeuille est ajouté aux frais ; les frais réels et le débit total sont présentés pour vérification. Le tarif s’exprime en yugeon/vB. La taille virtuelle est le poids de la transaction divisé par quatre, arrondi à l’entier supérieur.

Le portefeuille choisit les entrées et les sorties une seule fois, puis signe cette même transaction. La confirmation transmet la transaction signée conservée, sans la reconstruire ni recalculer ses frais. Une estimation expirée ou des entrées déjà dépensées imposent une nouvelle vérification. L’acceptation dans la file locale ne signifie pas une confirmation dans un bloc.

Pour un paiement P2WPKH ordinaire, le portefeuille produit des signatures low-R et low-S de 71 octets au maximum, octet SIGHASH_ALL compris. Il s’agit d’une politique de signature et d’estimation, pas d’une nouvelle limite de consensus pour les autres signatures valides. Une signature plus courte peut réduire la taille virtuelle réelle. 

## Compatibilité de la signature Android

Le format des fichiers du portefeuille, les adresses et les pièces existantes ne changent pas. La sauvegarde chiffrée existante peut être restaurée dans la nouvelle application pour retrouver le même portefeuille. Le nœud Android 0.6.103 et le portefeuille 1.1.14 utilisent une nouvelle clé de signature de publication. Ils ne peuvent pas remplacer une installation signée avec une autre clé. Conservez l’ancienne application et ses données jusqu’à disposer d’une sauvegarde chiffrée du portefeuille et d’un moyen de restauration fonctionnel. Ne désinstallez pas l’ancienne application uniquement pour forcer l’installation.

<!-- /payment-policy-20261116 -->

Après une réponse de version valide, le nœud laisse au pair le temps d’envoyer son accusé de réception. Si deux connexions sortantes mènent au même nœud, il conserve un chemin disponible jusqu’à la synchronisation.

<!-- poll-recovery-20261119 -->

La mise à jour de la synchronisation est relancée après une erreur interne. Une erreur sur un pair ne bloque plus les mises à jour des autres pairs. Le minage nécessite toujours un pair vérifié récemment ; une connexion ouverte ne suffit pas. Au démarrage, le minage sur téléphone attend désormais la synchronisation au lieu de s’arrêter immédiatement. Les blocages réseau pendant la vérification des preuves de connexion et la consultation de l’historique ont été corrigés. Le minage en arrière-plan reste actif.
