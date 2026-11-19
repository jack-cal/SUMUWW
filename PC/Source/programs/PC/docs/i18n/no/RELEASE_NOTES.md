# SUMUWW · Versjonsmerknader

Med én inngang på 1 SMW avhenger gebyret av om du skal ha veksel tilbake. Hvis inngangen og alle utgangene er av typen P2WPKH og satsen er 1 yugeon/vB, koster det 110 yugeon å sende 0.99999890 SMW, og det blir ingen veksel. Sender du 0.8 SMW fra samme inngang, kommer det en ekstra utgang for vekselen, og gebyret blir 141 yugeon. Lommeboken gir veksel tilbake hvis beløpet som gjenstår etter gebyret, når en nedre grense som tar hensyn til hva det koster å bruke vekselen senere. Et mindre restbeløp inngår i gebyret som vises før du bekrefter. For en lommebokinngang med native SegWit (P2WPKH) regner estimatet med opptil 71 byte til signaturen, inkludert hashtypen.

0.57.61 · Når du bytter språk mens appen kjører, endres også ikonet på oppgavelinjen i Windows.

Noden åpner vanligvis 10 utgående forbindelser. De fleste videresender blokker og transaksjoner. En kontrollert reserveforbindelse kan videresende blokker, og noden kan åpne en ellevte forbindelse en kort stund for å finne andre noder. Grensen er 125 forbindelser totalt. Det er plass til opptil 117 innkommende forbindelser, eller 115 når 10 er utgående. Skrivebordsappen viser nå bare det totale antallet tilkoblede noder. Hver utvinner bygger sine egne blokker. PC-noden videresender ferdige blokker og avviser forespørsler om utvinningsoppgaver og løsninger fra telefoner.

Etter omstart fortsetter noden fra den siste blokken den selv har verifisert, og sjekker nye blokker. Hvis den lagrede verifikasjonen mangler eller ikke stemmer, sjekker noden den lagrede historikken på nytt.

SUMUWW PC 0.57.61 · Noden validerer, lagrer, videresender og gjør kjededata tilgjengelige.

## Signaturformat

Det valgfrie kildekode-SDK-et setter sammen transaksjoner og kontrollerer oppgitte signaturer uten nøkler eller nettverk. Det er verken signeringsprogram eller nodekommando. P2WPKH-begrensningen gjelder eksempelformatet, ikke noden. Den personlige lommeboken er fortsatt tilgjengelig.

## RPC- og HTTP-API

validateaddress kontrollerer kontrollsum og valgt nettverk. decoderawtransaction gir decoded_only, ikke bevis på gyldig signatur eller bekreftelse. OP_RETURN lagrer data for eksterne programmer. Noden legger til gebyrspørringer, kontroll før sending, status for RBF-erstatning og data i blokkrekkefølge. Erstatningen valideres før ventende transaksjoner fjernes. Flere signaturer og låste utdata er implementert for isolerte aktiveringstester; de er ennå ikke aktive på det offentlige nettverket.

## Verifisering

Installer avhengighetene og kjør python examples/node_contract.py fra kildekoden. Offentlige testnøkler og midlertidig regtest tester innsending, avvisning, bekreftelser, omorganisering og datalagring. Ekte midler, brukerprofiler eller maskinvare for signering brukes ikke.

[Dokumentasjon](README.html) · [Nodegrensesnitt](EXCHANGE_INTEGRATION.html) · [RPC- og HTTP-API](RPC_API.html) · [Nodedrift](NETWORK_RUNBOOK.html) · [Verifisering](EXCHANGE_EXAMPLES.html)

[Utfyllende engelsk referanse](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Gebyrer, kontrollert transaksjon og kompatibilitet

Gebyret er summen av inngangene minus summen av utgangene. Anslaget tar bare med en vekselutgang når lommeboken faktisk oppretter tilstrekkelig veksel. Et restbeløp under lommebokens grense legges til gebyret; det endelige gebyret og samlet belastning vises til kontroll. Satsen oppgis i yugeon/vB. Virtuell størrelse er transaksjonsvekten delt på fire, avrundet oppover.

Lommeboken velger innganger og utganger én gang og signerer den samme transaksjonsplanen. Ved bekreftelse sendes den lagrede, signerte transaksjonen uten å bygges opp på nytt eller få gebyret beregnet om. Et utløpt tilbud eller innganger som allerede er brukt, krever en ny gjennomgang. At transaksjonen er akseptert i den lokale køen, betyr ikke at den er bekreftet i en blokk.

For vanlige P2WPKH-betalinger lager lommeboken low-R- og low-S-signaturer på høyst 71 byte, inkludert SIGHASH_ALL-byten. Dette er en regel for signering og størrelsesanslag, ikke en ny konsensusgrense for andre gyldige signaturer. Kortere signaturer kan gi mindre faktisk virtuell størrelse. 

<!-- /payment-policy-20261116 -->
