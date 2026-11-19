# SUMUWW Android 0.6.103 · Uendeshaji wa nodi

Nodi inapoanzishwa tena, huendelea kutoka kwenye bloku ya mwisho iliyothibitisha kwenye kifaa na hukagua bloku mpya. Ikiwa rekodi ya uthibitishaji haipo au hailingani, nodi hukagua tena historia iliyohifadhiwa.

SUMUWW Android 0.6.103 · Nodi huthibitisha, huhifadhi, husambaza na kuruhusu kusoma data ya mnyororo.

## Mtandao na anwani

Mtandao wa umma ni `sumuww`, jina la ndani ni `dora`. Hakiki hash ya kitalu cha mwanzo hapa chini. Anwani hutumia witness v0 P2WPKH na HASH160 ya ufunguo wa umma wa secp256k1 uliobanwa. Memo au tag si lazima. Kataa anwani ya mtandao usio sahihi na checksum batili. Rekodi tawi la HD la kupokea/chenji na faharasa; usidhani njia ya utoaji wa funguo ya Bitcoin.

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

Baada ya kupokea jibu halali la toleo, nodi huipa nodi nyingine muda wa kutuma uthibitisho. Ikiwa miunganisho miwili inayotoka inafika kwenye nodi ileile, njia inayopatikana hubaki wazi hadi usawazishaji ukamilike kupitia mojawapo. 
