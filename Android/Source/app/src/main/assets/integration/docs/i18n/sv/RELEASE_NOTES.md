# SUMUWW Android 0.6.99 · Versionsinformation

Efter en omstart fortsätter noden från det senaste block som den själv har verifierat och kontrollerar nya block. Om den sparade verifieringsposten saknas eller inte stämmer kontrollerar noden den sparade historiken igen.

SUMUWW Android 0.6.99 · Noden validerar, lagrar, vidarebefordrar och tillhandahåller kedjedata.

API-specifikationen beskriver den inbyggda nodkärnan. Android-appen saknar skärm för RPC-inställningar.

## RPC- och HTTP-API

validateaddress kontrollerar kontrollsumman och det valda nätverket. decoderawtransaction ger decoded_only, inget bevis på giltig signatur eller bekräftelse. OP_RETURN bevarar data för externa program. Noden lägger till avgiftsfrågor, kontroll före sändning, status för RBF-ersättning och data i blockordning. Ersättningen valideras innan väntande transaktioner tas bort. Flera signaturer och låsta utdata är implementerade för isolerade aktiveringstester; de är ännu inte aktiva i det offentliga nätverket.

[API_CONTRACT.json](../../../API_CONTRACT.json)
