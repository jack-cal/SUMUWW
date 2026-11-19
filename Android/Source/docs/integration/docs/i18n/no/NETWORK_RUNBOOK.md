# SUMUWW Android 0.6.103 · Nodedrift

Etter omstart fortsetter noden fra den siste blokken den selv har verifisert, og sjekker nye blokker. Hvis den lagrede verifikasjonen mangler eller ikke stemmer, sjekker noden den lagrede historikken på nytt.

SUMUWW Android 0.6.103 · Noden validerer, lagrer, videresender og gjør kjededata tilgjengelige.

## Nettverk og adresser

Det offentlige nettverket er `sumuww`, med internt alias `dora`. Kontroller genesis-hashen nedenfor. Native adresser bruker witness v0 P2WPKH og HASH160 av komprimert offentlig secp256k1-nøkkel. Memo eller tagg kreves ikke. Avvis feil nettverk og ugyldige kontrollsummer. Registrer HD-gren for mottak/vekslepenger og indeks; ikke anta Bitcoins avledningsbane.

## Søk etter transaksjoner og blokker

`getrawtransaction` søker aktiv kjede og mempool, ikke transaksjoner bare i foreldreløse grener. Innganger viser tidligere utganger, ikke én avsenderadresse. `getblock` bruker boolsk `verbose`; lagrede inaktive blokker har `active=false`, `confirmations=-1`. Råtransaksjoner er fortsatt tilgjengelige via blokkhash. `findspendingtransaction` søker bare bekreftede aktive forbruk; null beviser ikke tilgjengelighet. Sjekk `gettxout` med `include_mempool=true`. Bekreftelser og aktiv status kan endres ved omorganisering.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Gebyrer, kontrollert transaksjon og kompatibilitet

Gebyret er summen av inngangene minus summen av utgangene. Anslaget tar bare med en vekselutgang når lommeboken faktisk oppretter tilstrekkelig veksel. Et restbeløp under lommebokens grense legges til gebyret; det endelige gebyret og samlet belastning vises til kontroll. Satsen oppgis i yugeon/vB. Virtuell størrelse er transaksjonsvekten delt på fire, avrundet oppover.

Lommeboken velger innganger og utganger én gang og signerer den samme transaksjonsplanen. Ved bekreftelse sendes den lagrede, signerte transaksjonen uten å bygges opp på nytt eller få gebyret beregnet om. Et utløpt tilbud eller innganger som allerede er brukt, krever en ny gjennomgang. At transaksjonen er akseptert i den lokale køen, betyr ikke at den er bekreftet i en blokk.

For vanlige P2WPKH-betalinger lager lommeboken low-R- og low-S-signaturer på høyst 71 byte, inkludert SIGHASH_ALL-byten. Dette er en regel for signering og størrelsesanslag, ikke en ny konsensusgrense for andre gyldige signaturer. Kortere signaturer kan gi mindre faktisk virtuell størrelse. 

## Kompatibilitet for Android-signering

Lommebokens filformat, adresser og eksisterende mynter er uendret. Den eksisterende krypterte sikkerhetskopien kan gjenopprettes i den nye appen, slik at samme lommebok fortsatt kan brukes. Android-noden 0.6.103 og lommeboken 1.1.14 bruker en ny signeringsnøkkel for utgivelsen. De kan ikke erstatte en installasjon signert med en annen nøkkel. Behold den gamle appen og dataene til du har en kryptert sikkerhetskopi av lommeboken og en fungerende gjenopprettingsmetode. Ikke avinstaller den gamle appen bare for å tvinge gjennom en oppdatering.

<!-- /payment-policy-20261116 -->

Når noden har mottatt et gyldig versjonssvar, får motparten tid til å sende en bekreftelse. Hvis to utgående forbindelser går til samme node, holdes en tilgjengelig rute åpen til synkroniseringen er ferdig over en av dem. 
