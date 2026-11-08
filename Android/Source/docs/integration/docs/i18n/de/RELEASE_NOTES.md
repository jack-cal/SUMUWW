# SUMUWW Android 0.6.99 · Versionshinweise

Nach dem Neustart setzt der Knoten beim letzten lokal geprüften Block an und prüft neue Blöcke. Fehlt der gespeicherte Prüfnachweis oder ist er widersprüchlich, prüft der Knoten den gespeicherten Verlauf erneut.

SUMUWW Android 0.6.99 · Der Knoten prüft, speichert, verbreitet und liefert Kettendaten.

Die API-Spezifikation beschreibt den eingebetteten Knotenkern. Die Android-App hat keinen Bildschirm zur RPC-Konfiguration.

## RPC- und HTTP-API

validateaddress prüft Prüfsumme und gewähltes Netzwerk. decoderawtransaction liefert decoded_only, keine Aussage über Signaturgültigkeit oder Bestätigung. OP_RETURN-Ausgänge speichern Daten für externe Programme. Der Knoten ergänzt Gebührenabfragen, Prüfungen vor dem Senden, den RBF-Ersetzungsstatus und geordnete Blockdaten. Erst nach erfolgreicher Prüfung werden ersetzte ausstehende Transaktionen entfernt. Mehrfachsignaturen und gesperrte Ausgänge sind für isolierte Aktivierungstests implementiert und im öffentlichen Netz noch nicht aktiviert.

[API_CONTRACT.json](../../../API_CONTRACT.json)
