# SUMUWW Android 0.6.103 · Notes de version

Pour une entrée de 1 SMW, les frais varient selon qu’il faut vous rendre la monnaie ou non. Avec des entrées et sorties P2WPKH et un taux de 1 yugeon/vB, envoyer 0.99999890 SMW coûte 110 yugeon, sans monnaie à rendre. Envoyer 0.8 SMW à partir de la même entrée ajoute une sortie de change et porte les frais à 141 yugeon. Le portefeuille rend la monnaie si le montant restant après les frais atteint un seuil qui tient compte du coût à payer pour la dépenser plus tard. En dessous de ce seuil, le reste est inclus dans les frais affichés avant confirmation. Pour une entrée du portefeuille en SegWit natif (P2WPKH), l’estimation prévoit jusqu’à 71 octets pour la signature, type de hachage compris.

Au redémarrage, le nœud repart du dernier bloc vérifié localement et vérifie les nouveaux blocs. Si la trace de vérification enregistrée est absente ou incohérente, il vérifie à nouveau l’historique stocké.

SUMUWW Android 0.6.103 · Le nœud valide, conserve, relaie et expose les données de la chaîne.

[Documentation](../../integration/docs/i18n/fr/RELEASE_NOTES.html)

<!-- payment-policy-20261116 -->

## Frais, transaction vérifiée et compatibilité

Les frais correspondent à la somme des entrées moins celle des sorties. L’estimation ne compte une sortie de monnaie rendue que si le portefeuille crée effectivement une monnaie rendue suffisante. Un reliquat inférieur au seuil du portefeuille est ajouté aux frais ; les frais réels et le débit total sont présentés pour vérification. Le tarif s’exprime en yugeon/vB. La taille virtuelle est le poids de la transaction divisé par quatre, arrondi à l’entier supérieur.

Le portefeuille choisit les entrées et les sorties une seule fois, puis signe cette même transaction. La confirmation transmet la transaction signée conservée, sans la reconstruire ni recalculer ses frais. Une estimation expirée ou des entrées déjà dépensées imposent une nouvelle vérification. L’acceptation dans la file locale ne signifie pas une confirmation dans un bloc.

Pour un paiement P2WPKH ordinaire, le portefeuille produit des signatures low-R et low-S de 71 octets au maximum, octet SIGHASH_ALL compris. Il s’agit d’une politique de signature et d’estimation, pas d’une nouvelle limite de consensus pour les autres signatures valides. Une signature plus courte peut réduire la taille virtuelle réelle. 

## Compatibilité de la signature Android

Le format des fichiers du portefeuille, les adresses et les pièces existantes ne changent pas. La sauvegarde chiffrée existante peut être restaurée dans la nouvelle application pour retrouver le même portefeuille. Le nœud Android 0.6.103 et le portefeuille 1.1.14 utilisent une nouvelle clé de signature de publication. Ils ne peuvent pas remplacer une installation signée avec une autre clé. Conservez l’ancienne application et ses données jusqu’à disposer d’une sauvegarde chiffrée du portefeuille et d’un moyen de restauration fonctionnel. Ne désinstallez pas l’ancienne application uniquement pour forcer l’installation.

<!-- /payment-policy-20261116 -->
