# SUMUWW Android 0.6.103 · Maelezo ya toleo

Ukitumia ingizo moja la 1 SMW, ada hutegemea kama utarudishiwa chenji. Ikiwa ingizo na matokeo yote ni ya aina ya P2WPKH na kiwango cha ada ni 1 yugeon/vB, kutuma 0.99999890 SMW kunagharimu 110 yugeon bila chenji. Ukituma 0.8 SMW kutoka kwenye ingizo hilohilo, muamala unakuwa na tokeo la chenji na ada inakuwa 141 yugeon. Pochi inakurudishia chenji ikiwa kiasi kinachobaki baada ya ada kinafikia kiwango cha chini kinachozingatia gharama ya kuitumia chenji hiyo baadaye. Ikiwa kiasi hicho ni kidogo zaidi, hujumuishwa katika ada inayoonyeshwa kabla ya uthibitisho. Kwa ingizo la pochi la SegWit asilia (P2WPKH), makadirio hutenga hadi baiti 71 kwa sahihi, ikijumuisha aina ya heshi.

Nodi inapoanzishwa tena, huendelea kutoka kwenye bloku ya mwisho iliyothibitisha kwenye kifaa na hukagua bloku mpya. Ikiwa rekodi ya uthibitishaji haipo au hailingani, nodi hukagua tena historia iliyohifadhiwa.

SUMUWW Android 0.6.103 · Nodi huthibitisha, huhifadhi, husambaza na kuruhusu kusoma data ya mnyororo.

Maelezo ya API yanaeleza kiini cha nodi kilichojumuishwa. Programu ya Android haina skrini ya mipangilio ya RPC.

## API ya RPC na HTTP

validateaddress hukagua checksum na mtandao uliochaguliwa. decoded_only kutoka decoderawtransaction humaanisha kusoma muundo tu, si kuthibitisha sahihi au muamala. OP_RETURN huhifadhi data kwa programu za nje. Nodi imeongezewa maswali ya ada, ukaguzi kabla ya kutuma, hali ya ubadilishaji wa RBF na rekodi za data kwa mpangilio wa vitalu. Muamala mbadala hukaguliwa kabla ya kuondoa miamala inayosubiri. Sahihi nyingi na matokeo yaliyofungwa yameundwa kwa majaribio tofauti; bado hayajawashwa kwenye mtandao wa umma.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Ada, muamala uliokaguliwa na uoanifu

Ada ni jumla ya ingizo ukiondoa jumla ya matokeo. Makadirio yanahesabu tokeo la chenji tu ikiwa pochi itaunda chenji inayofikia kiwango chake cha chini. Salio dogo kuliko kiwango hicho huongezwa kwenye ada; ada inayotokana na hesabu hiyo na jumla itakayokatwa huonyeshwa ili vikaguliwe. Kiwango cha ada huandikwa kwa yugeon/vB. Ukubwa pepe ni uzito wa muamala uliogawanywa kwa nne na kuzungushwa kwenda juu.

Pochi huchagua ingizo na matokeo mara moja tu, kisha hutia sahihi mpango huohuo wa muamala. Unapothibitisha, hutuma muamala wenye sahihi uliohifadhiwa bila kuujenga upya au kukokotoa tena ada. Makadirio yakiisha muda au ingizo likiwa limetumika, ukaguzi mpya unahitajika. Kukubaliwa katika foleni ya ndani si uthibitisho ndani ya bloku.

Kwa malipo ya kawaida ya P2WPKH, pochi hutengeneza sahihi za low-R na low-S zenye hadi baiti 71, ikijumuisha baiti ya SIGHASH_ALL. Hii ni sera ya utiaji sahihi na makadirio ya ukubwa, wala si kikomo kipya cha makubaliano kwa sahihi nyingine halali. Sahihi fupi inaweza kupunguza ukubwa pepe halisi. 

## Uoanifu wa sahihi za Android

Muundo wa faili za pochi, anwani na sarafu zilizopo havijabadilika. Nakala fiche ya pochi iliyopo inaweza kurejeshwa katika programu mpya ili kuendelea kutumia pochi hiyohiyo. Nodi ya Android 0.6.103 na pochi 1.1.14 hutumia ufunguo mpya wa kusaini matoleo. Haziwezi kuchukua nafasi ya programu iliyosainiwa kwa ufunguo tofauti. Hifadhi programu ya zamani na data yake mpaka uwe na nakala fiche ya pochi na njia inayofanya kazi ya kuirejesha. Usiondoe programu ya zamani kwa lengo la kulazimisha usakinishaji wa sasisho.

<!-- /payment-policy-20261116 -->
