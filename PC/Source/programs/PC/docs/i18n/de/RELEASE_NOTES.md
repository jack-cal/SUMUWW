# SUMUWW · Versionshinweise

Bei einem Eingang von 1 SMW hängt die Gebühr davon ab, ob Wechselgeld zurückgeht. Sind alle Ein- und Ausgänge vom Typ P2WPKH, kostet eine Zahlung von 0.99999890 SMW bei 1 yugeon/vB genau 110 yugeon. Es bleibt kein Wechselgeld. Bei 0.8 SMW aus demselben Eingang kommt ein Wechselgeldausgang hinzu. Die Gebühr beträgt dann 141 yugeon. Die Wallet gibt Wechselgeld zurück, wenn der Rest nach Abzug der Gebühr einen Mindestbetrag erreicht. Dieser berücksichtigt die Kosten, die beim späteren Ausgeben des Wechselgelds anfallen. Kleinere Restbeträge fließen in die vor der Bestätigung angezeigte Gebühr ein. Bei einem nativen SegWit-Eingang (P2WPKH) rechnet die Wallet mit bis zu 71 Byte für die Signatur einschließlich des Hash-Typs.

0.57.61 · Wenn Sie bei laufender App die Sprache wechseln, ändert sich auch das Symbol in der Windows-Taskleiste.

Der Knoten baut normalerweise 10 ausgehende Verbindungen auf. Die meisten leiten Blöcke und Transaktionen weiter. Eine geprüfte Ersatzverbindung kann Blöcke weiterleiten. Zur Suche nach weiteren Knoten kann kurzzeitig eine elfte Verbindung hinzukommen. Insgesamt sind 125 Verbindungen möglich. Bei 10 ausgehenden Verbindungen sind bis zu 115 eingehende möglich, sonst höchstens 117. Die Desktop-App zeigt jetzt nur die Gesamtzahl der verbundenen Knoten an. Jedes Mining-Gerät erstellt seine eigenen Blöcke. Der PC-Knoten leitet fertige Blöcke weiter und lehnt Anfragen des Smartphones nach Mining-Aufträgen sowie eingereichte Lösungen ab.

Nach dem Neustart setzt der Knoten beim letzten lokal geprüften Block an und prüft neue Blöcke. Fehlt der gespeicherte Prüfnachweis oder ist er widersprüchlich, prüft der Knoten den gespeicherten Verlauf erneut.

SUMUWW PC 0.57.61 · Der Knoten prüft, speichert, verbreitet und liefert Kettendaten.

## Signaturformat

Das optionale Quellcode-SDK erstellt Transaktionen und prüft übergebene Signaturen ohne Schlüssel oder Netzwerk. Es ist weder Signierprogramm noch Knotenbefehl. Die P2WPKH-Beschränkung gilt für das Beispielformat, nicht den Knoten. Die bisherige persönliche Wallet bleibt verfügbar.

## RPC- und HTTP-API

validateaddress prüft Prüfsumme und gewähltes Netzwerk. decoderawtransaction liefert decoded_only, keine Aussage über Signaturgültigkeit oder Bestätigung. OP_RETURN-Ausgänge speichern Daten für externe Programme. Der Knoten ergänzt Gebührenabfragen, Prüfungen vor dem Senden, den RBF-Ersetzungsstatus und geordnete Blockdaten. Erst nach erfolgreicher Prüfung werden ersetzte ausstehende Transaktionen entfernt. Mehrfachsignaturen und gesperrte Ausgänge sind für isolierte Aktivierungstests implementiert und im öffentlichen Netz noch nicht aktiviert.

## Prüfung

Installieren Sie die Abhängigkeiten und führen Sie python examples/node_contract.py im Quellcode aus. Öffentliche Testschlüssel und temporäres Regtest prüfen Übermittlung, Ablehnung, Bestätigungen, Reorganisation und Datenerhalt. Echte Guthaben, Benutzerprofile und Hardware-Signierer werden nicht verwendet.

[Dokumentation](README.html) · [Knotenschnittstelle](EXCHANGE_INTEGRATION.html) · [RPC- und HTTP-API](RPC_API.html) · [Node-Betrieb](NETWORK_RUNBOOK.html) · [Prüfung](EXCHANGE_EXAMPLES.html)

[Ausführliche englische Referenz](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Gebühren, geprüfte Transaktion und Kompatibilität

Die Gebühr ist die Summe der Eingänge abzüglich der Summe der Ausgänge. Ein Wechselgeldausgang wird nur dann geschätzt, wenn die Wallet tatsächlich ausreichend Wechselgeld erzeugt. Ein Rest unterhalb der Wallet-Schwelle wird der Gebühr zugeschlagen; die resultierende Gebühr und die gesamte Belastung erscheinen zur Prüfung. Der Gebührensatz wird in yugeon/vB angegeben. Die virtuelle Größe entspricht dem Transaktionsgewicht geteilt durch vier, aufgerundet auf eine ganze Zahl.

Die Wallet wählt Eingänge und Ausgänge genau einmal und signiert diesen Transaktionsplan. Beim Bestätigen wird die gespeicherte signierte Transaktion eingereicht, ohne sie neu aufzubauen oder die Gebühr neu zu berechnen. Ein abgelaufenes Angebot oder inzwischen ausgegebene Eingänge erfordern eine erneute Prüfung. Die Aufnahme in die lokale Warteschlange ist noch keine Bestätigung in einem Block.

Bei gewöhnlichen P2WPKH-Zahlungen erzeugt die Wallet Low-R-/Low-S-Signaturen mit höchstens 71 Byte einschließlich des SIGHASH_ALL-Bytes. Das ist eine Signatur- und Schätzrichtlinie, keine neue Konsensgrenze für andere gültige Signaturen. Kürzere Signaturen können die tatsächliche virtuelle Größe verringern. 

<!-- /payment-policy-20261116 -->
