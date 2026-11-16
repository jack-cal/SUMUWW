# SUMUWW · Dokumentacja

SUMUWW PC 0.57.51 · Węzeł weryfikuje, przechowuje, przekazuje i udostępnia dane łańcucha.

## Format podpisu

Opcjonalny SDK w źródłach składa transakcje i weryfikuje otrzymane podpisy bez kluczy i sieci. Nie jest programem podpisującym ani poleceniem węzła. Ograniczenie P2WPKH dotyczy formatu przykładu, nie węzła. Dotychczasowy portfel osobisty pozostaje dostępny.

## API RPC i HTTP

validateaddress sprawdza sumę kontrolną i wybraną sieć. decoded_only z decoderawtransaction oznacza jedynie odczyt struktury, nie ważność podpisu ani potwierdzenie. OP_RETURN zachowuje dane dla programów zewnętrznych. Węzeł udostępnia zapytania o opłaty, kontrolę przed wysłaniem, stan zastąpienia RBF oraz dane w kolejności bloków. Transakcja zastępująca jest sprawdzana przed usunięciem oczekujących transakcji. Wielopodpis i blokady wyjść są zaimplementowane do izolowanych testów aktywacji; nie są jeszcze aktywne w sieci publicznej.

## Weryfikacja

Po instalacji zależności uruchom python examples/node_contract.py ze źródeł. Jawne klucze testowe i tymczasowy regtest sprawdzają wysyłanie, odrzucanie, potwierdzenia, reorganizację i trwałość danych. Nie używamy rzeczywistych środków, profili użytkowników ani urządzeń podpisujących.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Interfejs węzła](EXCHANGE_INTEGRATION.html) · [API RPC i HTTP](RPC_API.html) · [Obsługa węzła](NETWORK_RUNBOOK.html) · [Informacje o wersji](RELEASE_NOTES.html) · [Weryfikacja](EXCHANGE_EXAMPLES.html)

[Rozszerzona dokumentacja angielska](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Opłaty, sprawdzona transakcja i zgodność

Opłata to suma wejść pomniejszona o sumę wyjść. Oszacowanie uwzględnia wyjście reszty tylko wtedy, gdy portfel rzeczywiście tworzy resztę spełniającą jego próg. Pozostała kwota poniżej tego progu jest doliczana do opłaty; wynikowa opłata i łączne obciążenie są wyświetlane do sprawdzenia. Stawkę podaje się w yugeon/vB. Rozmiar wirtualny to waga transakcji podzielona przez cztery i zaokrąglona w górę.

Portfel wybiera wejścia i wyjścia jeden raz, a następnie podpisuje ten sam plan transakcji. Potwierdzenie wysyła zapisaną podpisaną transakcję, bez jej ponownego tworzenia i przeliczania opłaty. Wygaśnięcie wyceny lub wcześniejsze wydanie wejścia wymaga ponownego sprawdzenia. Przyjęcie do lokalnej kolejki nie oznacza potwierdzenia w bloku.

Przy zwykłych płatnościach P2WPKH portfel tworzy podpisy low-R i low-S o długości do 71 bajtów, łącznie z bajtem SIGHASH_ALL. Jest to polityka podpisywania i szacowania rozmiaru, a nie nowy limit konsensusu dla pozostałych prawidłowych podpisów. Krótszy podpis może zmniejszyć rzeczywisty rozmiar wirtualny. Sugerowane stawki nadal wynikają z lokalnej kolejki; podobny do Bitcoin sposób liczenia rozmiaru nie oznacza stosowania stawek sieci Bitcoin.

## Składnik I2P dla Windows i kontrola bezpieczeństwa

Pakiety Windows zawierają oficjalny i2pd 3.0.0 z aktualnymi sumami kontrolnymi i certyfikatami połączenia początkowego. W zapisanej kontroli Defender nadal wykrywa oficjalny plik wykonywalny I2P i oryginalny ZIP. Zgodność oficjalnego skrótu nie dowodzi bezpieczeństwa ani fałszywego alarmu. Lokalne wykluczenie pliku działa tylko na komputerze, na którym je ustawiono; pakiet publiczny go nie dodaje. Inne komputery mogą zablokować te same pliki.

<!-- /payment-policy-20261116 -->
