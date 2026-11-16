# SUMUWW Android 0.6.103 · Versionsnoter

Med ét input på 1 SMW afhænger gebyret af, om du skal have penge tilbage. Hvis input og output er af typen P2WPKH, koster det ved en sats på 1 yugeon/vB præcis 110 yugeon at sende 0.99999890 SMW. Der er ingen byttepenge. Sender du 0.8 SMW fra samme input, tilføjes et output til byttepengene, og gebyret bliver 141 yugeon. Tegnebogen sender byttepengene tilbage, hvis beløbet efter gebyret når en minimumsgrænse, der tager højde for, hvad det koster at bruge byttepengene senere. Et mindre restbeløb indgår i det gebyr, der vises før godkendelsen. For et input fra en tegnebog med native SegWit (P2WPKH) regner estimatet med op til 71 byte til signaturen, inklusive hash-typen.


Efter en genstart fortsætter noden fra den sidste blok, den selv har verificeret, og kontrollerer nye blokke. Hvis den gemte verifikation mangler eller ikke stemmer, kontrollerer den den gemte historik igen.

SUMUWW Android 0.6.103 · Noden validerer, gemmer, videresender og stiller kædedata til rådighed.

API-specifikationen beskriver den indbyggede nodekerne. Android-appen har ingen skærm til RPC-konfiguration.

## RPC- og HTTP-API

validateaddress kontrollerer kontrolsum og valgt netværk. decoderawtransaction returnerer decoded_only, ikke bevis for gyldig signatur eller bekræftelse. OP_RETURN gemmer data til eksterne programmer. Noden tilføjer gebyrforespørgsler, kontrol før afsendelse, status for RBF-erstatning og data i blokrækkefølge. Erstatningen valideres, før ventende transaktioner fjernes. Flere signaturer og låste outputs er implementeret til isolerede aktiveringstests; de er endnu ikke aktive på det offentlige netværk.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Gebyrer, gennemgået transaktion og kompatibilitet

Gebyret er summen af inputs minus summen af outputs. Estimatet medregner kun et tilbagebetalingsoutput, når tegnebogen faktisk opretter en tilstrækkelig restbetaling. Et restbeløb under tegnebogens grænse lægges til gebyret; det endelige gebyr og det samlede træk vises til gennemgang. Satsen angives i yugeon/vB. Den virtuelle størrelse er transaktionens vægt divideret med fire og rundet op.

Tegnebogen vælger inputs og outputs én gang og signerer den samme transaktionsplan. Ved bekræftelse indsendes den gemte signerede transaktion uden at blive genopbygget eller få genberegnet gebyret. Et udløbet tilbud eller inputs, der allerede er brugt, kræver en ny gennemgang. Optagelse i den lokale kø er ikke en bekræftelse i en blok.

Ved almindelige P2WPKH-betalinger laver tegnebogen low-R- og low-S-signaturer på højst 71 byte inklusive SIGHASH_ALL-byten. Dette er en politik for signering og størrelsesestimering, ikke en ny konsensusgrænse for andre gyldige signaturer. Kortere signaturer kan mindske den faktiske virtuelle størrelse. De foreslåede satser bygger stadig på den lokale kø; en størrelsesberegning som i Bitcoin overtager ikke Bitcoin-netværkets gebyrsatser.

## Kompatibilitet for Android-signering

Tegnebogens filformat, adresser og eksisterende mønter er uændrede. Den eksisterende krypterede sikkerhedskopi kan gendannes i den nye app, så den samme tegnebog fortsat kan bruges. Android-noden 0.6.103 og tegnebogen 1.1.14 bruger en ny signeringsnøgle til udgivelsen. De kan ikke erstatte en installation signeret med en anden nøgle. Behold den gamle app og dens data, indtil du har en krypteret sikkerhedskopi af tegnebogen og en fungerende gendannelsesmetode. Afinstaller ikke den gamle app blot for at tvinge en opdatering igennem.

<!-- /payment-policy-20261116 -->
