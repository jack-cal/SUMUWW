# SUMUWW Android 0.6.99 · Informacje o wersji

Po ponownym uruchomieniu węzeł wznawia pracę od ostatniego bloku, który sam zweryfikował, i sprawdza nowe bloki. Jeśli zapis weryfikacji zaginął lub jest niespójny, węzeł ponownie sprawdza zapisaną historię.

SUMUWW Android 0.6.99 · Węzeł weryfikuje, przechowuje, przekazuje i udostępnia dane łańcucha.

Specyfikacja API opisuje wbudowany rdzeń węzła. Aplikacja Android nie ma ekranu konfiguracji RPC.

## API RPC i HTTP

validateaddress sprawdza sumę kontrolną i wybraną sieć. decoded_only z decoderawtransaction oznacza jedynie odczyt struktury, nie ważność podpisu ani potwierdzenie. OP_RETURN zachowuje dane dla programów zewnętrznych. Węzeł udostępnia zapytania o opłaty, kontrolę przed wysłaniem, stan zastąpienia RBF oraz dane w kolejności bloków. Transakcja zastępująca jest sprawdzana przed usunięciem oczekujących transakcji. Wielopodpis i blokady wyjść są zaimplementowane do izolowanych testów aktywacji; nie są jeszcze aktywne w sieci publicznej.

[API_CONTRACT.json](../../../API_CONTRACT.json)
