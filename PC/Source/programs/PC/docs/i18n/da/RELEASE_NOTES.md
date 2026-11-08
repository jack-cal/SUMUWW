# SUMUWW · Versionsnoter

Noden åbner normalt 10 udgående forbindelser. De fleste videresender blokke og transaktioner. En afprøvet reserveforbindelse kan videresende blokke, og noden kan kortvarigt åbne en 11. forbindelse for at finde andre noder. Grænsen er 125 i alt. Der er plads til op til 117 indgående forbindelser, eller 115 ved 10 udgående. På computeren vises nu kun det samlede antal tilsluttede noder. Hver miner bygger sine egne blokke. PC-noden videresender færdige blokke og afviser telefonens anmodninger om mineopgaver og indsendte løsninger.

Efter en genstart fortsætter noden fra den sidste blok, den selv har verificeret, og kontrollerer nye blokke. Hvis den gemte verifikation mangler eller ikke stemmer, kontrollerer den den gemte historik igen.


SUMUWW PC 0.57.54 · Noden validerer, gemmer, videresender og stiller kædedata til rådighed.

## Signaturformat

Det valgfrie kildekode-SDK samler transaktioner og kontrollerer leverede signaturer uden nøgler eller netværk. Det er hverken signeringsprogram eller nodekommando. P2WPKH-begrænsningen gælder eksemplets format, ikke noden. Den personlige tegnebog er stadig tilgængelig.

## RPC- og HTTP-API

validateaddress kontrollerer kontrolsum og valgt netværk. decoderawtransaction returnerer decoded_only, ikke bevis for gyldig signatur eller bekræftelse. OP_RETURN gemmer data til eksterne programmer. Noden tilføjer gebyrforespørgsler, kontrol før afsendelse, status for RBF-erstatning og data i blokrækkefølge. Erstatningen valideres, før ventende transaktioner fjernes. Flere signaturer og låste outputs er implementeret til isolerede aktiveringstests; de er endnu ikke aktive på det offentlige netværk.

## Verifikation

Installer afhængighederne og kør python examples/node_contract.py fra kildekoden. Offentlige testnøgler og midlertidigt regtest afprøver indsendelse, afvisning, bekræftelser, reorganisering og databevaring. Ingen rigtige midler, brugerprofiler eller hardware til signering bruges.

[Dokumentation](README.html) · [Nodegrænseflade](EXCHANGE_INTEGRATION.html) · [RPC- og HTTP-API](RPC_API.html) · [Nodedrift](NETWORK_RUNBOOK.html) · [Verifikation](EXCHANGE_EXAMPLES.html)

[Uddybende engelsk reference](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
