# SUMUWW · Versionsnoter

Med ét input på 1 SMW afhænger gebyret af, om du skal have penge tilbage. Hvis input og output er af typen P2WPKH, koster det ved en sats på 1 yugeon/vB præcis 110 yugeon at sende 0.99999890 SMW. Der er ingen byttepenge. Sender du 0.8 SMW fra samme input, tilføjes et output til byttepengene, og gebyret bliver 141 yugeon. Tegnebogen sender byttepengene tilbage, hvis beløbet efter gebyret når en minimumsgrænse, der tager højde for, hvad det koster at bruge byttepengene senere. Et mindre restbeløb indgår i det gebyr, der vises før godkendelsen. For et input fra en tegnebog med native SegWit (P2WPKH) regner estimatet med op til 71 byte til signaturen, inklusive hash-typen.


0.57.61 · Når du skifter sprog i appen, opdateres ikonet på proceslinjen i Windows også.

Noden åbner normalt 10 udgående forbindelser. De fleste videresender blokke og transaktioner. En afprøvet reserveforbindelse kan videresende blokke, og noden kan kortvarigt åbne en 11. forbindelse for at finde andre noder. Grænsen er 125 i alt. Der er plads til op til 117 indgående forbindelser, eller 115 ved 10 udgående. På computeren vises nu kun det samlede antal tilsluttede noder. Hver miner bygger sine egne blokke. PC-noden videresender færdige blokke og afviser telefonens anmodninger om mineopgaver og indsendte løsninger.

Efter en genstart fortsætter noden fra den sidste blok, den selv har verificeret, og kontrollerer nye blokke. Hvis den gemte verifikation mangler eller ikke stemmer, kontrollerer den den gemte historik igen.


SUMUWW PC 0.57.61 · Noden validerer, gemmer, videresender og stiller kædedata til rådighed.

## Signaturformat

Det valgfrie kildekode-SDK samler transaktioner og kontrollerer leverede signaturer uden nøgler eller netværk. Det er hverken signeringsprogram eller nodekommando. P2WPKH-begrænsningen gælder eksemplets format, ikke noden. Den personlige tegnebog er stadig tilgængelig.

## RPC- og HTTP-API

validateaddress kontrollerer kontrolsum og valgt netværk. decoderawtransaction returnerer decoded_only, ikke bevis for gyldig signatur eller bekræftelse. OP_RETURN gemmer data til eksterne programmer. Noden tilføjer gebyrforespørgsler, kontrol før afsendelse, status for RBF-erstatning og data i blokrækkefølge. Erstatningen valideres, før ventende transaktioner fjernes. Flere signaturer og låste outputs er implementeret til isolerede aktiveringstests; de er endnu ikke aktive på det offentlige netværk.

## Verifikation

Installer afhængighederne og kør python examples/node_contract.py fra kildekoden. Offentlige testnøgler og midlertidigt regtest afprøver indsendelse, afvisning, bekræftelser, reorganisering og databevaring. Ingen rigtige midler, brugerprofiler eller hardware til signering bruges.

[Dokumentation](README.html) · [Nodegrænseflade](EXCHANGE_INTEGRATION.html) · [RPC- og HTTP-API](RPC_API.html) · [Nodedrift](NETWORK_RUNBOOK.html) · [Verifikation](EXCHANGE_EXAMPLES.html)

[Uddybende engelsk reference](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Gebyrer, gennemgået transaktion og kompatibilitet

Gebyret er summen af inputs minus summen af outputs. Estimatet medregner kun et tilbagebetalingsoutput, når tegnebogen faktisk opretter en tilstrækkelig restbetaling. Et restbeløb under tegnebogens grænse lægges til gebyret; det endelige gebyr og det samlede træk vises til gennemgang. Satsen angives i yugeon/vB. Den virtuelle størrelse er transaktionens vægt divideret med fire og rundet op.

Tegnebogen vælger inputs og outputs én gang og signerer den samme transaktionsplan. Ved bekræftelse indsendes den gemte signerede transaktion uden at blive genopbygget eller få genberegnet gebyret. Et udløbet tilbud eller inputs, der allerede er brugt, kræver en ny gennemgang. Optagelse i den lokale kø er ikke en bekræftelse i en blok.

Ved almindelige P2WPKH-betalinger laver tegnebogen low-R- og low-S-signaturer på højst 71 byte inklusive SIGHASH_ALL-byten. Dette er en politik for signering og størrelsesestimering, ikke en ny konsensusgrænse for andre gyldige signaturer. Kortere signaturer kan mindske den faktiske virtuelle størrelse. De foreslåede satser bygger stadig på den lokale kø; en størrelsesberegning som i Bitcoin overtager ikke Bitcoin-netværkets gebyrsatser.

## Windows-I2P-komponent og sikkerhedskontrol

Windows-pakkerne indeholder officiel i2pd 3.0.0 med opdaterede kontrolsummer og certifikater til den første forbindelse. I den registrerede kontrol registrerer Defender stadig det officielle I2P-program og det oprindelige ZIP-arkiv som trusler. Et match med den officielle hash beviser hverken sikkerhed eller en falsk alarm. En lokal filundtagelse gælder kun på den computer, hvor den er oprettet; den offentlige pakke tilføjer den ikke. Andre computere kan blokere de samme filer.

<!-- /payment-policy-20261116 -->
