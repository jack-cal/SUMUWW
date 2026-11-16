# SUMUWW · Uendeshaji wa nodi

Kwa kawaida nodi hufungua miunganisho 10 ya kutoka. Mingi hupitisha bloku na miamala. Nodi inaweza kutumia muunganisho wa akiba uliothibitishwa kupitisha bloku na kufungua wa 11 kwa muda mfupi ili kutafuta nodi nyingine. Kikomo cha jumla ni miunganisho 125. Inaweza kupokea hadi miunganisho 117 ya kuingia, au 115 ikiwa kuna 10 ya kutoka. Programu ya kompyuta sasa inaonyesha jumla pekee ya nodi zilizounganishwa. Kila kifaa cha uchimbaji huunda bloku zake. Nodi ya kompyuta husambaza bloku zilizokamilika na hukataa maombi ya kazi za uchimbaji na majibu kutoka kwenye simu.

Nodi inapoanzishwa tena, huendelea kutoka kwenye bloku ya mwisho iliyothibitisha kwenye kifaa na hukagua bloku mpya. Ikiwa rekodi ya uthibitishaji haipo au hailingani, nodi hukagua tena historia iliyohifadhiwa.


SUMUWW PC 0.57.61 · Nodi huthibitisha, huhifadhi, husambaza na kuruhusu kusoma data ya mnyororo.

## Mtandao na anwani

Mtandao wa umma ni `sumuww`, jina la ndani ni `dora`. Hakiki hash ya kitalu cha mwanzo hapa chini. Anwani hutumia witness v0 P2WPKH na HASH160 ya ufunguo wa umma wa secp256k1 uliobanwa. Memo au tag si lazima. Kataa anwani ya mtandao usio sahihi na checksum batili. Rekodi tawi la HD la kupokea/chenji na faharasa; usidhani njia ya utoaji wa funguo ya Bitcoin.

## Uthibitishaji na mipaka

Washa RPC waziwazi kwenye loopback ya namba `127.0.0.1:18443` yenye tokeni binafsi ya Bearer. Hakuna kufungua pochi au kusaini kwa mbali. Tumia huduma ya ndani au handaki lenye uthibitishaji; maombi ya kivinjari ya Origin/Referer hukataliwa. JSON-RPC hutumia POST `/rpc`, kitu/safu `params` na `id`; arifa hurudisha HTTP 204. Mipaka: mwili baiti 8004096, vichwa 8192, kundi 16, maombi ya wakati mmoja 16, muda sekunde 10; limit 1–1000, offset 0–1000000. Kuna mbinu 28 na njia 11 za REST.

## Kutafuta miamala na vitalu

`getrawtransaction` hutafuta mnyororo hai na mempool, si miamala iliyo kwenye matawi yaliyotengwa pekee. Ingizo hutaja matokeo yaliyopita, si anwani moja ya mtumaji. `getblock` hupokea `verbose` ya Boolean; vitalu visivyo hai vilivyohifadhiwa vina `active=false`, `confirmations=-1`. Miamala ghafi bado inapatikana kwa hash ya kitalu. `findspendingtransaction` hutafuta matumizi yaliyothibitishwa katika mnyororo hai tu; null haithibitishi kupatikana. Kagua `gettxout` yenye `include_mempool=true`. Uthibitisho na hali hai vinaweza kubadilika baada ya upangaji upya.

## Uhakiki

Sakinisha vitegemezi kisha endesha python examples/node_contract.py kutoka msimbo chanzo. Funguo za majaribio zilizo wazi na regtest ya muda hukagua utumaji, kukataliwa, uthibitisho, upangaji upya na uhifadhi. Hakuna fedha halisi, wasifu wa mtumiaji au kifaa cha kutia sahihi kinachotumiwa.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Nyaraka](README.html) · [Kiolesura cha nodi](EXCHANGE_INTEGRATION.html) · [API ya RPC na HTTP](RPC_API.html) · [Maelezo ya toleo](RELEASE_NOTES.html) · [Uhakiki](EXCHANGE_EXAMPLES.html)

[Rejea ya kina ya Kiingereza](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Ada, muamala uliokaguliwa na uoanifu

Ada ni jumla ya ingizo ukiondoa jumla ya matokeo. Makadirio yanahesabu tokeo la chenji tu ikiwa pochi itaunda chenji inayofikia kiwango chake cha chini. Salio dogo kuliko kiwango hicho huongezwa kwenye ada; ada inayotokana na hesabu hiyo na jumla itakayokatwa huonyeshwa ili vikaguliwe. Kiwango cha ada huandikwa kwa yugeon/vB. Ukubwa pepe ni uzito wa muamala uliogawanywa kwa nne na kuzungushwa kwenda juu.

Pochi huchagua ingizo na matokeo mara moja tu, kisha hutia sahihi mpango huohuo wa muamala. Unapothibitisha, hutuma muamala wenye sahihi uliohifadhiwa bila kuujenga upya au kukokotoa tena ada. Makadirio yakiisha muda au ingizo likiwa limetumika, ukaguzi mpya unahitajika. Kukubaliwa katika foleni ya ndani si uthibitisho ndani ya bloku.

Kwa malipo ya kawaida ya P2WPKH, pochi hutengeneza sahihi za low-R na low-S zenye hadi baiti 71, ikijumuisha baiti ya SIGHASH_ALL. Hii ni sera ya utiaji sahihi na makadirio ya ukubwa, wala si kikomo kipya cha makubaliano kwa sahihi nyingine halali. Sahihi fupi inaweza kupunguza ukubwa pepe halisi. Mapendekezo ya viwango bado hutumia foleni ya ndani; kutumia hesabu ya ukubwa inayofanana na Bitcoin hakumaanishi kutumia viwango vya ada vya mtandao wa Bitcoin.

## Kijenzi cha I2P cha Windows na ukaguzi wa usalama

Vifurushi vya Windows vina i2pd 3.0.0 rasmi pamoja na hashi na vyeti vya kuanzisha muunganisho vilivyosasishwa. Katika ukaguzi uliorekodiwa, Defender bado hutambua faili rasmi ya I2P na ZIP yake kama tishio. Hashi inayolingana na chanzo rasmi haithibitishi usalama wala tahadhari ya kimakosa. Ruhusa ya kutokagua faili kwenye kompyuta moja hutumika hapo tu; kifurushi cha umma hakiiongezi. Kompyuta nyingine zinaweza kuzuia faili hizo.

<!-- /payment-policy-20261116 -->

Baada ya kupokea jibu halali la toleo, nodi huipa nodi nyingine muda wa kutuma uthibitisho. Ikiwa miunganisho miwili inayotoka inafika kwenye nodi ileile, njia inayopatikana hubaki wazi hadi usawazishaji ukamilike kupitia mojawapo. Ukaguzi wa ndani hukubali bloku yenye uthibitisho halali wa kazi kabla ya kupokea uthibitisho wa muunganisho. Kisha hukagua saini za mashahidi watatu, usambazaji wa uthibitisho huo na kama bado unapatikana baada ya kuwasha upya.
