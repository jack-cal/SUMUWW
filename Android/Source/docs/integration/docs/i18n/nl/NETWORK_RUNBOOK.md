# SUMUWW Android 0.6.98 · Nodebeheer

De telefoon maakt verbinding met een volledige SUMUWW-node met versie 0.57.49 of hoger. Hij controleert de beloning en berekent het werkbewijs zonder de hele transactiegeschiedenis te downloaden.

## Netwerk en adressen

Het publieke netwerk is `sumuww`, intern ook `dora`. Controleer de genesis-hash hieronder. Native adressen gebruiken witness-v0-P2WPKH en HASH160 van een gecomprimeerde secp256k1-publieke sleutel. Memo of tag is niet verplicht. Verwerp adressen van een verkeerd netwerk en ongeldige controlesommen. Noteer HD-ontvangst-/wisselgeldtak en index; neem geen Bitcoin-afleidingspad aan.

## Transacties en blokken opzoeken

`getrawtransaction` doorzoekt actieve keten en mempool, geen uitsluitend verweesde transacties. Inputs verwijzen naar eerdere outputs, niet één afzenderadres. `getblock` gebruikt booleaanse `verbose`; opgeslagen inactieve blokken hebben `active=false`, `confirmations=-1`. Hun ruwe transacties blijven via blokhash beschikbaar. `findspendingtransaction` zoekt alleen bevestigde actieve bestedingen; null bewijst geen beschikbaarheid. Controleer `gettxout` met `include_mempool=true`. Bevestigingen en actieve status kunnen veranderen na reorganisatie.

[API_CONTRACT.json](../../../API_CONTRACT.json)
