# Gebyrer, gennemgået transaktion og kompatibilitet

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Gebyrer, gennemgået transaktion og kompatibilitet

Gebyret er summen af inputs minus summen af outputs. Estimatet medregner kun et tilbagebetalingsoutput, når tegnebogen faktisk opretter en tilstrækkelig restbetaling. Et restbeløb under tegnebogens grænse lægges til gebyret; det endelige gebyr og det samlede træk vises til gennemgang. Satsen angives i yugeon/vB. Den virtuelle størrelse er transaktionens vægt divideret med fire og rundet op.

Tegnebogen vælger inputs og outputs én gang og signerer den samme transaktionsplan. Ved bekræftelse indsendes den gemte signerede transaktion uden at blive genopbygget eller få genberegnet gebyret. Et udløbet tilbud eller inputs, der allerede er brugt, kræver en ny gennemgang. Optagelse i den lokale kø er ikke en bekræftelse i en blok.

Ved almindelige P2WPKH-betalinger laver tegnebogen low-R- og low-S-signaturer på højst 71 byte inklusive SIGHASH_ALL-byten. Dette er en politik for signering og størrelsesestimering, ikke en ny konsensusgrænse for andre gyldige signaturer. Kortere signaturer kan mindske den faktiske virtuelle størrelse. 

## Kompatibilitet for Android-signering

Tegnebogens filformat, adresser og eksisterende mønter er uændrede. Den eksisterende krypterede sikkerhedskopi kan gendannes i den nye app, så den samme tegnebog fortsat kan bruges. Android-noden 0.6.103 og tegnebogen 1.1.14 bruger en ny signeringsnøgle til udgivelsen. De kan ikke erstatte en installation signeret med en anden nøgle. Behold den gamle app og dens data, indtil du har en krypteret sikkerhedskopi af tegnebogen og en fungerende gendannelsesmetode. Afinstaller ikke den gamle app blot for at tvinge en opdatering igennem.

<!-- /payment-policy-20261116 -->

Når noden har modtaget et gyldigt versionssvar, får modparten tid til at sende sin bekræftelse. Hvis to udgående forbindelser fører til samme node, holdes en tilgængelig vej åben, indtil synkroniseringen er fuldført via en af dem. 
