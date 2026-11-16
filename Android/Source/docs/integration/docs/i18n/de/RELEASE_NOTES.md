# SUMUWW Android 0.6.103 · Versionshinweise

Bei einem Eingang von 1 SMW hängt die Gebühr davon ab, ob Wechselgeld zurückgeht. Sind alle Ein- und Ausgänge vom Typ P2WPKH, kostet eine Zahlung von 0.99999890 SMW bei 1 yugeon/vB genau 110 yugeon. Es bleibt kein Wechselgeld. Bei 0.8 SMW aus demselben Eingang kommt ein Wechselgeldausgang hinzu. Die Gebühr beträgt dann 141 yugeon. Die Wallet gibt Wechselgeld zurück, wenn der Rest nach Abzug der Gebühr einen Mindestbetrag erreicht. Dieser berücksichtigt die Kosten, die beim späteren Ausgeben des Wechselgelds anfallen. Kleinere Restbeträge fließen in die vor der Bestätigung angezeigte Gebühr ein. Bei einem nativen SegWit-Eingang (P2WPKH) rechnet die Wallet mit bis zu 71 Byte für die Signatur einschließlich des Hash-Typs.


Nach dem Neustart setzt der Knoten beim letzten lokal geprüften Block an und prüft neue Blöcke. Fehlt der gespeicherte Prüfnachweis oder ist er widersprüchlich, prüft der Knoten den gespeicherten Verlauf erneut.

SUMUWW Android 0.6.103 · Der Knoten prüft, speichert, verbreitet und liefert Kettendaten.

Die API-Spezifikation beschreibt den eingebetteten Knotenkern. Die Android-App hat keinen Bildschirm zur RPC-Konfiguration.

## RPC- und HTTP-API

validateaddress prüft Prüfsumme und gewähltes Netzwerk. decoderawtransaction liefert decoded_only, keine Aussage über Signaturgültigkeit oder Bestätigung. OP_RETURN-Ausgänge speichern Daten für externe Programme. Der Knoten ergänzt Gebührenabfragen, Prüfungen vor dem Senden, den RBF-Ersetzungsstatus und geordnete Blockdaten. Erst nach erfolgreicher Prüfung werden ersetzte ausstehende Transaktionen entfernt. Mehrfachsignaturen und gesperrte Ausgänge sind für isolierte Aktivierungstests implementiert und im öffentlichen Netz noch nicht aktiviert.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Gebühren, geprüfte Transaktion und Kompatibilität

Die Gebühr ist die Summe der Eingänge abzüglich der Summe der Ausgänge. Ein Wechselgeldausgang wird nur dann geschätzt, wenn die Wallet tatsächlich ausreichend Wechselgeld erzeugt. Ein Rest unterhalb der Wallet-Schwelle wird der Gebühr zugeschlagen; die resultierende Gebühr und die gesamte Belastung erscheinen zur Prüfung. Der Gebührensatz wird in yugeon/vB angegeben. Die virtuelle Größe entspricht dem Transaktionsgewicht geteilt durch vier, aufgerundet auf eine ganze Zahl.

Die Wallet wählt Eingänge und Ausgänge genau einmal und signiert diesen Transaktionsplan. Beim Bestätigen wird die gespeicherte signierte Transaktion eingereicht, ohne sie neu aufzubauen oder die Gebühr neu zu berechnen. Ein abgelaufenes Angebot oder inzwischen ausgegebene Eingänge erfordern eine erneute Prüfung. Die Aufnahme in die lokale Warteschlange ist noch keine Bestätigung in einem Block.

Bei gewöhnlichen P2WPKH-Zahlungen erzeugt die Wallet Low-R-/Low-S-Signaturen mit höchstens 71 Byte einschließlich des SIGHASH_ALL-Bytes. Das ist eine Signatur- und Schätzrichtlinie, keine neue Konsensgrenze für andere gültige Signaturen. Kürzere Signaturen können die tatsächliche virtuelle Größe verringern. Die vorgeschlagenen Sätze beruhen weiterhin auf der lokalen Warteschlange; eine ähnliche Größenberechnung wie bei Bitcoin übernimmt nicht dessen Netzwerkgebühren.

## Kompatibilität der Android-Signatur

Wallet-Dateiformate, Adressen und vorhandene Coins bleiben unverändert. Die vorhandene verschlüsselte Sicherung lässt sich in der neuen App wiederherstellen, um dieselbe Wallet weiterzuverwenden. Der Android-Knoten 0.6.103 und die Wallet 1.1.14 verwenden einen neu erzeugten Veröffentlichungsschlüssel. Sie können keine mit einem anderen Schlüssel signierte Installation ersetzen. Bewahren Sie die alte App und ihre Daten auf, bis eine verschlüsselte Wallet-Sicherung und ein funktionierender Wiederherstellungsweg vorliegen. Deinstallieren Sie die alte App nicht nur, um die Installation eines Updates zu erzwingen.

<!-- /payment-policy-20261116 -->
