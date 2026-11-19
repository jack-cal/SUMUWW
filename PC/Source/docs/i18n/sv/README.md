# SUMUWW · Dokumentation

Med en ingång på 1 SMW beror avgiften på om du ska få växel tillbaka. Om ingången och alla utgångar är av typen P2WPKH och avgiftssatsen är 1 yugeon/vB kostar det 110 yugeon att skicka 0.99999890 SMW. Då blir det ingen växel. Skickar du 0.8 SMW från samma ingång tillkommer en utgång för växeln och avgiften blir 141 yugeon. Plånboken ger växel tillbaka om beloppet som återstår efter avgiften når en gräns som tar hänsyn till kostnaden för att använda växeln senare. Ett mindre restbelopp ingår i avgiften som visas före bekräftelsen. För en indata från en plånbok med inbyggt SegWit-stöd (P2WPKH) räknar uppskattningen med högst 71 byte för signaturen, inklusive hashtypen.

SUMUWW PC 0.57.51 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

## Signeringsformat

Det valfria källkods-SDK:t sammanställer transaktioner och verifierar tillhandahållna signaturer utan nycklar eller nätverk. Det är inget signeringsprogram eller nodkommando. P2WPKH-begränsningen gäller exempelformatet, inte noden. Den personliga plånboken finns kvar.

## RPC- och HTTP-API

validateaddress kontrollerar kontrollsumman och det valda nätverket. decoderawtransaction ger decoded_only, inget bevis på giltig signatur eller bekräftelse. OP_RETURN bevarar data för externa program. Noden lägger till avgiftsfrågor, kontroll före sändning, status för RBF-ersättning och data i blockordning. Ersättningen valideras innan väntande transaktioner tas bort. Flera signaturer och låsta utdata är implementerade för isolerade aktiveringstester; de är ännu inte aktiva i det offentliga nätverket.

## Verifiering

Installera beroendena och kör python examples/node_contract.py från källkoden. Offentliga testnycklar och tillfälligt regtest prövar insändning, avvisning, bekräftelser, omorganisation och lagring. Inga riktiga medel, användarprofiler eller hårdvarusignerare används.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Nodgränssnitt](EXCHANGE_INTEGRATION.html) · [RPC- och HTTP-API](RPC_API.html) · [Noddrift](NETWORK_RUNBOOK.html) · [Versionsinformation](RELEASE_NOTES.html) · [Verifiering](EXCHANGE_EXAMPLES.html)

[Utförlig engelsk referens](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Avgifter, granskad transaktion och kompatibilitet

Avgiften är summan av ingångarna minus summan av utgångarna. Uppskattningen räknar bara med en växelutgång när plånboken faktiskt skapar tillräcklig växel. Ett restbelopp under plånbokens gräns läggs till avgiften; den slutliga avgiften och hela debiteringen visas för granskning. Avgiftssatsen anges i yugeon/vB. Virtuell storlek är transaktionens vikt delad med fyra, avrundad uppåt.

Plånboken väljer ingångar och utgångar en gång och signerar samma transaktionsplan. Vid bekräftelse skickas den sparade signerade transaktionen utan att byggas om eller få avgiften omräknad. Ett utgånget förslag eller redan förbrukade ingångar kräver en ny granskning. Att tas emot i den lokala kön betyder inte att transaktionen är bekräftad i ett block.

För vanliga P2WPKH-betalningar skapar plånboken low-R- och low-S-signaturer på högst 71 byte, inklusive SIGHASH_ALL-byten. Det är en policy för signering och storleksuppskattning, inte en ny konsensusgräns för andra giltiga signaturer. En kortare signatur kan minska den verkliga virtuella storleken. 

<!-- /payment-policy-20261116 -->
