# SUMUWW · Versjonsmerknader

Noden åpner vanligvis 10 utgående forbindelser. De fleste videresender blokker og transaksjoner. En kontrollert reserveforbindelse kan videresende blokker, og noden kan åpne en ellevte forbindelse en kort stund for å finne andre noder. Grensen er 125 forbindelser totalt. Det er plass til opptil 117 innkommende forbindelser, eller 115 når 10 er utgående. Skrivebordsappen viser nå bare det totale antallet tilkoblede noder. Hver utvinner bygger sine egne blokker. PC-noden videresender ferdige blokker og avviser forespørsler om utvinningsoppgaver og løsninger fra telefoner.

Etter omstart fortsetter noden fra den siste blokken den selv har verifisert, og sjekker nye blokker. Hvis den lagrede verifikasjonen mangler eller ikke stemmer, sjekker noden den lagrede historikken på nytt.


SUMUWW PC 0.57.54 · Noden validerer, lagrer, videresender og gjør kjededata tilgjengelige.

## Signaturformat

Det valgfrie kildekode-SDK-et setter sammen transaksjoner og kontrollerer oppgitte signaturer uten nøkler eller nettverk. Det er verken signeringsprogram eller nodekommando. P2WPKH-begrensningen gjelder eksempelformatet, ikke noden. Den personlige lommeboken er fortsatt tilgjengelig.

## RPC- og HTTP-API

validateaddress kontrollerer kontrollsum og valgt nettverk. decoderawtransaction gir decoded_only, ikke bevis på gyldig signatur eller bekreftelse. OP_RETURN lagrer data for eksterne programmer. Noden legger til gebyrspørringer, kontroll før sending, status for RBF-erstatning og data i blokkrekkefølge. Erstatningen valideres før ventende transaksjoner fjernes. Flere signaturer og låste utdata er implementert for isolerte aktiveringstester; de er ennå ikke aktive på det offentlige nettverket.

## Verifisering

Installer avhengighetene og kjør python examples/node_contract.py fra kildekoden. Offentlige testnøkler og midlertidig regtest tester innsending, avvisning, bekreftelser, omorganisering og datalagring. Ekte midler, brukerprofiler eller maskinvare for signering brukes ikke.

[Dokumentasjon](README.html) · [Nodegrensesnitt](EXCHANGE_INTEGRATION.html) · [RPC- og HTTP-API](RPC_API.html) · [Nodedrift](NETWORK_RUNBOOK.html) · [Verifisering](EXCHANGE_EXAMPLES.html)

[Utfyllende engelsk referanse](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)
