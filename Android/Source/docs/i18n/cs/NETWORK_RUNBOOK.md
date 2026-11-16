# SUMUWW Android 0.6.103 · Provoz uzlu

Po restartu uzel naváže na poslední blok, který sám ověřil, a ověřuje nové bloky. Pokud uložený záznam o ověření chybí nebo nesouhlasí, znovu ověří uloženou historii.

SUMUWW Android 0.6.103 · Uzel ověřuje, ukládá, předává a zpřístupňuje data řetězce.

[Dokumentace](../../integration/docs/i18n/cs/NETWORK_RUNBOOK.html)

<!-- payment-policy-20261116 -->

## Poplatky, zkontrolovaná transakce a kompatibilita

Poplatek je součet vstupů minus součet výstupů. Odhad zahrnuje výstup vrácené částky jen tehdy, když peněženka skutečně vytvoří dostatečnou vratku. Zbytek pod prahem peněženky se připočte k poplatku; výsledný poplatek a celková odepsaná částka se zobrazí ke kontrole. Sazba se udává v yugeon/vB. Virtuální velikost je váha transakce dělená čtyřmi, zaokrouhlená nahoru.

Peněženka vybere vstupy a výstupy jednou a podepíše stejný plán transakce. Po potvrzení odešle uloženou podepsanou transakci, aniž ji sestavuje znovu nebo přepočítává poplatek. Vypršelý odhad nebo mezitím utracené vstupy vyžadují novou kontrolu. Přijetí do místní fronty není potvrzením v bloku.

Pro běžné platby P2WPKH vytváří peněženka podpisy low-R a low-S dlouhé nejvýše 71 bajtů včetně bajtu SIGHASH_ALL. Jde o pravidlo podepisování a odhadu velikosti, nikoli nový limit konsensu pro jiné platné podpisy. Kratší podpis může snížit skutečnou virtuální velikost. Navrhované sazby stále vycházejí z místní fronty; podobný výpočet velikosti jako u Bitcoin neznamená převzetí sazeb jeho sítě.

## Kompatibilita podpisu Android

Formát souborů peněženky, adresy ani stávající mince se nezměnily. Dosavadní zašifrovanou zálohu lze obnovit v nové aplikaci a dál používat stejnou peněženku. Uzel Android 0.6.103 a peněženka 1.1.14 používají nový klíč pro podepisování vydání. Nemohou nahradit instalaci podepsanou jiným klíčem. Původní aplikaci a její data uchovejte, dokud nemáte zašifrovanou zálohu peněženky a funkční způsob obnovy. Původní aplikaci neodinstalovávejte jen kvůli vynucení instalace aktualizace.

<!-- /payment-policy-20261116 -->

Po přijetí platné odpovědi s verzí dá uzel protistraně čas na odeslání potvrzení. Pokud dvě odchozí spojení vedou ke stejnému uzlu, zůstane dostupná cesta otevřená, dokud přes jedno z nich neskončí synchronizace. Vestavěná diagnostika přijme blok s platným důkazem práce ještě před doručením důkazu o spojení. Poté ověří podpisy tří svědků, předání důkazu dalšímu uzlu a jeho zachování po restartu.
