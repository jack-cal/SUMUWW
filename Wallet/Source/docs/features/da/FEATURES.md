# SUMUWW Wallet Android 1.1.14

Noden åbner normalt 10 udgående forbindelser. De fleste videresender blokke og transaktioner. En afprøvet reserveforbindelse kan videresende blokke, og noden kan kortvarigt åbne en 11. forbindelse for at finde andre noder. Grænsen er 125 i alt. Der er plads til op til 117 indgående forbindelser, eller 115 ved 10 udgående. En fejl ved opstart af Android-tegnebogen er rettet. Tegnebogen registrerer ændringer i telefonens netværksforbindelse.

1 SMW = 100.000.000 yugeon. Automatiske gebyrer tilbyder tre niveauer ud fra lokale observationer uden at garantere bekræftelsestiden. Du kan indtaste en sats i yugeon/vB. Kontrollér det endelige gebyr og totalen i SMW før afsendelse. En afvist transaktion reducerer ikke saldoen.

Med ét input på 1 SMW afhænger gebyret af, om du skal have penge tilbage. Hvis input og output er af typen P2WPKH, koster det ved en sats på 1 yugeon/vB præcis 110 yugeon at sende 0.99999890 SMW. Der er ingen byttepenge. Sender du 0.8 SMW fra samme input, tilføjes et output til byttepengene, og gebyret bliver 141 yugeon. Tegnebogen sender byttepengene tilbage, hvis beløbet efter gebyret når en minimumsgrænse, der tager højde for, hvad det koster at bruge byttepengene senere. Et mindre restbeløb indgår i det gebyr, der vises før godkendelsen. For et input fra en tegnebog med native SegWit (P2WPKH) regner estimatet med op til 71 byte til signaturen, inklusive hash-typen.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Automatiske gebyrer følger den ventende datamængde, blokkapaciteten og transaktionernes prioritet. Gebyrer fra tidligere blokke bruges ikke. Ved kort kø gælder minimumssatsen. Forhåndsvisningen opdateres; den endelige bekræftelse fastlægger gebyret. Oplysningerne dækker den tilsluttede lokale node, ikke alle noder.

Udskiftninger registreret af denne node bevares i historikken efter genstart af tegnebogen. Fjernede transaktioner påvirker ikke saldoen.

Minehistorikken viser ny udstedelse, gebyrer og samlet belønning for hver blok hver for sig. Det beløb, din wallet modtager, vises separat. Ved delvis udbetaling antages ingen fordeling mellem de to dele. Noden tilbyder 28 RPC-metoder, herunder gebyrestimering, og kontrollerer og videresender signerede transaktioner.

<!-- payment-policy-20261116 -->

## Gebyrer, gennemgået transaktion og kompatibilitet

Gebyret er summen af inputs minus summen af outputs. Estimatet medregner kun et tilbagebetalingsoutput, når tegnebogen faktisk opretter en tilstrækkelig restbetaling. Et restbeløb under tegnebogens grænse lægges til gebyret; det endelige gebyr og det samlede træk vises til gennemgang. Satsen angives i yugeon/vB. Den virtuelle størrelse er transaktionens vægt divideret med fire og rundet op.

Tegnebogen vælger inputs og outputs én gang og signerer den samme transaktionsplan. Ved bekræftelse indsendes den gemte signerede transaktion uden at blive genopbygget eller få genberegnet gebyret. Et udløbet tilbud eller inputs, der allerede er brugt, kræver en ny gennemgang. Optagelse i den lokale kø er ikke en bekræftelse i en blok.

Ved almindelige P2WPKH-betalinger laver tegnebogen low-R- og low-S-signaturer på højst 71 byte inklusive SIGHASH_ALL-byten. Dette er en politik for signering og størrelsesestimering, ikke en ny konsensusgrænse for andre gyldige signaturer. Kortere signaturer kan mindske den faktiske virtuelle størrelse. 

## Kompatibilitet for Android-signering

Tegnebogens filformat, adresser og eksisterende mønter er uændrede. Den eksisterende krypterede sikkerhedskopi kan gendannes i den nye app, så den samme tegnebog fortsat kan bruges. Android-noden 0.6.103 og tegnebogen 1.1.14 bruger en ny signeringsnøgle til udgivelsen. De kan ikke erstatte en installation signeret med en anden nøgle. Behold den gamle app og dens data, indtil du har en krypteret sikkerhedskopi af tegnebogen og en fungerende gendannelsesmetode. Afinstaller ikke den gamle app blot for at tvinge en opdatering igennem.

<!-- /payment-policy-20261116 -->

Når noden har modtaget et gyldigt versionssvar, får modparten tid til at sende sin bekræftelse. Hvis to udgående forbindelser fører til samme node, holdes en tilgængelig vej åben, indtil synkroniseringen er fuldført via en af dem. 
