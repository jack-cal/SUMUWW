# Opłaty, sprawdzona transakcja i zgodność

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Opłaty, sprawdzona transakcja i zgodność

Opłata to suma wejść pomniejszona o sumę wyjść. Oszacowanie uwzględnia wyjście reszty tylko wtedy, gdy portfel rzeczywiście tworzy resztę spełniającą jego próg. Pozostała kwota poniżej tego progu jest doliczana do opłaty; wynikowa opłata i łączne obciążenie są wyświetlane do sprawdzenia. Stawkę podaje się w yugeon/vB. Rozmiar wirtualny to waga transakcji podzielona przez cztery i zaokrąglona w górę.

Portfel wybiera wejścia i wyjścia jeden raz, a następnie podpisuje ten sam plan transakcji. Potwierdzenie wysyła zapisaną podpisaną transakcję, bez jej ponownego tworzenia i przeliczania opłaty. Wygaśnięcie wyceny lub wcześniejsze wydanie wejścia wymaga ponownego sprawdzenia. Przyjęcie do lokalnej kolejki nie oznacza potwierdzenia w bloku.

Przy zwykłych płatnościach P2WPKH portfel tworzy podpisy low-R i low-S o długości do 71 bajtów, łącznie z bajtem SIGHASH_ALL. Jest to polityka podpisywania i szacowania rozmiaru, a nie nowy limit konsensusu dla pozostałych prawidłowych podpisów. Krótszy podpis może zmniejszyć rzeczywisty rozmiar wirtualny. Sugerowane stawki nadal wynikają z lokalnej kolejki; podobny do Bitcoin sposób liczenia rozmiaru nie oznacza stosowania stawek sieci Bitcoin.

## Składnik I2P dla Windows i kontrola bezpieczeństwa

Pakiety Windows zawierają oficjalny i2pd 3.0.0 z aktualnymi sumami kontrolnymi i certyfikatami połączenia początkowego. W zapisanej kontroli Defender nadal wykrywa oficjalny plik wykonywalny I2P i oryginalny ZIP. Zgodność oficjalnego skrótu nie dowodzi bezpieczeństwa ani fałszywego alarmu. Lokalne wykluczenie pliku działa tylko na komputerze, na którym je ustawiono; pakiet publiczny go nie dodaje. Inne komputery mogą zablokować te same pliki.

## Zgodność podpisów Android

Format plików portfela, adresy i istniejące monety nie zmieniły się. Dotychczasową zaszyfrowaną kopię można przywrócić w nowej aplikacji i nadal używać tego samego portfela. Węzeł Android 0.6.102 i portfel 1.1.13 korzystają z nowego klucza podpisywania wydań. Nie zastąpią instalacji podpisanej innym kluczem. Zachowaj starą aplikację i jej dane do czasu uzyskania zaszyfrowanej kopii portfela i działającego sposobu odzyskiwania. Nie odinstalowuj starej aplikacji tylko po to, by wymusić instalację aktualizacji.

<!-- /payment-policy-20261116 -->
