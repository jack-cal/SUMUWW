# SUMUWW · Notes de version

Pour une entrée de 1 SMW, les frais varient selon qu’il faut vous rendre la monnaie ou non. Avec des entrées et sorties P2WPKH et un taux de 1 yugeon/vB, envoyer 0.99999890 SMW coûte 110 yugeon, sans monnaie à rendre. Envoyer 0.8 SMW à partir de la même entrée ajoute une sortie de change et porte les frais à 141 yugeon. Le portefeuille rend la monnaie si le montant restant après les frais atteint un seuil qui tient compte du coût à payer pour la dépenser plus tard. En dessous de ce seuil, le reste est inclus dans les frais affichés avant confirmation. Pour une entrée du portefeuille en SegWit natif (P2WPKH), l’estimation prévoit jusqu’à 71 octets pour la signature, type de hachage compris.

0.57.61 · Lorsque vous changez de langue dans l’application, son icône change aussi dans la barre des tâches de Windows.

Le nœud ouvre normalement 10 connexions sortantes. La plupart relaient les blocs et les transactions. Une connexion de secours vérifiée peut relayer les blocs et une 11e connexion peut servir brièvement à découvrir d’autres pairs. La limite totale est de 125. Le nœud accepte jusqu’à 117 connexions entrantes, ou 115 avec 10 connexions sortantes. L’application de bureau affiche désormais uniquement le nombre total de nœuds connectés. Chaque appareil de minage construit ses propres blocs. Le nœud sur PC relaie les blocs terminés et refuse les demandes de travail de minage et les solutions envoyées par le téléphone.

Au redémarrage, le nœud repart du dernier bloc vérifié localement et vérifie les nouveaux blocs. Si la trace de vérification enregistrée est absente ou incohérente, il vérifie à nouveau l’historique stocké.

SUMUWW PC 0.57.61 · Le nœud valide, conserve, relaie et expose les données de la chaîne.

## Format de signature

Le SDK source facultatif assemble les transactions et vérifie les signatures fournies, sans clé ni réseau. Ce n’est ni un outil de signature ni une commande du nœud. La restriction P2WPKH concerne le format de l’exemple, pas le nœud. Le portefeuille personnel existant reste disponible.

## API RPC et HTTP

validateaddress vérifie la somme de contrôle et le réseau choisi. decoderawtransaction renvoie decoded_only, sans attester la signature ni la confirmation. Les sorties OP_RETURN conservent les données destinées aux programmes externes . Le nœud ajoute la consultation des frais, la vérification avant envoi, le suivi des remplacements RBF et la lecture ordonnée des données de bloc. La validation précède toute suppression de transaction en attente. Les signatures multiples et les sorties verrouillées sont implémentées pour des essais isolés ; elles ne sont pas encore activées sur le réseau public.

## Vérification

Exécutez python examples/node_contract.py depuis les sources après installation des dépendances. Des clés publiques de test et un regtest temporaire vérifient soumission, rejet, confirmations, réorganisation et conservation. Aucun fonds réel, profil personnel ou dispositif de signature matériel n’est utilisé.

[Documentation](README.html) · [Interface du nœud](EXCHANGE_INTEGRATION.html) · [API RPC et HTTP](RPC_API.html) · [Exploitation du nœud](NETWORK_RUNBOOK.html) · [Vérification](EXCHANGE_EXAMPLES.html)

[Référence détaillée en anglais](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Frais, transaction vérifiée et compatibilité

Les frais correspondent à la somme des entrées moins celle des sorties. L’estimation ne compte une sortie de monnaie rendue que si le portefeuille crée effectivement une monnaie rendue suffisante. Un reliquat inférieur au seuil du portefeuille est ajouté aux frais ; les frais réels et le débit total sont présentés pour vérification. Le tarif s’exprime en yugeon/vB. La taille virtuelle est le poids de la transaction divisé par quatre, arrondi à l’entier supérieur.

Le portefeuille choisit les entrées et les sorties une seule fois, puis signe cette même transaction. La confirmation transmet la transaction signée conservée, sans la reconstruire ni recalculer ses frais. Une estimation expirée ou des entrées déjà dépensées imposent une nouvelle vérification. L’acceptation dans la file locale ne signifie pas une confirmation dans un bloc.

Pour un paiement P2WPKH ordinaire, le portefeuille produit des signatures low-R et low-S de 71 octets au maximum, octet SIGHASH_ALL compris. Il s’agit d’une politique de signature et d’estimation, pas d’une nouvelle limite de consensus pour les autres signatures valides. Une signature plus courte peut réduire la taille virtuelle réelle. 

<!-- /payment-policy-20261116 -->
