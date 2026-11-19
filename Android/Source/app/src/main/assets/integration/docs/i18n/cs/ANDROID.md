# SUMUWW Android 0.6.103 · Dokumentace

SUMUWW Android 0.6.103 · Uzel ověřuje, ukládá, předává a zpřístupňuje data řetězce.

## Síť a adresy

Veřejná síť je `sumuww`, interní alias `dora`. Ověřte níže uvedený hash genesis. Nativní adresy používají witness v0 P2WPKH a HASH160 komprimovaného veřejného klíče secp256k1. Memo ani tag nejsou povinné. Odmítněte cizí síť a chybný kontrolní součet. Zaznamenejte HD větev příjmu/vratky a index; nepředpokládejte derivační cestu Bitcoinu.

## Částky a dostupné výstupy

`_units` jsou celé nejmenší jednotky, `_smw` řetězec s 8 desetinnými místy, `_dora` kompatibilní alias. Částkové pole `_sumuww` neexistuje. 1 SMW = 100000000 jednotek. `gettxout` nemá `spendable` a může vrátit nezralé coinbase výstupy. Pro utracení v příštím bloku je nutných alespoň 100 potvrzení. Filtrujte `listunspent` přes `spendable`; available v `getaddressbalance` vynechává nezralé prostředky a čekající útraty. Nové výstupy mempoolu nejsou potvrzené. Kontrolujte vrchol mezi stránkami a znovu ověřte vybrané vstupy.

1 SMW = 100 000 000 yugeon. Automatické poplatky nabízejí tři úrovně podle místních pozorování, bez záruky času potvrzení. Sazbu v yugeon/vB lze zadat ručně. Před odesláním ověřte konečný poplatek a součet v SMW. Odmítnutá transakce nesníží zůstatek.

U jednoho vstupu v hodnotě 1 SMW závisí poplatek na tom, zda je potřeba vrátit drobné. Pokud jsou vstup i všechny výstupy typu P2WPKH, při sazbě 1 yugeon/vB stojí odeslání 0.99999890 SMW přesně 110 yugeon a nic nezbývá. Při odeslání 0.8 SMW ze stejného vstupu přibude výstup pro vrácení zbytku a poplatek činí 141 yugeon. Peněženka vrátí zbytek, pokud částka po odečtení poplatku dosáhne minima, které zohledňuje náklady na její pozdější utracení. Menší zbytek se započítá do poplatku zobrazeného před potvrzením. Při odhadu velikosti nativního vstupu SegWit (P2WPKH) peněženka počítá s nejvýše 71 bajty na podpis včetně typu hashe.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Automatický poplatek zohledňuje objem čekajících dat, kapacitu bloků a prioritu transakcí. Poplatky z minulých bloků nepoužívá. Při malé frontě platí minimální sazba. Náhled se aktualizuje; konečné potvrzení poplatek zafixuje. Pozorování se týká připojeného místního uzlu, nikoli všech uzlů.

Historie nahrazení zaznamenaná tímto uzlem zůstává zachována po restartu peněženky. Odstraněné transakce nemění zůstatek.

Historie těžby zobrazuje zvlášť novou emisi, poplatky a celkovou odměnu každého bloku. Částka přijatá vaší peněženkou je uvedena samostatně. Při částečném vyzvednutí se rozdělení mezi složkami nepředpokládá. Uzel poskytuje 28 metod RPC včetně odhadu poplatků a ověřuje a předává podepsané transakce.

## Vyhledání transakcí a bloků

`getrawtransaction` prohledává aktivní řetězec a mempool, nikoli výhradně osiřelé transakce. Vstupy určují předchozí výstupy, ne jednoznačného odesílatele. `getblock` používá logické `verbose`; uložené neaktivní bloky mají `active=false`, `confirmations=-1`. Surové transakce zůstávají dostupné přes hash bloku. `findspendingtransaction` hledá pouze potvrzené aktivní útraty; null nedokazuje dostupnost. Zkontrolujte `gettxout` s `include_mempool=true`. Potvrzení a aktivní stav se mohou při reorganizaci změnit.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Poplatky, zkontrolovaná transakce a kompatibilita

Poplatek je součet vstupů minus součet výstupů. Odhad zahrnuje výstup vrácené částky jen tehdy, když peněženka skutečně vytvoří dostatečnou vratku. Zbytek pod prahem peněženky se připočte k poplatku; výsledný poplatek a celková odepsaná částka se zobrazí ke kontrole. Sazba se udává v yugeon/vB. Virtuální velikost je váha transakce dělená čtyřmi, zaokrouhlená nahoru.

Peněženka vybere vstupy a výstupy jednou a podepíše stejný plán transakce. Po potvrzení odešle uloženou podepsanou transakci, aniž ji sestavuje znovu nebo přepočítává poplatek. Vypršelý odhad nebo mezitím utracené vstupy vyžadují novou kontrolu. Přijetí do místní fronty není potvrzením v bloku.

Pro běžné platby P2WPKH vytváří peněženka podpisy low-R a low-S dlouhé nejvýše 71 bajtů včetně bajtu SIGHASH_ALL. Jde o pravidlo podepisování a odhadu velikosti, nikoli nový limit konsensu pro jiné platné podpisy. Kratší podpis může snížit skutečnou virtuální velikost. 

## Kompatibilita podpisu Android

Formát souborů peněženky, adresy ani stávající mince se nezměnily. Dosavadní zašifrovanou zálohu lze obnovit v nové aplikaci a dál používat stejnou peněženku. Uzel Android 0.6.103 a peněženka 1.1.14 používají nový klíč pro podepisování vydání. Nemohou nahradit instalaci podepsanou jiným klíčem. Původní aplikaci a její data uchovejte, dokud nemáte zašifrovanou zálohu peněženky a funkční způsob obnovy. Původní aplikaci neodinstalovávejte jen kvůli vynucení instalace aktualizace.

<!-- /payment-policy-20261116 -->

Po přijetí platné odpovědi s verzí dá uzel protistraně čas na odeslání potvrzení. Pokud dvě odchozí spojení vedou ke stejnému uzlu, zůstane dostupná cesta otevřená, dokud přes jedno z nich neskončí synchronizace. 
