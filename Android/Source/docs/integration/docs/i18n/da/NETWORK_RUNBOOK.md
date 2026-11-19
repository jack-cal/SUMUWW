# SUMUWW Android 0.6.103 · Nodedrift

Efter en genstart fortsætter noden fra den sidste blok, den selv har verificeret, og kontrollerer nye blokke. Hvis den gemte verifikation mangler eller ikke stemmer, kontrollerer den den gemte historik igen.

SUMUWW Android 0.6.103 · Noden validerer, gemmer, videresender og stiller kædedata til rådighed.

## Netværk og adresser

Det offentlige netværk er `sumuww`, internt også `dora`. Kontrollér genesis-hashen nedenfor. Adresser bruger witness v0 P2WPKH og HASH160 af en komprimeret offentlig secp256k1-nøgle. Memo eller tag er ikke påkrævet. Afvis forkert netværk og ugyldige kontrolsummer. Notér HD-gren til modtagelse/byttepenge og indeks; antag ikke Bitcoins afledningssti.

## Find transaktioner og blokke

`getrawtransaction` søger aktiv kæde og mempool, ikke transaktioner udelukkende i forældreløse grene. Inputs angiver tidligere outputs, ikke én afsenderadresse. `getblock` kræver boolesk `verbose`; gemte inaktive blokke har `active=false`, `confirmations=-1`. Råtransaktioner er stadig tilgængelige via blokhash. `findspendingtransaction` søger kun bekræftede aktive forbrug; null beviser ikke tilgængelighed. Kontrollér `gettxout` med `include_mempool=true`. Bekræftelser og aktiv status kan ændres ved reorganisering.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Gebyrer, gennemgået transaktion og kompatibilitet

Gebyret er summen af inputs minus summen af outputs. Estimatet medregner kun et tilbagebetalingsoutput, når tegnebogen faktisk opretter en tilstrækkelig restbetaling. Et restbeløb under tegnebogens grænse lægges til gebyret; det endelige gebyr og det samlede træk vises til gennemgang. Satsen angives i yugeon/vB. Den virtuelle størrelse er transaktionens vægt divideret med fire og rundet op.

Tegnebogen vælger inputs og outputs én gang og signerer den samme transaktionsplan. Ved bekræftelse indsendes den gemte signerede transaktion uden at blive genopbygget eller få genberegnet gebyret. Et udløbet tilbud eller inputs, der allerede er brugt, kræver en ny gennemgang. Optagelse i den lokale kø er ikke en bekræftelse i en blok.

Ved almindelige P2WPKH-betalinger laver tegnebogen low-R- og low-S-signaturer på højst 71 byte inklusive SIGHASH_ALL-byten. Dette er en politik for signering og størrelsesestimering, ikke en ny konsensusgrænse for andre gyldige signaturer. Kortere signaturer kan mindske den faktiske virtuelle størrelse. 

## Kompatibilitet for Android-signering

Tegnebogens filformat, adresser og eksisterende mønter er uændrede. Den eksisterende krypterede sikkerhedskopi kan gendannes i den nye app, så den samme tegnebog fortsat kan bruges. Android-noden 0.6.103 og tegnebogen 1.1.14 bruger en ny signeringsnøgle til udgivelsen. De kan ikke erstatte en installation signeret med en anden nøgle. Behold den gamle app og dens data, indtil du har en krypteret sikkerhedskopi af tegnebogen og en fungerende gendannelsesmetode. Afinstaller ikke den gamle app blot for at tvinge en opdatering igennem.

<!-- /payment-policy-20261116 -->

Når noden har modtaget et gyldigt versionssvar, får modparten tid til at sende sin bekræftelse. Hvis to udgående forbindelser fører til samme node, holdes en tilgængelig vej åben, indtil synkroniseringen er fuldført via en af dem. 
