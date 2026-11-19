# SUMUWW Wallet Android 1.1.14

Węzeł zwykle otwiera 10 połączeń wychodzących. Większość przekazuje bloki i transakcje. Sprawdzone połączenie zapasowe może przekazywać bloki. Węzeł może też na krótko otworzyć jedenaste połączenie, aby znaleźć inne węzły. Łączny limit wynosi 125. Połączeń przychodzących może być do 117, a przy 10 wychodzących do 115. Naprawiono błąd uruchamiania portfela na Androidzie. Portfel wykrywa zmiany połączenia sieciowego telefonu.

1 SMW = 100 000 000 yugeon. Opłaty automatyczne oferują trzy poziomy na podstawie lokalnych obserwacji, bez gwarancji czasu potwierdzenia. Możesz wpisać stawkę w yugeon/vB. Przed wysłaniem sprawdź końcową opłatę i sumę w SMW. Odrzucona transakcja nie zmniejsza salda.

Przy jednym wejściu o wartości 1 SMW opłata zależy od tego, czy trzeba wydać resztę. Jeśli wejście i wszystkie wyjścia są typu P2WPKH, przy stawce 1 yugeon/vB wysłanie 0.99999890 SMW kosztuje 110 yugeon i nie pozostawia reszty. Wysłanie 0.8 SMW z tego samego wejścia wymaga dodatkowego wyjścia na resztę i zwiększa opłatę do 141 yugeon. Portfel zwraca resztę, jeśli po odjęciu opłaty pozostała kwota osiąga próg uwzględniający koszt jej późniejszego wydania. Gdy kwota jest mniejsza, wchodzi w skład opłaty wyświetlanej przed zatwierdzeniem. Dla wejścia portfela w formacie natywnego SegWit (P2WPKH) szacunek przewiduje do 71 bajtów na podpis wraz z typem skrótu.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Opłata automatyczna uwzględnia ilość oczekujących danych, pojemność bloków i priorytet transakcji. Nie używa opłat z wcześniejszych bloków. Przy małej kolejce obowiązuje stawka minimalna. Podgląd jest odświeżany; końcowe potwierdzenie ustala opłatę. Obserwacje dotyczą połączonego lokalnego węzła, nie wszystkich węzłów.

Historia zastąpień zarejestrowanych przez ten węzeł pozostaje dostępna po ponownym uruchomieniu portfela. Usunięte transakcje nie wpływają na saldo.

Historia wydobycia pokazuje osobno nową emisję, opłaty i łączną nagrodę każdego bloku. Kwota otrzymana przez portfel jest wyświetlana oddzielnie. Przy częściowym odebraniu nagrody nie zakłada się podziału jej składników. Węzeł udostępnia 28 metod RPC, w tym szacowanie opłat, oraz weryfikuje i rozsyła podpisane transakcje.

<!-- payment-policy-20261116 -->

## Opłaty, sprawdzona transakcja i zgodność

Opłata to suma wejść pomniejszona o sumę wyjść. Oszacowanie uwzględnia wyjście reszty tylko wtedy, gdy portfel rzeczywiście tworzy resztę spełniającą jego próg. Pozostała kwota poniżej tego progu jest doliczana do opłaty; wynikowa opłata i łączne obciążenie są wyświetlane do sprawdzenia. Stawkę podaje się w yugeon/vB. Rozmiar wirtualny to waga transakcji podzielona przez cztery i zaokrąglona w górę.

Portfel wybiera wejścia i wyjścia jeden raz, a następnie podpisuje ten sam plan transakcji. Potwierdzenie wysyła zapisaną podpisaną transakcję, bez jej ponownego tworzenia i przeliczania opłaty. Wygaśnięcie wyceny lub wcześniejsze wydanie wejścia wymaga ponownego sprawdzenia. Przyjęcie do lokalnej kolejki nie oznacza potwierdzenia w bloku.

Przy zwykłych płatnościach P2WPKH portfel tworzy podpisy low-R i low-S o długości do 71 bajtów, łącznie z bajtem SIGHASH_ALL. Jest to polityka podpisywania i szacowania rozmiaru, a nie nowy limit konsensusu dla pozostałych prawidłowych podpisów. Krótszy podpis może zmniejszyć rzeczywisty rozmiar wirtualny. 

## Zgodność podpisów Android

Format plików portfela, adresy i istniejące monety nie zmieniły się. Dotychczasową zaszyfrowaną kopię można przywrócić w nowej aplikacji i nadal używać tego samego portfela. Węzeł Android 0.6.103 i portfel 1.1.14 korzystają z nowego klucza podpisywania wydań. Nie zastąpią instalacji podpisanej innym kluczem. Zachowaj starą aplikację i jej dane do czasu uzyskania zaszyfrowanej kopii portfela i działającego sposobu odzyskiwania. Nie odinstalowuj starej aplikacji tylko po to, by wymusić instalację aktualizacji.

<!-- /payment-policy-20261116 -->

Po otrzymaniu poprawnej odpowiedzi z wersją węzeł daje drugiej stronie czas na przesłanie potwierdzenia. Jeśli dwa połączenia wychodzące prowadzą do tego samego węzła, dostępna ścieżka pozostaje otwarta do zakończenia synchronizacji przez jedno z nich. 
