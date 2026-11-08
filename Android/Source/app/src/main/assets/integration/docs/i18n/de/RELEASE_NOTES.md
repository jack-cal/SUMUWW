# SUMUWW Android 0.6.98 · Versionshinweise

Das Gerät verbindet sich mit einem SUMUWW-Vollknoten ab Version 0.57.49. Es prüft die Belohnung und berechnet den Arbeitsnachweis, ohne den gesamten Transaktionsverlauf der Blockchain herunterzuladen.

Die API-Spezifikation beschreibt den eingebetteten Knotenkern. Die Android-App hat keinen Bildschirm zur RPC-Konfiguration.

## RPC- und HTTP-API

validateaddress prüft Prüfsumme und gewähltes Netzwerk. decoderawtransaction liefert decoded_only, keine Aussage über Signaturgültigkeit oder Bestätigung. OP_RETURN-Ausgänge speichern Daten für externe Programme. Der Knoten ergänzt Gebührenabfragen, Prüfungen vor dem Senden, den RBF-Ersetzungsstatus und geordnete Blockdaten. Erst nach erfolgreicher Prüfung werden ersetzte ausstehende Transaktionen entfernt. Mehrfachsignaturen und gesperrte Ausgänge sind für isolierte Aktivierungstests implementiert und im öffentlichen Netz noch nicht aktiviert.

[API_CONTRACT.json](../../../API_CONTRACT.json)
