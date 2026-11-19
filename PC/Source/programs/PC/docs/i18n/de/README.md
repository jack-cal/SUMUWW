# SUMUWW · Dokumentation

SUMUWW PC 0.57.51 · Der Knoten prüft, speichert, verbreitet und liefert Kettendaten.

## Signaturformat

Das optionale Quellcode-SDK erstellt Transaktionen und prüft übergebene Signaturen ohne Schlüssel oder Netzwerk. Es ist weder Signierprogramm noch Knotenbefehl. Die P2WPKH-Beschränkung gilt für das Beispielformat, nicht den Knoten. Die bisherige persönliche Wallet bleibt verfügbar.

## RPC- und HTTP-API

validateaddress prüft Prüfsumme und gewähltes Netzwerk. decoderawtransaction liefert decoded_only, keine Aussage über Signaturgültigkeit oder Bestätigung. OP_RETURN-Ausgänge speichern Daten für externe Programme. Der Knoten ergänzt Gebührenabfragen, Prüfungen vor dem Senden, den RBF-Ersetzungsstatus und geordnete Blockdaten. Erst nach erfolgreicher Prüfung werden ersetzte ausstehende Transaktionen entfernt. Mehrfachsignaturen und gesperrte Ausgänge sind für isolierte Aktivierungstests implementiert und im öffentlichen Netz noch nicht aktiviert.

## Prüfung

Installieren Sie die Abhängigkeiten und führen Sie python examples/node_contract.py im Quellcode aus. Öffentliche Testschlüssel und temporäres Regtest prüfen Übermittlung, Ablehnung, Bestätigungen, Reorganisation und Datenerhalt. Echte Guthaben, Benutzerprofile und Hardware-Signierer werden nicht verwendet.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Knotenschnittstelle](EXCHANGE_INTEGRATION.html) · [RPC- und HTTP-API](RPC_API.html) · [Node-Betrieb](NETWORK_RUNBOOK.html) · [Versionshinweise](RELEASE_NOTES.html) · [Prüfung](EXCHANGE_EXAMPLES.html)

[Ausführliche englische Referenz](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Gebühren, geprüfte Transaktion und Kompatibilität

Die Gebühr ist die Summe der Eingänge abzüglich der Summe der Ausgänge. Ein Wechselgeldausgang wird nur dann geschätzt, wenn die Wallet tatsächlich ausreichend Wechselgeld erzeugt. Ein Rest unterhalb der Wallet-Schwelle wird der Gebühr zugeschlagen; die resultierende Gebühr und die gesamte Belastung erscheinen zur Prüfung. Der Gebührensatz wird in yugeon/vB angegeben. Die virtuelle Größe entspricht dem Transaktionsgewicht geteilt durch vier, aufgerundet auf eine ganze Zahl.

Die Wallet wählt Eingänge und Ausgänge genau einmal und signiert diesen Transaktionsplan. Beim Bestätigen wird die gespeicherte signierte Transaktion eingereicht, ohne sie neu aufzubauen oder die Gebühr neu zu berechnen. Ein abgelaufenes Angebot oder inzwischen ausgegebene Eingänge erfordern eine erneute Prüfung. Die Aufnahme in die lokale Warteschlange ist noch keine Bestätigung in einem Block.

Bei gewöhnlichen P2WPKH-Zahlungen erzeugt die Wallet Low-R-/Low-S-Signaturen mit höchstens 71 Byte einschließlich des SIGHASH_ALL-Bytes. Das ist eine Signatur- und Schätzrichtlinie, keine neue Konsensgrenze für andere gültige Signaturen. Kürzere Signaturen können die tatsächliche virtuelle Größe verringern. 

<!-- /payment-policy-20261116 -->
