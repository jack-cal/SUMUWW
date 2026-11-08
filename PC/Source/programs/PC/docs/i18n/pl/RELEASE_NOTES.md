# SUMUWW · Informacje o wersji

Węzeł zwykle otwiera 10 połączeń wychodzących. Większość przekazuje bloki i transakcje. Sprawdzone połączenie zapasowe może przekazywać bloki. Węzeł może też na krótko otworzyć jedenaste połączenie, aby znaleźć inne węzły. Łączny limit wynosi 125. Połączeń przychodzących może być do 117, a przy 10 wychodzących do 115. Aplikacja komputerowa pokazuje teraz tylko łączną liczbę połączonych węzłów. Każde urządzenie wydobywcze tworzy własne bloki. Węzeł na komputerze rozsyła gotowe bloki i odrzuca prośby telefonu o zadania wydobywcze oraz przesyłane rozwiązania.

Po ponownym uruchomieniu węzeł wznawia pracę od ostatniego bloku, który sam zweryfikował, i sprawdza nowe bloki. Jeśli zapis weryfikacji zaginął lub jest niespójny, węzeł ponownie sprawdza zapisaną historię.


SUMUWW PC 0.57.54 · Węzeł weryfikuje, przechowuje, przekazuje i udostępnia dane łańcucha.

## Format podpisu

Opcjonalny SDK w źródłach składa transakcje i weryfikuje otrzymane podpisy bez kluczy i sieci. Nie jest programem podpisującym ani poleceniem węzła. Ograniczenie P2WPKH dotyczy formatu przykładu, nie węzła. Dotychczasowy portfel osobisty pozostaje dostępny.

## API RPC i HTTP

validateaddress sprawdza sumę kontrolną i wybraną sieć. decoded_only z decoderawtransaction oznacza jedynie odczyt struktury, nie ważność podpisu ani potwierdzenie. OP_RETURN zachowuje dane dla programów zewnętrznych. Węzeł udostępnia zapytania o opłaty, kontrolę przed wysłaniem, stan zastąpienia RBF oraz dane w kolejności bloków. Transakcja zastępująca jest sprawdzana przed usunięciem oczekujących transakcji. Wielopodpis i blokady wyjść są zaimplementowane do izolowanych testów aktywacji; nie są jeszcze aktywne w sieci publicznej.

## Weryfikacja

Po instalacji zależności uruchom python examples/node_contract.py ze źródeł. Jawne klucze testowe i tymczasowy regtest sprawdzają wysyłanie, odrzucanie, potwierdzenia, reorganizację i trwałość danych. Nie używamy rzeczywistych środków, profili użytkowników ani urządzeń podpisujących.

[Dokumentacja](README.html) · [Interfejs węzła](EXCHANGE_INTEGRATION.html) · [API RPC i HTTP](RPC_API.html) · [Obsługa węzła](NETWORK_RUNBOOK.html) · [Weryfikacja](EXCHANGE_EXAMPLES.html)

[Rozszerzona dokumentacja angielska](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
