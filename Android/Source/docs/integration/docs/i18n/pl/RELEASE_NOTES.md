# SUMUWW Android 0.6.103 · Informacje o wersji

Przy jednym wejściu o wartości 1 SMW opłata zależy od tego, czy trzeba wydać resztę. Jeśli wejście i wszystkie wyjścia są typu P2WPKH, przy stawce 1 yugeon/vB wysłanie 0.99999890 SMW kosztuje 110 yugeon i nie pozostawia reszty. Wysłanie 0.8 SMW z tego samego wejścia wymaga dodatkowego wyjścia na resztę i zwiększa opłatę do 141 yugeon. Portfel zwraca resztę, jeśli po odjęciu opłaty pozostała kwota osiąga próg uwzględniający koszt jej późniejszego wydania. Gdy kwota jest mniejsza, wchodzi w skład opłaty wyświetlanej przed zatwierdzeniem. Dla wejścia portfela w formacie natywnego SegWit (P2WPKH) szacunek przewiduje do 71 bajtów na podpis wraz z typem skrótu.


Po ponownym uruchomieniu węzeł wznawia pracę od ostatniego bloku, który sam zweryfikował, i sprawdza nowe bloki. Jeśli zapis weryfikacji zaginął lub jest niespójny, węzeł ponownie sprawdza zapisaną historię.

SUMUWW Android 0.6.103 · Węzeł weryfikuje, przechowuje, przekazuje i udostępnia dane łańcucha.

Specyfikacja API opisuje wbudowany rdzeń węzła. Aplikacja Android nie ma ekranu konfiguracji RPC.

## API RPC i HTTP

validateaddress sprawdza sumę kontrolną i wybraną sieć. decoded_only z decoderawtransaction oznacza jedynie odczyt struktury, nie ważność podpisu ani potwierdzenie. OP_RETURN zachowuje dane dla programów zewnętrznych. Węzeł udostępnia zapytania o opłaty, kontrolę przed wysłaniem, stan zastąpienia RBF oraz dane w kolejności bloków. Transakcja zastępująca jest sprawdzana przed usunięciem oczekujących transakcji. Wielopodpis i blokady wyjść są zaimplementowane do izolowanych testów aktywacji; nie są jeszcze aktywne w sieci publicznej.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Opłaty, sprawdzona transakcja i zgodność

Opłata to suma wejść pomniejszona o sumę wyjść. Oszacowanie uwzględnia wyjście reszty tylko wtedy, gdy portfel rzeczywiście tworzy resztę spełniającą jego próg. Pozostała kwota poniżej tego progu jest doliczana do opłaty; wynikowa opłata i łączne obciążenie są wyświetlane do sprawdzenia. Stawkę podaje się w yugeon/vB. Rozmiar wirtualny to waga transakcji podzielona przez cztery i zaokrąglona w górę.

Portfel wybiera wejścia i wyjścia jeden raz, a następnie podpisuje ten sam plan transakcji. Potwierdzenie wysyła zapisaną podpisaną transakcję, bez jej ponownego tworzenia i przeliczania opłaty. Wygaśnięcie wyceny lub wcześniejsze wydanie wejścia wymaga ponownego sprawdzenia. Przyjęcie do lokalnej kolejki nie oznacza potwierdzenia w bloku.

Przy zwykłych płatnościach P2WPKH portfel tworzy podpisy low-R i low-S o długości do 71 bajtów, łącznie z bajtem SIGHASH_ALL. Jest to polityka podpisywania i szacowania rozmiaru, a nie nowy limit konsensusu dla pozostałych prawidłowych podpisów. Krótszy podpis może zmniejszyć rzeczywisty rozmiar wirtualny. Sugerowane stawki nadal wynikają z lokalnej kolejki; podobny do Bitcoin sposób liczenia rozmiaru nie oznacza stosowania stawek sieci Bitcoin.

## Zgodność podpisów Android

Format plików portfela, adresy i istniejące monety nie zmieniły się. Dotychczasową zaszyfrowaną kopię można przywrócić w nowej aplikacji i nadal używać tego samego portfela. Węzeł Android 0.6.103 i portfel 1.1.14 korzystają z nowego klucza podpisywania wydań. Nie zastąpią instalacji podpisanej innym kluczem. Zachowaj starą aplikację i jej dane do czasu uzyskania zaszyfrowanej kopii portfela i działającego sposobu odzyskiwania. Nie odinstalowuj starej aplikacji tylko po to, by wymusić instalację aktualizacji.

<!-- /payment-policy-20261116 -->
