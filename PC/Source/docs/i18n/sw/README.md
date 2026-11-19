# SUMUWW · Nyaraka

Ukitumia ingizo moja la 1 SMW, ada hutegemea kama utarudishiwa chenji. Ikiwa ingizo na matokeo yote ni ya aina ya P2WPKH na kiwango cha ada ni 1 yugeon/vB, kutuma 0.99999890 SMW kunagharimu 110 yugeon bila chenji. Ukituma 0.8 SMW kutoka kwenye ingizo hilohilo, muamala unakuwa na tokeo la chenji na ada inakuwa 141 yugeon. Pochi inakurudishia chenji ikiwa kiasi kinachobaki baada ya ada kinafikia kiwango cha chini kinachozingatia gharama ya kuitumia chenji hiyo baadaye. Ikiwa kiasi hicho ni kidogo zaidi, hujumuishwa katika ada inayoonyeshwa kabla ya uthibitisho. Kwa ingizo la pochi la SegWit asilia (P2WPKH), makadirio hutenga hadi baiti 71 kwa sahihi, ikijumuisha aina ya heshi.

SUMUWW PC 0.57.51 · Nodi huthibitisha, huhifadhi, husambaza na kuruhusu kusoma data ya mnyororo.

## Muundo wa saini

SDK ya hiari katika msimbo chanzo huunda miamala na kuhakiki sahihi zilizotolewa bila funguo au mtandao. Si programu ya kutia sahihi wala amri ya nodi. Kikomo cha P2WPKH ni cha muundo wa mfano, si nodi. Pochi binafsi iliyopo bado inapatikana.

## API ya RPC na HTTP

validateaddress hukagua checksum na mtandao uliochaguliwa. decoded_only kutoka decoderawtransaction humaanisha kusoma muundo tu, si kuthibitisha sahihi au muamala. OP_RETURN huhifadhi data kwa programu za nje. Nodi imeongezewa maswali ya ada, ukaguzi kabla ya kutuma, hali ya ubadilishaji wa RBF na rekodi za data kwa mpangilio wa vitalu. Muamala mbadala hukaguliwa kabla ya kuondoa miamala inayosubiri. Sahihi nyingi na matokeo yaliyofungwa yameundwa kwa majaribio tofauti; bado hayajawashwa kwenye mtandao wa umma.

## Uhakiki

Sakinisha vitegemezi kisha endesha python examples/node_contract.py kutoka msimbo chanzo. Funguo za majaribio zilizo wazi na regtest ya muda hukagua utumaji, kukataliwa, uthibitisho, upangaji upya na uhifadhi. Hakuna fedha halisi, wasifu wa mtumiaji au kifaa cha kutia sahihi kinachotumiwa.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Kiolesura cha nodi](EXCHANGE_INTEGRATION.html) · [API ya RPC na HTTP](RPC_API.html) · [Uendeshaji wa nodi](NETWORK_RUNBOOK.html) · [Maelezo ya toleo](RELEASE_NOTES.html) · [Uhakiki](EXCHANGE_EXAMPLES.html)

[Rejea ya kina ya Kiingereza](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Ada, muamala uliokaguliwa na uoanifu

Ada ni jumla ya ingizo ukiondoa jumla ya matokeo. Makadirio yanahesabu tokeo la chenji tu ikiwa pochi itaunda chenji inayofikia kiwango chake cha chini. Salio dogo kuliko kiwango hicho huongezwa kwenye ada; ada inayotokana na hesabu hiyo na jumla itakayokatwa huonyeshwa ili vikaguliwe. Kiwango cha ada huandikwa kwa yugeon/vB. Ukubwa pepe ni uzito wa muamala uliogawanywa kwa nne na kuzungushwa kwenda juu.

Pochi huchagua ingizo na matokeo mara moja tu, kisha hutia sahihi mpango huohuo wa muamala. Unapothibitisha, hutuma muamala wenye sahihi uliohifadhiwa bila kuujenga upya au kukokotoa tena ada. Makadirio yakiisha muda au ingizo likiwa limetumika, ukaguzi mpya unahitajika. Kukubaliwa katika foleni ya ndani si uthibitisho ndani ya bloku.

Kwa malipo ya kawaida ya P2WPKH, pochi hutengeneza sahihi za low-R na low-S zenye hadi baiti 71, ikijumuisha baiti ya SIGHASH_ALL. Hii ni sera ya utiaji sahihi na makadirio ya ukubwa, wala si kikomo kipya cha makubaliano kwa sahihi nyingine halali. Sahihi fupi inaweza kupunguza ukubwa pepe halisi. 

<!-- /payment-policy-20261116 -->
