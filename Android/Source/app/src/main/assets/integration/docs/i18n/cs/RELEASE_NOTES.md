# SUMUWW Android 0.6.103 · Poznámky k vydání

U jednoho vstupu v hodnotě 1 SMW závisí poplatek na tom, zda je potřeba vrátit drobné. Pokud jsou vstup i všechny výstupy typu P2WPKH, při sazbě 1 yugeon/vB stojí odeslání 0.99999890 SMW přesně 110 yugeon a nic nezbývá. Při odeslání 0.8 SMW ze stejného vstupu přibude výstup pro vrácení zbytku a poplatek činí 141 yugeon. Peněženka vrátí zbytek, pokud částka po odečtení poplatku dosáhne minima, které zohledňuje náklady na její pozdější utracení. Menší zbytek se započítá do poplatku zobrazeného před potvrzením. Při odhadu velikosti nativního vstupu SegWit (P2WPKH) peněženka počítá s nejvýše 71 bajty na podpis včetně typu hashe.


Po restartu uzel naváže na poslední blok, který sám ověřil, a ověřuje nové bloky. Pokud uložený záznam o ověření chybí nebo nesouhlasí, znovu ověří uloženou historii.

SUMUWW Android 0.6.103 · Uzel ověřuje, ukládá, předává a zpřístupňuje data řetězce.

Specifikace API popisuje vestavěné jádro uzlu. Aplikace Android nemá obrazovku nastavení RPC.

## RPC a HTTP API

validateaddress kontroluje kontrolní součet a zvolenou síť. decoded_only z decoderawtransaction znamená pouze rozbor, nikoli platnost podpisu či potvrzení. OP_RETURN uchovává data pro externí programy. Uzel přidává dotazy na poplatky, kontrolu před odesláním, stav náhrady RBF a čtení dat v pořadí bloků. Náhrada se ověří před odstraněním čekajících transakcí. Vícenásobné podpisy a uzamčené výstupy jsou implementovány pro oddělené testy aktivace; ve veřejné síti zatím nejsou aktivní.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Poplatky, zkontrolovaná transakce a kompatibilita

Poplatek je součet vstupů minus součet výstupů. Odhad zahrnuje výstup vrácené částky jen tehdy, když peněženka skutečně vytvoří dostatečnou vratku. Zbytek pod prahem peněženky se připočte k poplatku; výsledný poplatek a celková odepsaná částka se zobrazí ke kontrole. Sazba se udává v yugeon/vB. Virtuální velikost je váha transakce dělená čtyřmi, zaokrouhlená nahoru.

Peněženka vybere vstupy a výstupy jednou a podepíše stejný plán transakce. Po potvrzení odešle uloženou podepsanou transakci, aniž ji sestavuje znovu nebo přepočítává poplatek. Vypršelý odhad nebo mezitím utracené vstupy vyžadují novou kontrolu. Přijetí do místní fronty není potvrzením v bloku.

Pro běžné platby P2WPKH vytváří peněženka podpisy low-R a low-S dlouhé nejvýše 71 bajtů včetně bajtu SIGHASH_ALL. Jde o pravidlo podepisování a odhadu velikosti, nikoli nový limit konsensu pro jiné platné podpisy. Kratší podpis může snížit skutečnou virtuální velikost. Navrhované sazby stále vycházejí z místní fronty; podobný výpočet velikosti jako u Bitcoin neznamená převzetí sazeb jeho sítě.

## Kompatibilita podpisu Android

Formát souborů peněženky, adresy ani stávající mince se nezměnily. Dosavadní zašifrovanou zálohu lze obnovit v nové aplikaci a dál používat stejnou peněženku. Uzel Android 0.6.103 a peněženka 1.1.14 používají nový klíč pro podepisování vydání. Nemohou nahradit instalaci podepsanou jiným klíčem. Původní aplikaci a její data uchovejte, dokud nemáte zašifrovanou zálohu peněženky a funkční způsob obnovy. Původní aplikaci neodinstalovávejte jen kvůli vynucení instalace aktualizace.

<!-- /payment-policy-20261116 -->
