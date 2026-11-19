# SUMUWW Android 0.6.103 · Versjonsmerknader

Med én inngang på 1 SMW avhenger gebyret av om du skal ha veksel tilbake. Hvis inngangen og alle utgangene er av typen P2WPKH og satsen er 1 yugeon/vB, koster det 110 yugeon å sende 0.99999890 SMW, og det blir ingen veksel. Sender du 0.8 SMW fra samme inngang, kommer det en ekstra utgang for vekselen, og gebyret blir 141 yugeon. Lommeboken gir veksel tilbake hvis beløpet som gjenstår etter gebyret, når en nedre grense som tar hensyn til hva det koster å bruke vekselen senere. Et mindre restbeløp inngår i gebyret som vises før du bekrefter. For en lommebokinngang med native SegWit (P2WPKH) regner estimatet med opptil 71 byte til signaturen, inkludert hashtypen.

Etter omstart fortsetter noden fra den siste blokken den selv har verifisert, og sjekker nye blokker. Hvis den lagrede verifikasjonen mangler eller ikke stemmer, sjekker noden den lagrede historikken på nytt.

SUMUWW Android 0.6.103 · Noden validerer, lagrer, videresender og gjør kjededata tilgjengelige.

API-spesifikasjonen beskriver den innebygde nodekjernen. Android-appen har ingen skjerm for RPC-oppsett.

## RPC- og HTTP-API

validateaddress kontrollerer kontrollsum og valgt nettverk. decoderawtransaction gir decoded_only, ikke bevis på gyldig signatur eller bekreftelse. OP_RETURN lagrer data for eksterne programmer. Noden legger til gebyrspørringer, kontroll før sending, status for RBF-erstatning og data i blokkrekkefølge. Erstatningen valideres før ventende transaksjoner fjernes. Flere signaturer og låste utdata er implementert for isolerte aktiveringstester; de er ennå ikke aktive på det offentlige nettverket.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Gebyrer, kontrollert transaksjon og kompatibilitet

Gebyret er summen av inngangene minus summen av utgangene. Anslaget tar bare med en vekselutgang når lommeboken faktisk oppretter tilstrekkelig veksel. Et restbeløp under lommebokens grense legges til gebyret; det endelige gebyret og samlet belastning vises til kontroll. Satsen oppgis i yugeon/vB. Virtuell størrelse er transaksjonsvekten delt på fire, avrundet oppover.

Lommeboken velger innganger og utganger én gang og signerer den samme transaksjonsplanen. Ved bekreftelse sendes den lagrede, signerte transaksjonen uten å bygges opp på nytt eller få gebyret beregnet om. Et utløpt tilbud eller innganger som allerede er brukt, krever en ny gjennomgang. At transaksjonen er akseptert i den lokale køen, betyr ikke at den er bekreftet i en blokk.

For vanlige P2WPKH-betalinger lager lommeboken low-R- og low-S-signaturer på høyst 71 byte, inkludert SIGHASH_ALL-byten. Dette er en regel for signering og størrelsesanslag, ikke en ny konsensusgrense for andre gyldige signaturer. Kortere signaturer kan gi mindre faktisk virtuell størrelse. 

## Kompatibilitet for Android-signering

Lommebokens filformat, adresser og eksisterende mynter er uendret. Den eksisterende krypterte sikkerhetskopien kan gjenopprettes i den nye appen, slik at samme lommebok fortsatt kan brukes. Android-noden 0.6.103 og lommeboken 1.1.14 bruker en ny signeringsnøkkel for utgivelsen. De kan ikke erstatte en installasjon signert med en annen nøkkel. Behold den gamle appen og dataene til du har en kryptert sikkerhetskopi av lommeboken og en fungerende gjenopprettingsmetode. Ikke avinstaller den gamle appen bare for å tvinge gjennom en oppdatering.

<!-- /payment-policy-20261116 -->
