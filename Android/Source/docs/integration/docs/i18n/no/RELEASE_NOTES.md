# SUMUWW Android 0.6.99 · Versjonsmerknader

Etter omstart fortsetter noden fra den siste blokken den selv har verifisert, og sjekker nye blokker. Hvis den lagrede verifikasjonen mangler eller ikke stemmer, sjekker noden den lagrede historikken på nytt.

SUMUWW Android 0.6.99 · Noden validerer, lagrer, videresender og gjør kjededata tilgjengelige.

API-spesifikasjonen beskriver den innebygde nodekjernen. Android-appen har ingen skjerm for RPC-oppsett.

## RPC- og HTTP-API

validateaddress kontrollerer kontrollsum og valgt nettverk. decoderawtransaction gir decoded_only, ikke bevis på gyldig signatur eller bekreftelse. OP_RETURN lagrer data for eksterne programmer. Noden legger til gebyrspørringer, kontroll før sending, status for RBF-erstatning og data i blokkrekkefølge. Erstatningen valideres før ventende transaksjoner fjernes. Flere signaturer og låste utdata er implementert for isolerte aktiveringstester; de er ennå ikke aktive på det offentlige nettverket.

[API_CONTRACT.json](../../../API_CONTRACT.json)
