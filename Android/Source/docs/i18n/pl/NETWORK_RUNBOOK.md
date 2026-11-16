# SUMUWW Android 0.6.103 · Obsługa węzła

Po ponownym uruchomieniu węzeł wznawia pracę od ostatniego bloku, który sam zweryfikował, i sprawdza nowe bloki. Jeśli zapis weryfikacji zaginął lub jest niespójny, węzeł ponownie sprawdza zapisaną historię.

SUMUWW Android 0.6.103 · Węzeł weryfikuje, przechowuje, przekazuje i udostępnia dane łańcucha.

[Dokumentacja](../../integration/docs/i18n/pl/NETWORK_RUNBOOK.html)

<!-- payment-policy-20261116 -->

## Opłaty, sprawdzona transakcja i zgodność

Opłata to suma wejść pomniejszona o sumę wyjść. Oszacowanie uwzględnia wyjście reszty tylko wtedy, gdy portfel rzeczywiście tworzy resztę spełniającą jego próg. Pozostała kwota poniżej tego progu jest doliczana do opłaty; wynikowa opłata i łączne obciążenie są wyświetlane do sprawdzenia. Stawkę podaje się w yugeon/vB. Rozmiar wirtualny to waga transakcji podzielona przez cztery i zaokrąglona w górę.

Portfel wybiera wejścia i wyjścia jeden raz, a następnie podpisuje ten sam plan transakcji. Potwierdzenie wysyła zapisaną podpisaną transakcję, bez jej ponownego tworzenia i przeliczania opłaty. Wygaśnięcie wyceny lub wcześniejsze wydanie wejścia wymaga ponownego sprawdzenia. Przyjęcie do lokalnej kolejki nie oznacza potwierdzenia w bloku.

Przy zwykłych płatnościach P2WPKH portfel tworzy podpisy low-R i low-S o długości do 71 bajtów, łącznie z bajtem SIGHASH_ALL. Jest to polityka podpisywania i szacowania rozmiaru, a nie nowy limit konsensusu dla pozostałych prawidłowych podpisów. Krótszy podpis może zmniejszyć rzeczywisty rozmiar wirtualny. Sugerowane stawki nadal wynikają z lokalnej kolejki; podobny do Bitcoin sposób liczenia rozmiaru nie oznacza stosowania stawek sieci Bitcoin.

## Zgodność podpisów Android

Format plików portfela, adresy i istniejące monety nie zmieniły się. Dotychczasową zaszyfrowaną kopię można przywrócić w nowej aplikacji i nadal używać tego samego portfela. Węzeł Android 0.6.103 i portfel 1.1.14 korzystają z nowego klucza podpisywania wydań. Nie zastąpią instalacji podpisanej innym kluczem. Zachowaj starą aplikację i jej dane do czasu uzyskania zaszyfrowanej kopii portfela i działającego sposobu odzyskiwania. Nie odinstalowuj starej aplikacji tylko po to, by wymusić instalację aktualizacji.

<!-- /payment-policy-20261116 -->

Po otrzymaniu poprawnej odpowiedzi z wersją węzeł daje drugiej stronie czas na przesłanie potwierdzenia. Jeśli dwa połączenia wychodzące prowadzą do tego samego węzła, dostępna ścieżka pozostaje otwarta do zakończenia synchronizacji przez jedno z nich. Wbudowana diagnostyka przyjmuje blok z prawidłowym dowodem pracy, zanim otrzyma dowód połączenia. Następnie sprawdza podpisy trzech świadków, przekazanie dowodu połączenia innemu węzłowi i zachowanie go po ponownym uruchomieniu.
