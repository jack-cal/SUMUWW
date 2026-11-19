# SUMUWW · Dokumentace

U jednoho vstupu v hodnotě 1 SMW závisí poplatek na tom, zda je potřeba vrátit drobné. Pokud jsou vstup i všechny výstupy typu P2WPKH, při sazbě 1 yugeon/vB stojí odeslání 0.99999890 SMW přesně 110 yugeon a nic nezbývá. Při odeslání 0.8 SMW ze stejného vstupu přibude výstup pro vrácení zbytku a poplatek činí 141 yugeon. Peněženka vrátí zbytek, pokud částka po odečtení poplatku dosáhne minima, které zohledňuje náklady na její pozdější utracení. Menší zbytek se započítá do poplatku zobrazeného před potvrzením. Při odhadu velikosti nativního vstupu SegWit (P2WPKH) peněženka počítá s nejvýše 71 bajty na podpis včetně typu hashe.

SUMUWW PC 0.57.51 · Uzel ověřuje, ukládá, předává a zpřístupňuje data řetězce.

## Formát podpisu

Volitelné SDK ve zdrojích sestavuje transakce a ověřuje dodané podpisy bez klíčů a sítě. Není to podepisovací program ani příkaz uzlu. Omezení P2WPKH platí pro formát příkladu, nikoli pro uzel. Dosavadní osobní peněženka zůstává dostupná.

## RPC a HTTP API

validateaddress kontroluje kontrolní součet a zvolenou síť. decoded_only z decoderawtransaction znamená pouze rozbor, nikoli platnost podpisu či potvrzení. OP_RETURN uchovává data pro externí programy. Uzel přidává dotazy na poplatky, kontrolu před odesláním, stav náhrady RBF a čtení dat v pořadí bloků. Náhrada se ověří před odstraněním čekajících transakcí. Vícenásobné podpisy a uzamčené výstupy jsou implementovány pro oddělené testy aktivace; ve veřejné síti zatím nejsou aktivní.

## Ověření

Po instalaci závislostí spusťte ze zdrojů python examples/node_contract.py. Veřejné testovací klíče a dočasný regtest ověřují odeslání, odmítnutí, potvrzení, reorganizaci a uchování dat. Nepoužívají se skutečné prostředky, uživatelské profily ani hardwarové podepisovače.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Rozhraní uzlu](EXCHANGE_INTEGRATION.html) · [RPC a HTTP API](RPC_API.html) · [Provoz uzlu](NETWORK_RUNBOOK.html) · [Poznámky k vydání](RELEASE_NOTES.html) · [Ověření](EXCHANGE_EXAMPLES.html)

[Podrobná anglická reference](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Poplatky, zkontrolovaná transakce a kompatibilita

Poplatek je součet vstupů minus součet výstupů. Odhad zahrnuje výstup vrácené částky jen tehdy, když peněženka skutečně vytvoří dostatečnou vratku. Zbytek pod prahem peněženky se připočte k poplatku; výsledný poplatek a celková odepsaná částka se zobrazí ke kontrole. Sazba se udává v yugeon/vB. Virtuální velikost je váha transakce dělená čtyřmi, zaokrouhlená nahoru.

Peněženka vybere vstupy a výstupy jednou a podepíše stejný plán transakce. Po potvrzení odešle uloženou podepsanou transakci, aniž ji sestavuje znovu nebo přepočítává poplatek. Vypršelý odhad nebo mezitím utracené vstupy vyžadují novou kontrolu. Přijetí do místní fronty není potvrzením v bloku.

Pro běžné platby P2WPKH vytváří peněženka podpisy low-R a low-S dlouhé nejvýše 71 bajtů včetně bajtu SIGHASH_ALL. Jde o pravidlo podepisování a odhadu velikosti, nikoli nový limit konsensu pro jiné platné podpisy. Kratší podpis může snížit skutečnou virtuální velikost. 

<!-- /payment-policy-20261116 -->
