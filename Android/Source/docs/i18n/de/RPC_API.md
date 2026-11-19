# SUMUWW Android 0.6.103 · RPC- und HTTP-API

SUMUWW Android 0.6.103 · Der Knoten prüft, speichert, verbreitet und liefert Kettendaten.

[Dokumentation](../../integration/docs/i18n/de/RPC_API.html)

<!-- payment-policy-20261116 -->

## Gebühren, geprüfte Transaktion und Kompatibilität

Die Gebühr ist die Summe der Eingänge abzüglich der Summe der Ausgänge. Ein Wechselgeldausgang wird nur dann geschätzt, wenn die Wallet tatsächlich ausreichend Wechselgeld erzeugt. Ein Rest unterhalb der Wallet-Schwelle wird der Gebühr zugeschlagen; die resultierende Gebühr und die gesamte Belastung erscheinen zur Prüfung. Der Gebührensatz wird in yugeon/vB angegeben. Die virtuelle Größe entspricht dem Transaktionsgewicht geteilt durch vier, aufgerundet auf eine ganze Zahl.

Die Wallet wählt Eingänge und Ausgänge genau einmal und signiert diesen Transaktionsplan. Beim Bestätigen wird die gespeicherte signierte Transaktion eingereicht, ohne sie neu aufzubauen oder die Gebühr neu zu berechnen. Ein abgelaufenes Angebot oder inzwischen ausgegebene Eingänge erfordern eine erneute Prüfung. Die Aufnahme in die lokale Warteschlange ist noch keine Bestätigung in einem Block.

Bei gewöhnlichen P2WPKH-Zahlungen erzeugt die Wallet Low-R-/Low-S-Signaturen mit höchstens 71 Byte einschließlich des SIGHASH_ALL-Bytes. Das ist eine Signatur- und Schätzrichtlinie, keine neue Konsensgrenze für andere gültige Signaturen. Kürzere Signaturen können die tatsächliche virtuelle Größe verringern. 

## Kompatibilität der Android-Signatur

Wallet-Dateiformate, Adressen und vorhandene Coins bleiben unverändert. Die vorhandene verschlüsselte Sicherung lässt sich in der neuen App wiederherstellen, um dieselbe Wallet weiterzuverwenden. Der Android-Knoten 0.6.103 und die Wallet 1.1.14 verwenden einen neu erzeugten Veröffentlichungsschlüssel. Sie können keine mit einem anderen Schlüssel signierte Installation ersetzen. Bewahren Sie die alte App und ihre Daten auf, bis eine verschlüsselte Wallet-Sicherung und ein funktionierender Wiederherstellungsweg vorliegen. Deinstallieren Sie die alte App nicht nur, um die Installation eines Updates zu erzwingen.

<!-- /payment-policy-20261116 -->
