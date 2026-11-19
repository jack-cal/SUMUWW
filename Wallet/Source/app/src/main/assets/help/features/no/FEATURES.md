# SUMUWW Wallet Android 1.1.14

Noden åpner vanligvis 10 utgående forbindelser. De fleste videresender blokker og transaksjoner. En kontrollert reserveforbindelse kan videresende blokker, og noden kan åpne en ellevte forbindelse en kort stund for å finne andre noder. Grensen er 125 forbindelser totalt. Det er plass til opptil 117 innkommende forbindelser, eller 115 når 10 er utgående. En feil ved oppstart av Android-lommeboken er rettet. Lommeboken oppdager endringer i telefonens nettverkstilkobling.

1 SMW = 100 000 000 yugeon. Automatiske gebyrer tilbyr tre nivåer basert på lokale observasjoner uten å garantere bekreftelsestiden. Du kan angi en sats i yugeon/vB. Kontroller endelig gebyr og totalsum i SMW før sending. En avvist transaksjon reduserer ikke saldoen.

Med én inngang på 1 SMW avhenger gebyret av om du skal ha veksel tilbake. Hvis inngangen og alle utgangene er av typen P2WPKH og satsen er 1 yugeon/vB, koster det 110 yugeon å sende 0.99999890 SMW, og det blir ingen veksel. Sender du 0.8 SMW fra samme inngang, kommer det en ekstra utgang for vekselen, og gebyret blir 141 yugeon. Lommeboken gir veksel tilbake hvis beløpet som gjenstår etter gebyret, når en nedre grense som tar hensyn til hva det koster å bruke vekselen senere. Et mindre restbeløp inngår i gebyret som vises før du bekrefter. For en lommebokinngang med native SegWit (P2WPKH) regner estimatet med opptil 71 byte til signaturen, inkludert hashtypen.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Automatiske gebyrer bygger på ventende datamengde, blokkapasitet og transaksjonsprioritet. Gebyrer fra tidligere blokker brukes ikke. Ved liten kø gjelder minstesatsen. Forhåndsvisningen oppdateres; den endelige bekreftelsen låser gebyret. Opplysningene gjelder den tilkoblede lokale noden, ikke alle noder.

Erstatninger som denne noden har registrert, beholdes i historikken etter omstart av lommeboken. Fjernede transaksjoner påvirker ikke saldoen.

Utvinninghistorikken viser ny utstedelse, gebyrer og samlet belønning for hver blokk hver for seg. Beløpet lommeboken din mottar vises separat. Ved delvis uttak antas ingen fordeling mellom de to delene. Noden tilbyr 28 RPC-metoder, inkludert gebyrestimering, og kontrollerer og videresender signerte transaksjoner.

<!-- payment-policy-20261116 -->

## Gebyrer, kontrollert transaksjon og kompatibilitet

Gebyret er summen av inngangene minus summen av utgangene. Anslaget tar bare med en vekselutgang når lommeboken faktisk oppretter tilstrekkelig veksel. Et restbeløp under lommebokens grense legges til gebyret; det endelige gebyret og samlet belastning vises til kontroll. Satsen oppgis i yugeon/vB. Virtuell størrelse er transaksjonsvekten delt på fire, avrundet oppover.

Lommeboken velger innganger og utganger én gang og signerer den samme transaksjonsplanen. Ved bekreftelse sendes den lagrede, signerte transaksjonen uten å bygges opp på nytt eller få gebyret beregnet om. Et utløpt tilbud eller innganger som allerede er brukt, krever en ny gjennomgang. At transaksjonen er akseptert i den lokale køen, betyr ikke at den er bekreftet i en blokk.

For vanlige P2WPKH-betalinger lager lommeboken low-R- og low-S-signaturer på høyst 71 byte, inkludert SIGHASH_ALL-byten. Dette er en regel for signering og størrelsesanslag, ikke en ny konsensusgrense for andre gyldige signaturer. Kortere signaturer kan gi mindre faktisk virtuell størrelse. 

## Kompatibilitet for Android-signering

Lommebokens filformat, adresser og eksisterende mynter er uendret. Den eksisterende krypterte sikkerhetskopien kan gjenopprettes i den nye appen, slik at samme lommebok fortsatt kan brukes. Android-noden 0.6.103 og lommeboken 1.1.14 bruker en ny signeringsnøkkel for utgivelsen. De kan ikke erstatte en installasjon signert med en annen nøkkel. Behold den gamle appen og dataene til du har en kryptert sikkerhetskopi av lommeboken og en fungerende gjenopprettingsmetode. Ikke avinstaller den gamle appen bare for å tvinge gjennom en oppdatering.

<!-- /payment-policy-20261116 -->

Når noden har mottatt et gyldig versjonssvar, får motparten tid til å sende en bekreftelse. Hvis to utgående forbindelser går til samme node, holdes en tilgjengelig rute åpen til synkroniseringen er ferdig over en av dem. 
