# SUMUWW · Noddrift

Noden öppnar normalt 10 utgående anslutningar. De flesta förmedlar block och transaktioner. En verifierad reservanslutning kan förmedla block, och noden kan tillfälligt öppna en elfte anslutning för att hitta andra noder. Totalt tillåts 125 anslutningar. Högst 117 kan vara inkommande, eller 115 vid 10 utgående. Datorappen visar nu bara det sammanlagda antalet anslutna noder. Varje gruvenhet bygger sina egna block. PC-noden vidarebefordrar färdiga block och avvisar telefonens begäran om gruvuppgifter och inskickade lösningar.

Efter en omstart fortsätter noden från det senaste block som den själv har verifierat och kontrollerar nya block. Om den sparade verifieringsposten saknas eller inte stämmer kontrollerar noden den sparade historiken igen.


SUMUWW PC 0.57.61 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

## Nätverk och adresser

Det publika nätverket heter `sumuww`, internt även `dora`. Kontrollera genesis-hashen nedan. Adresser använder witness v0 P2WPKH och HASH160 av en komprimerad secp256k1-nyckel. Memo eller tagg krävs inte. Avvisa fel nätverk och ogiltiga kontrollsummor. Anteckna HD-gren för mottagning/växel och index; anta inte Bitcoins härledningsväg.

## Autentisering och gränser

Aktivera RPC uttryckligen på numerisk loopback `127.0.0.1:18443` med privat Bearer-token. Ingen fjärrsignering eller upplåsning av plånbok exponeras. Använd lokal tjänst eller autentiserad tunnel; webbläsarens Origin/Referer nekas. JSON-RPC använder POST `/rpc`, objekt/array `params` och `id`; notifieringar ger HTTP 204. Gränser: kropp 8004096 byte, huvuden 8192, batch 16, samtidiga anrop 16, tidsgräns 10 sekunder; limit 1–1000, offset 0–1000000. Det finns 28 metoder och 11 REST-rutter.

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

[Dokumentation](README.html) · [Nodgränssnitt](EXCHANGE_INTEGRATION.html) · [RPC- och HTTP-API](RPC_API.html) · [Versionsinformation](RELEASE_NOTES.html) · [Verifiering](EXCHANGE_EXAMPLES.html)

[Utförlig engelsk referens](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Avgifter, granskad transaktion och kompatibilitet

Avgiften är summan av ingångarna minus summan av utgångarna. Uppskattningen räknar bara med en växelutgång när plånboken faktiskt skapar tillräcklig växel. Ett restbelopp under plånbokens gräns läggs till avgiften; den slutliga avgiften och hela debiteringen visas för granskning. Avgiftssatsen anges i yugeon/vB. Virtuell storlek är transaktionens vikt delad med fyra, avrundad uppåt.

Plånboken väljer ingångar och utgångar en gång och signerar samma transaktionsplan. Vid bekräftelse skickas den sparade signerade transaktionen utan att byggas om eller få avgiften omräknad. Ett utgånget förslag eller redan förbrukade ingångar kräver en ny granskning. Att tas emot i den lokala kön betyder inte att transaktionen är bekräftad i ett block.

För vanliga P2WPKH-betalningar skapar plånboken low-R- och low-S-signaturer på högst 71 byte, inklusive SIGHASH_ALL-byten. Det är en policy för signering och storleksuppskattning, inte en ny konsensusgräns för andra giltiga signaturer. En kortare signatur kan minska den verkliga virtuella storleken. Föreslagna satser grundas fortfarande på den lokala kön; en storleksberäkning som liknar Bitcoins innebär inte att Bitcoin-nätverkets avgiftssatser används.

## Windows I2P-komponent och säkerhetskontroll

Windows-paketen innehåller officiella i2pd 3.0.0 med uppdaterade kontrollsummor och certifikat för första anslutningen. I den dokumenterade kontrollen upptäcker Defender fortfarande den officiella I2P-programfilen och den ursprungliga ZIP-filen som hot. En matchande officiell hash bevisar varken säkerhet eller en falsk varning. Ett lokalt filundantag gäller bara på datorn där det har lagts till; det offentliga paketet lägger inte till det. Andra datorer kan blockera samma filer.

<!-- /payment-policy-20261116 -->

När noden har fått ett giltigt versionssvar får motparten tid att skicka en bekräftelse. Om två utgående anslutningar leder till samma nod hålls en tillgänglig väg öppen tills synkroniseringen är klar via en av dem. Det inbyggda självtestet godtar ett block med giltigt arbetsbevis innan anslutningsbeviset kommer fram. Därefter kontrollerar det de tre vittnenas underskrifter, att beviset vidarebefordras och att det finns kvar efter omstart.
