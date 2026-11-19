# SUMUWW Android 0.6.103 · Nodgränssnitt

SUMUWW Android 0.6.103 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

API-specifikationen beskriver den inbyggda nodkärnan. Android-appen saknar skärm för RPC-inställningar.

## Nätverk och adresser

Det publika nätverket heter `sumuww`, internt även `dora`. Kontrollera genesis-hashen nedan. Adresser använder witness v0 P2WPKH och HASH160 av en komprimerad secp256k1-nyckel. Memo eller tagg krävs inte. Avvisa fel nätverk och ogiltiga kontrollsummor. Anteckna HD-gren för mottagning/växel och index; anta inte Bitcoins härledningsväg.

## RPC- och HTTP-API

validateaddress kontrollerar kontrollsumman och det valda nätverket. decoderawtransaction ger decoded_only, inget bevis på giltig signatur eller bekräftelse. OP_RETURN bevarar data för externa program. Noden lägger till avgiftsfrågor, kontroll före sändning, status för RBF-ersättning och data i blockordning. Ersättningen valideras innan väntande transaktioner tas bort. Flera signaturer och låsta utdata är implementerade för isolerade aktiveringstester; de är ännu inte aktiva i det offentliga nätverket.

## Belopp och tillgängliga utgångar

`_units` är heltal i minsta enhet; `_smw` strängar med 8 decimaler; `_dora` kompatibilitetsalias. Inget beloppsfält `_sumuww` finns. 1 SMW = 100000000 enheter. `gettxout` saknar `spendable` och kan ge omogna coinbase-utgångar. Minst 100 bekräftelser behövs för användning i nästa block. Filtrera `listunspent` på `spendable`; available i `getaddressbalance` utesluter omogna medel och väntande utgifter. Nya mempool-utgångar är inte bekräftade. Kontrollera spetsen mellan sidor och validera valda ingångar igen.

1 SMW = 100 000 000 yugeon. Automatiska avgifter erbjuder tre nivåer utifrån lokala observationer, utan att garantera bekräftelsetiden. Du kan ange en sats i yugeon/vB. Kontrollera den slutliga avgiften och totalsumman i SMW innan du skickar. En avvisad transaktion minskar inte saldot.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Automatiska avgifter utgår från väntande datamängd, blockkapacitet och transaktionsprioritet. Avgifter i tidigare block används inte. Vid kort kö gäller minimiavgiften. Förhandsvisningen uppdateras; den slutliga bekräftelsen låser avgiften. Uppgifterna gäller den anslutna lokala noden, inte alla noder.

Ersättningar som denna nod har registrerat finns kvar i historiken efter omstart av plånboken. Borttagna transaktioner påverkar inte saldot.

Utvinningshistoriken visar ny utgivning, avgifter och total belöning för varje block var för sig. Beloppet din plånbok tar emot visas separat. Vid delvis uttag antas ingen fördelning mellan delarna. Noden erbjuder 28 RPC-metoder, inklusive avgiftsuppskattning, och kontrollerar och vidarebefordrar signerade transaktioner.

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
