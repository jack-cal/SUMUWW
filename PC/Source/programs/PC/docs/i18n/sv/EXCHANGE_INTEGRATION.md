# SUMUWW · Nodgränssnitt

SUMUWW PC 0.57.51 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

## Nätverk och adresser

Det publika nätverket heter `sumuww`, internt även `dora`. Kontrollera genesis-hashen nedan. Adresser använder witness v0 P2WPKH och HASH160 av en komprimerad secp256k1-nyckel. Memo eller tagg krävs inte. Avvisa fel nätverk och ogiltiga kontrollsummor. Anteckna HD-gren för mottagning/växel och index; anta inte Bitcoins härledningsväg.

## Signeringsformat

Det valfria källkods-SDK:t sammanställer transaktioner och verifierar tillhandahållna signaturer utan nycklar eller nätverk. Det är inget signeringsprogram eller nodkommando. P2WPKH-begränsningen gäller exempelformatet, inte noden. Den personliga plånboken finns kvar.

## RPC- och HTTP-API

validateaddress kontrollerar kontrollsumman och det valda nätverket. decoderawtransaction ger decoded_only, inget bevis på giltig signatur eller bekräftelse. OP_RETURN bevarar data för externa program. Noden lägger till avgiftsfrågor, kontroll före sändning, status för RBF-ersättning och data i blockordning. Ersättningen valideras innan väntande transaktioner tas bort. Flera signaturer och låsta utdata är implementerade för isolerade aktiveringstester; de är ännu inte aktiva i det offentliga nätverket.

## Autentisering och gränser

Aktivera RPC uttryckligen på numerisk loopback `127.0.0.1:18443` med privat Bearer-token. Ingen fjärrsignering eller upplåsning av plånbok exponeras. Använd lokal tjänst eller autentiserad tunnel; webbläsarens Origin/Referer nekas. JSON-RPC använder POST `/rpc`, objekt/array `params` och `id`; notifieringar ger HTTP 204. Gränser: kropp 8004096 byte, huvuden 8192, batch 16, samtidiga anrop 16, tidsgräns 10 sekunder; limit 1–1000, offset 0–1000000. Det finns 28 metoder och 11 REST-rutter.

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

## Verifiering

Installera beroendena och kör python examples/node_contract.py från källkoden. Offentliga testnycklar och tillfälligt regtest prövar insändning, avvisning, bekräftelser, omorganisation och lagring. Inga riktiga medel, användarprofiler eller hårdvarusignerare används.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Dokumentation](README.html) · [RPC- och HTTP-API](RPC_API.html) · [Noddrift](NETWORK_RUNBOOK.html) · [Versionsinformation](RELEASE_NOTES.html) · [Verifiering](EXCHANGE_EXAMPLES.html)

[Utförlig engelsk referens](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Avgifter, granskad transaktion och kompatibilitet

Avgiften är summan av ingångarna minus summan av utgångarna. Uppskattningen räknar bara med en växelutgång när plånboken faktiskt skapar tillräcklig växel. Ett restbelopp under plånbokens gräns läggs till avgiften; den slutliga avgiften och hela debiteringen visas för granskning. Avgiftssatsen anges i yugeon/vB. Virtuell storlek är transaktionens vikt delad med fyra, avrundad uppåt.

Plånboken väljer ingångar och utgångar en gång och signerar samma transaktionsplan. Vid bekräftelse skickas den sparade signerade transaktionen utan att byggas om eller få avgiften omräknad. Ett utgånget förslag eller redan förbrukade ingångar kräver en ny granskning. Att tas emot i den lokala kön betyder inte att transaktionen är bekräftad i ett block.

För vanliga P2WPKH-betalningar skapar plånboken low-R- och low-S-signaturer på högst 71 byte, inklusive SIGHASH_ALL-byten. Det är en policy för signering och storleksuppskattning, inte en ny konsensusgräns för andra giltiga signaturer. En kortare signatur kan minska den verkliga virtuella storleken. Föreslagna satser grundas fortfarande på den lokala kön; en storleksberäkning som liknar Bitcoins innebär inte att Bitcoin-nätverkets avgiftssatser används.

## Windows I2P-komponent och säkerhetskontroll

Windows-paketen innehåller officiella i2pd 3.0.0 med uppdaterade kontrollsummor och certifikat för första anslutningen. I den dokumenterade kontrollen upptäcker Defender fortfarande den officiella I2P-programfilen och den ursprungliga ZIP-filen som hot. En matchande officiell hash bevisar varken säkerhet eller en falsk varning. Ett lokalt filundantag gäller bara på datorn där det har lagts till; det offentliga paketet lägger inte till det. Andra datorer kan blockera samma filer.

<!-- /payment-policy-20261116 -->
