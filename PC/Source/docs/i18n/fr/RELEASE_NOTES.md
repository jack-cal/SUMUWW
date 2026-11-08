# SUMUWW · Notes de version

Le nœud ouvre normalement 10 connexions sortantes. La plupart relaient les blocs et les transactions. Une connexion de secours vérifiée peut relayer les blocs et une 11e connexion peut servir brièvement à découvrir d’autres pairs. La limite totale est de 125. Le nœud accepte jusqu’à 117 connexions entrantes, ou 115 avec 10 connexions sortantes. L’application de bureau affiche désormais uniquement le nombre total de nœuds connectés. Chaque appareil de minage construit ses propres blocs. Le nœud sur PC relaie les blocs terminés et refuse les demandes de travail de minage et les solutions envoyées par le téléphone.

Au redémarrage, le nœud repart du dernier bloc vérifié localement et vérifie les nouveaux blocs. Si la trace de vérification enregistrée est absente ou incohérente, il vérifie à nouveau l’historique stocké.


SUMUWW PC 0.57.54 · Le nœud valide, conserve, relaie et expose les données de la chaîne.

## Format de signature

Le SDK source facultatif assemble les transactions et vérifie les signatures fournies, sans clé ni réseau. Ce n’est ni un outil de signature ni une commande du nœud. La restriction P2WPKH concerne le format de l’exemple, pas le nœud. Le portefeuille personnel existant reste disponible.

## API RPC et HTTP

validateaddress vérifie la somme de contrôle et le réseau choisi. decoderawtransaction renvoie decoded_only, sans attester la signature ni la confirmation. Les sorties OP_RETURN conservent les données destinées aux programmes externes . Le nœud ajoute la consultation des frais, la vérification avant envoi, le suivi des remplacements RBF et la lecture ordonnée des données de bloc. La validation précède toute suppression de transaction en attente. Les signatures multiples et les sorties verrouillées sont implémentées pour des essais isolés ; elles ne sont pas encore activées sur le réseau public.

## Vérification

Exécutez python examples/node_contract.py depuis les sources après installation des dépendances. Des clés publiques de test et un regtest temporaire vérifient soumission, rejet, confirmations, réorganisation et conservation. Aucun fonds réel, profil personnel ou dispositif de signature matériel n’est utilisé.

[Documentation](README.html) · [Interface du nœud](EXCHANGE_INTEGRATION.html) · [API RPC et HTTP](RPC_API.html) · [Exploitation du nœud](NETWORK_RUNBOOK.html) · [Vérification](EXCHANGE_EXAMPLES.html)

[Référence détaillée en anglais](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)
