# SUMUWW Android 0.6.103 · Noddrift

Efter en omstart fortsätter noden från det senaste block som den själv har verifierat och kontrollerar nya block. Om den sparade verifieringsposten saknas eller inte stämmer kontrollerar noden den sparade historiken igen.

SUMUWW Android 0.6.103 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

## Nätverk och adresser

Det publika nätverket heter `sumuww`, internt även `dora`. Kontrollera genesis-hashen nedan. Adresser använder witness v0 P2WPKH och HASH160 av en komprimerad secp256k1-nyckel. Memo eller tagg krävs inte. Avvisa fel nätverk och ogiltiga kontrollsummor. Anteckna HD-gren för mottagning/växel och index; anta inte Bitcoins härledningsväg.

## Sök transaktioner och block

`getrawtransaction` söker aktiv kedja och mempool, inte enbart övergivna transaktioner. Ingångar anger tidigare utgångar, inte en unik avsändare. `getblock` tar boolesk `verbose`; lagrade inaktiva block har `active=false`, `confirmations=-1`. Råtransaktioner kan fortsatt hämtas via blockhash. `findspendingtransaction` söker bara bekräftade aktiva utgifter; null bevisar inte tillgänglighet. Kontrollera `gettxout` med `include_mempool=true`. Bekräftelser och aktiv status kan ändras vid omorganisation.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Avgifter, granskad transaktion och kompatibilitet

Avgiften är summan av ingångarna minus summan av utgångarna. Uppskattningen räknar bara med en växelutgång när plånboken faktiskt skapar tillräcklig växel. Ett restbelopp under plånbokens gräns läggs till avgiften; den slutliga avgiften och hela debiteringen visas för granskning. Avgiftssatsen anges i yugeon/vB. Virtuell storlek är transaktionens vikt delad med fyra, avrundad uppåt.

Plånboken väljer ingångar och utgångar en gång och signerar samma transaktionsplan. Vid bekräftelse skickas den sparade signerade transaktionen utan att byggas om eller få avgiften omräknad. Ett utgånget förslag eller redan förbrukade ingångar kräver en ny granskning. Att tas emot i den lokala kön betyder inte att transaktionen är bekräftad i ett block.

För vanliga P2WPKH-betalningar skapar plånboken low-R- och low-S-signaturer på högst 71 byte, inklusive SIGHASH_ALL-byten. Det är en policy för signering och storleksuppskattning, inte en ny konsensusgräns för andra giltiga signaturer. En kortare signatur kan minska den verkliga virtuella storleken. 

## Kompatibilitet för Android-signaturer

Plånbokens filformat, adresser och befintliga mynt har inte ändrats. Den tidigare krypterade säkerhetskopian kan återställas i den nya appen för att fortsätta använda samma plånbok. Android-noden 0.6.103 och plånboken 1.1.14 använder en ny nyckel för utgivningssignering. De kan inte ersätta en installation som signerats med en annan nyckel. Behåll den gamla appen och dess data tills du har en krypterad säkerhetskopia av plånboken och en fungerande återställningsmetod. Avinstallera inte den gamla appen bara för att tvinga fram installationen av en uppdatering.

<!-- /payment-policy-20261116 -->

När noden har fått ett giltigt versionssvar får motparten tid att skicka en bekräftelse. Om två utgående anslutningar leder till samma nod hålls en tillgänglig väg öppen tills synkroniseringen är klar via en av dem. 
