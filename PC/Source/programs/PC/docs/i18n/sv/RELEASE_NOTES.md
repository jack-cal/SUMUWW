# SUMUWW · Versionsinformation

Noden öppnar normalt 10 utgående anslutningar. De flesta förmedlar block och transaktioner. En verifierad reservanslutning kan förmedla block, och noden kan tillfälligt öppna en elfte anslutning för att hitta andra noder. Totalt tillåts 125 anslutningar. Högst 117 kan vara inkommande, eller 115 vid 10 utgående. Datorappen visar nu bara det sammanlagda antalet anslutna noder. Varje gruvenhet bygger sina egna block. PC-noden vidarebefordrar färdiga block och avvisar telefonens begäran om gruvuppgifter och inskickade lösningar.

Efter en omstart fortsätter noden från det senaste block som den själv har verifierat och kontrollerar nya block. Om den sparade verifieringsposten saknas eller inte stämmer kontrollerar noden den sparade historiken igen.


SUMUWW PC 0.57.54 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

## Signeringsformat

Det valfria källkods-SDK:t sammanställer transaktioner och verifierar tillhandahållna signaturer utan nycklar eller nätverk. Det är inget signeringsprogram eller nodkommando. P2WPKH-begränsningen gäller exempelformatet, inte noden. Den personliga plånboken finns kvar.

## RPC- och HTTP-API

validateaddress kontrollerar kontrollsumman och det valda nätverket. decoderawtransaction ger decoded_only, inget bevis på giltig signatur eller bekräftelse. OP_RETURN bevarar data för externa program. Noden lägger till avgiftsfrågor, kontroll före sändning, status för RBF-ersättning och data i blockordning. Ersättningen valideras innan väntande transaktioner tas bort. Flera signaturer och låsta utdata är implementerade för isolerade aktiveringstester; de är ännu inte aktiva i det offentliga nätverket.

## Verifiering

Installera beroendena och kör python examples/node_contract.py från källkoden. Offentliga testnycklar och tillfälligt regtest prövar insändning, avvisning, bekräftelser, omorganisation och lagring. Inga riktiga medel, användarprofiler eller hårdvarusignerare används.

[Dokumentation](README.html) · [Nodgränssnitt](EXCHANGE_INTEGRATION.html) · [RPC- och HTTP-API](RPC_API.html) · [Noddrift](NETWORK_RUNBOOK.html) · [Verifiering](EXCHANGE_EXAMPLES.html)

[Utförlig engelsk referens](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
