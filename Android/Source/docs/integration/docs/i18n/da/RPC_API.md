# SUMUWW Android 0.6.103 · RPC- og HTTP-API

SUMUWW Android 0.6.103 · Noden validerer, gemmer, videresender og stiller kædedata til rådighed.

API-specifikationen beskriver den indbyggede nodekerne. Android-appen har ingen skærm til RPC-konfiguration.

## RPC- og HTTP-API

validateaddress kontrollerer kontrolsum og valgt netværk. decoderawtransaction returnerer decoded_only, ikke bevis for gyldig signatur eller bekræftelse. OP_RETURN gemmer data til eksterne programmer. Noden tilføjer gebyrforespørgsler, kontrol før afsendelse, status for RBF-erstatning og data i blokrækkefølge. Erstatningen valideres, før ventende transaktioner fjernes. Flere signaturer og låste outputs er implementeret til isolerede aktiveringstests; de er endnu ikke aktive på det offentlige netværk.

## Beløb og tilgængelige outputs

`_units` er hele mindsteenheder; `_smw` tekst med 8 decimaler; `_dora` kompatibilitetsalias. Intet beløbsfelt `_sumuww` findes. 1 SMW = 100000000 enheder. `gettxout` har ikke `spendable` og kan returnere umodne coinbase-outputs. Mindst 100 bekræftelser kræves til brug i næste blok. Filtrér `listunspent` på `spendable`; available i `getaddressbalance` udelader umodne midler og midler brugt af ventende transaktioner. Nye mempool-outputs er ikke bekræftede. Kontrollér spidsen mellem sider og validér valgte inputs igen.

1 SMW = 100.000.000 yugeon. Automatiske gebyrer tilbyder tre niveauer ud fra lokale observationer uden at garantere bekræftelsestiden. Du kan indtaste en sats i yugeon/vB. Kontrollér det endelige gebyr og totalen i SMW før afsendelse. En afvist transaktion reducerer ikke saldoen.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Automatiske gebyrer følger den ventende datamængde, blokkapaciteten og transaktionernes prioritet. Gebyrer fra tidligere blokke bruges ikke. Ved kort kø gælder minimumssatsen. Forhåndsvisningen opdateres; den endelige bekræftelse fastlægger gebyret. Oplysningerne dækker den tilsluttede lokale node, ikke alle noder.

Udskiftninger registreret af denne node bevares i historikken efter genstart af tegnebogen. Fjernede transaktioner påvirker ikke saldoen.

Minehistorikken viser ny udstedelse, gebyrer og samlet belønning for hver blok hver for sig. Det beløb, din wallet modtager, vises separat. Ved delvis udbetaling antages ingen fordeling mellem de to dele. Noden tilbyder 28 RPC-metoder, herunder gebyrestimering, og kontrollerer og videresender signerede transaktioner.

## Find transaktioner og blokke

`getrawtransaction` søger aktiv kæde og mempool, ikke transaktioner udelukkende i forældreløse grene. Inputs angiver tidligere outputs, ikke én afsenderadresse. `getblock` kræver boolesk `verbose`; gemte inaktive blokke har `active=false`, `confirmations=-1`. Råtransaktioner er stadig tilgængelige via blokhash. `findspendingtransaction` søger kun bekræftede aktive forbrug; null beviser ikke tilgængelighed. Kontrollér `gettxout` med `include_mempool=true`. Bekræftelser og aktiv status kan ændres ved reorganisering.

| method | params |
|---|---|
| `getblockchaininfo` | `{} / []` |
| `gethtlcinfo` | `{} / []` |
| `getspendinginfo` | `{} / []` |
| `getdatarecords` | `blockhash, offset=0, limit=100` |
| `decodescript` | `hex` |
| `gettxout` | `txid, index, include_mempool=true` |
| `findspendingtransaction` | `txid, index, start_height=0` |
| `getnetworkinfo` | `{} / []` |
| `getblockcount` | `{} / []` |
| `getbestblockhash` | `{} / []` |
| `getblockhash` | `height` |
| `getblock` | `hash, verbose=true` |
| `getrawmempool` | `{} / []` |
| `getmempoolinfo` | `{} / []` |
| `getmempoolpolicy` | `{} / []` |
| `estimatefee` | `vsize=140, mode=normal` |
| `testmempoolaccept` | `hex` |
| `getmempoolentry` | `txid` |
| `gettransactionstatus` | `txid` |
| `getrawtransaction` | `txid, verbose=true` |
| `decoderawtransaction` | `hex` |
| `validateaddress` | `address` |
| `listunspent` | `address, limit=100, offset=0` |
| `getaddressbalance` | `address` |
| `sendrawtransaction` | `hex` |
| `submitblock` | `hex` |
| `getblocktemplate` | `address` |
| `help` | `{} / []` |

| HTTP | URI | JSON |
|---|---|---|
| `GET` | `/api/v1/info` | `—` |
| `GET` | `/api/v1/network` | `—` |
| `GET` | `/api/v1/mempool` | `—` |
| `GET` | `/api/v1/mempool/info` | `—` |
| `GET` | `/api/v1/blocks/{height-or-hash}` | `—` |
| `GET` | `/api/v1/transactions/{txid}` | `—` |
| `GET` | `/api/v1/addresses/{address}/balance` | `—` |
| `GET` | `/api/v1/addresses/{address}/utxos?limit=100&offset=0` | `—` |
| `POST` | `/api/v1/transactions` | `{"hex":"..."}` |
| `POST` | `/api/v1/blocks` | `{"hex":"..."}` |
| `POST` | `/api/v1/mining/template` | `{"address":"..."}` |

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Gebyrer, gennemgået transaktion og kompatibilitet

Gebyret er summen af inputs minus summen af outputs. Estimatet medregner kun et tilbagebetalingsoutput, når tegnebogen faktisk opretter en tilstrækkelig restbetaling. Et restbeløb under tegnebogens grænse lægges til gebyret; det endelige gebyr og det samlede træk vises til gennemgang. Satsen angives i yugeon/vB. Den virtuelle størrelse er transaktionens vægt divideret med fire og rundet op.

Tegnebogen vælger inputs og outputs én gang og signerer den samme transaktionsplan. Ved bekræftelse indsendes den gemte signerede transaktion uden at blive genopbygget eller få genberegnet gebyret. Et udløbet tilbud eller inputs, der allerede er brugt, kræver en ny gennemgang. Optagelse i den lokale kø er ikke en bekræftelse i en blok.

Ved almindelige P2WPKH-betalinger laver tegnebogen low-R- og low-S-signaturer på højst 71 byte inklusive SIGHASH_ALL-byten. Dette er en politik for signering og størrelsesestimering, ikke en ny konsensusgrænse for andre gyldige signaturer. Kortere signaturer kan mindske den faktiske virtuelle størrelse. 

## Kompatibilitet for Android-signering

Tegnebogens filformat, adresser og eksisterende mønter er uændrede. Den eksisterende krypterede sikkerhedskopi kan gendannes i den nye app, så den samme tegnebog fortsat kan bruges. Android-noden 0.6.103 og tegnebogen 1.1.14 bruger en ny signeringsnøgle til udgivelsen. De kan ikke erstatte en installation signeret med en anden nøgle. Behold den gamle app og dens data, indtil du har en krypteret sikkerhedskopi af tegnebogen og en fungerende gendannelsesmetode. Afinstaller ikke den gamle app blot for at tvinge en opdatering igennem.

<!-- /payment-policy-20261116 -->
