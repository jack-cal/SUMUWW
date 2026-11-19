# SUMUWW Android 0.6.103 · Kiolesura cha nodi

SUMUWW Android 0.6.103 · Nodi huthibitisha, huhifadhi, husambaza na kuruhusu kusoma data ya mnyororo.

Maelezo ya API yanaeleza kiini cha nodi kilichojumuishwa. Programu ya Android haina skrini ya mipangilio ya RPC.

## Mtandao na anwani

Mtandao wa umma ni `sumuww`, jina la ndani ni `dora`. Hakiki hash ya kitalu cha mwanzo hapa chini. Anwani hutumia witness v0 P2WPKH na HASH160 ya ufunguo wa umma wa secp256k1 uliobanwa. Memo au tag si lazima. Kataa anwani ya mtandao usio sahihi na checksum batili. Rekodi tawi la HD la kupokea/chenji na faharasa; usidhani njia ya utoaji wa funguo ya Bitcoin.

## API ya RPC na HTTP

validateaddress hukagua checksum na mtandao uliochaguliwa. decoded_only kutoka decoderawtransaction humaanisha kusoma muundo tu, si kuthibitisha sahihi au muamala. OP_RETURN huhifadhi data kwa programu za nje. Nodi imeongezewa maswali ya ada, ukaguzi kabla ya kutuma, hali ya ubadilishaji wa RBF na rekodi za data kwa mpangilio wa vitalu. Muamala mbadala hukaguliwa kabla ya kuondoa miamala inayosubiri. Sahihi nyingi na matokeo yaliyofungwa yameundwa kwa majaribio tofauti; bado hayajawashwa kwenye mtandao wa umma.

## Kiasi na matokeo yanayopatikana

`_units` ni namba kamili za kipimo kidogo zaidi; `_smw` ni maandishi yenye desimali 8; `_dora` ni jina la uoanifu. Hakuna sehemu ya kiasi `_sumuww`. 1 SMW = vipimo 100000000. `gettxout` haina `spendable` na inaweza kurudisha coinbase isiyokomaa. Angalau uthibitisho 100 unahitajika kutumia katika kitalu kinachofuata. Chuja `listunspent` kwa `spendable`; available ya `getaddressbalance` haijumuishi fedha zisizokomaa au zinazotumika na miamala inayosubiri. Matokeo mapya ya mempool hayajathibitishwa. Hakiki kilele kati ya kurasa na kagua tena ingizo zilizochaguliwa.

1 SMW = 100,000,000 yugeon. Ada ya kiotomatiki ina viwango vitatu vinavyotegemea taarifa za ndani, bila kuhakikisha muda wa uthibitisho. Unaweza kuingiza kiwango cha yugeon/vB mwenyewe. Kagua ada ya mwisho na jumla kwa SMW kabla ya kutuma. Muamala uliokataliwa haupunguzi salio.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Ada ya kiotomatiki hutegemea kiasi cha data inayosubiri, uwezo wa vitalu na kipaumbele cha miamala. Ada za vitalu vya zamani hazitumiki. Foleni ikiwa fupi, kiwango cha chini hubaki. Hakiki husasishwa; uthibitisho wa mwisho huweka ada isiyobadilika. Uchunguzi unahusu nodi ya ndani iliyounganishwa, si nodi zote.

Historia ya miamala iliyobadilishwa ambayo nodi hii imerekodi huhifadhiwa baada ya kuanzisha pochi upya. Miamala iliyoondolewa haiathiri salio.

Historia ya uchimbaji hutenganisha sarafu mpya, ada za miamala na jumla ya zawadi kwa kila bloku. Kiasi kilichopokelewa na pochi yako huonyeshwa kando. Zawadi ikidaiwa kwa sehemu, mgawanyo wa vipengele hivyo haukadiriwi. Nodi ina mbinu 28 za RPC, zikiwemo makadirio ya ada, na huthibitisha na kusambaza miamala iliyosainiwa.

## Kutafuta miamala na vitalu

`getrawtransaction` hutafuta mnyororo hai na mempool, si miamala iliyo kwenye matawi yaliyotengwa pekee. Ingizo hutaja matokeo yaliyopita, si anwani moja ya mtumaji. `getblock` hupokea `verbose` ya Boolean; vitalu visivyo hai vilivyohifadhiwa vina `active=false`, `confirmations=-1`. Miamala ghafi bado inapatikana kwa hash ya kitalu. `findspendingtransaction` hutafuta matumizi yaliyothibitishwa katika mnyororo hai tu; null haithibitishi kupatikana. Kagua `gettxout` yenye `include_mempool=true`. Uthibitisho na hali hai vinaweza kubadilika baada ya upangaji upya.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Ada, muamala uliokaguliwa na uoanifu

Ada ni jumla ya ingizo ukiondoa jumla ya matokeo. Makadirio yanahesabu tokeo la chenji tu ikiwa pochi itaunda chenji inayofikia kiwango chake cha chini. Salio dogo kuliko kiwango hicho huongezwa kwenye ada; ada inayotokana na hesabu hiyo na jumla itakayokatwa huonyeshwa ili vikaguliwe. Kiwango cha ada huandikwa kwa yugeon/vB. Ukubwa pepe ni uzito wa muamala uliogawanywa kwa nne na kuzungushwa kwenda juu.

Pochi huchagua ingizo na matokeo mara moja tu, kisha hutia sahihi mpango huohuo wa muamala. Unapothibitisha, hutuma muamala wenye sahihi uliohifadhiwa bila kuujenga upya au kukokotoa tena ada. Makadirio yakiisha muda au ingizo likiwa limetumika, ukaguzi mpya unahitajika. Kukubaliwa katika foleni ya ndani si uthibitisho ndani ya bloku.

Kwa malipo ya kawaida ya P2WPKH, pochi hutengeneza sahihi za low-R na low-S zenye hadi baiti 71, ikijumuisha baiti ya SIGHASH_ALL. Hii ni sera ya utiaji sahihi na makadirio ya ukubwa, wala si kikomo kipya cha makubaliano kwa sahihi nyingine halali. Sahihi fupi inaweza kupunguza ukubwa pepe halisi. 

## Uoanifu wa sahihi za Android

Muundo wa faili za pochi, anwani na sarafu zilizopo havijabadilika. Nakala fiche ya pochi iliyopo inaweza kurejeshwa katika programu mpya ili kuendelea kutumia pochi hiyohiyo. Nodi ya Android 0.6.103 na pochi 1.1.14 hutumia ufunguo mpya wa kusaini matoleo. Haziwezi kuchukua nafasi ya programu iliyosainiwa kwa ufunguo tofauti. Hifadhi programu ya zamani na data yake mpaka uwe na nakala fiche ya pochi na njia inayofanya kazi ya kuirejesha. Usiondoe programu ya zamani kwa lengo la kulazimisha usakinishaji wa sasisho.

<!-- /payment-policy-20261116 -->
