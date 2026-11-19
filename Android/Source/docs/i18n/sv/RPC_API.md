# SUMUWW Android 0.6.103 · RPC- och HTTP-API

SUMUWW Android 0.6.103 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

[Dokumentation](../../integration/docs/i18n/sv/RPC_API.html)

<!-- payment-policy-20261116 -->

## Avgifter, granskad transaktion och kompatibilitet

Avgiften är summan av ingångarna minus summan av utgångarna. Uppskattningen räknar bara med en växelutgång när plånboken faktiskt skapar tillräcklig växel. Ett restbelopp under plånbokens gräns läggs till avgiften; den slutliga avgiften och hela debiteringen visas för granskning. Avgiftssatsen anges i yugeon/vB. Virtuell storlek är transaktionens vikt delad med fyra, avrundad uppåt.

Plånboken väljer ingångar och utgångar en gång och signerar samma transaktionsplan. Vid bekräftelse skickas den sparade signerade transaktionen utan att byggas om eller få avgiften omräknad. Ett utgånget förslag eller redan förbrukade ingångar kräver en ny granskning. Att tas emot i den lokala kön betyder inte att transaktionen är bekräftad i ett block.

För vanliga P2WPKH-betalningar skapar plånboken low-R- och low-S-signaturer på högst 71 byte, inklusive SIGHASH_ALL-byten. Det är en policy för signering och storleksuppskattning, inte en ny konsensusgräns för andra giltiga signaturer. En kortare signatur kan minska den verkliga virtuella storleken. 

## Kompatibilitet för Android-signaturer

Plånbokens filformat, adresser och befintliga mynt har inte ändrats. Den tidigare krypterade säkerhetskopian kan återställas i den nya appen för att fortsätta använda samma plånbok. Android-noden 0.6.103 och plånboken 1.1.14 använder en ny nyckel för utgivningssignering. De kan inte ersätta en installation som signerats med en annan nyckel. Behåll den gamla appen och dess data tills du har en krypterad säkerhetskopia av plånboken och en fungerande återställningsmetod. Avinstallera inte den gamla appen bara för att tvinga fram installationen av en uppdatering.

<!-- /payment-policy-20261116 -->
