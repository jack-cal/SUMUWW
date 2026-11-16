# SUMUWW Android 0.6.103 · Node-Betrieb

Nach dem Neustart setzt der Knoten beim letzten lokal geprüften Block an und prüft neue Blöcke. Fehlt der gespeicherte Prüfnachweis oder ist er widersprüchlich, prüft der Knoten den gespeicherten Verlauf erneut.

SUMUWW Android 0.6.103 · Der Knoten prüft, speichert, verbreitet und liefert Kettendaten.

## Netzwerk und Adressen

Das öffentliche Netzwerk heißt `sumuww`, intern auch `dora`. Prüfen Sie den unten angegebenen Genesis-Hash. Native Adressen verwenden Witness-v0-P2WPKH und HASH160 eines komprimierten secp256k1-Public-Keys. Memo oder Tag sind nicht vorgeschrieben. Falsches Netzwerk und ungültige Prüfsummen sind abzulehnen. Empfangs-/Wechselgeldzweig und HD-Index dokumentieren; nicht den Bitcoin-Ableitungspfad voraussetzen.

## Transaktionen und Blöcke abfragen

`getrawtransaction` durchsucht aktive Kette und Mempool, keine ausschließlich verwaisten Transaktionen. Eingänge nennen frühere Ausgänge, keine eindeutige Absenderadresse. `getblock` erwartet boolesches `verbose`; gespeicherte inaktive Blöcke haben `active=false` und `confirmations=-1`. Ihre Rohtransaktionen bleiben über den Block-Hash abrufbar. `findspendingtransaction` sucht nur bestätigte aktive Ausgaben; null beweist keine Verfügbarkeit. `gettxout` mit `include_mempool=true` prüfen. Bestätigungen und Aktivstatus können sich durch Reorganisation ändern.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Gebühren, geprüfte Transaktion und Kompatibilität

Die Gebühr ist die Summe der Eingänge abzüglich der Summe der Ausgänge. Ein Wechselgeldausgang wird nur dann geschätzt, wenn die Wallet tatsächlich ausreichend Wechselgeld erzeugt. Ein Rest unterhalb der Wallet-Schwelle wird der Gebühr zugeschlagen; die resultierende Gebühr und die gesamte Belastung erscheinen zur Prüfung. Der Gebührensatz wird in yugeon/vB angegeben. Die virtuelle Größe entspricht dem Transaktionsgewicht geteilt durch vier, aufgerundet auf eine ganze Zahl.

Die Wallet wählt Eingänge und Ausgänge genau einmal und signiert diesen Transaktionsplan. Beim Bestätigen wird die gespeicherte signierte Transaktion eingereicht, ohne sie neu aufzubauen oder die Gebühr neu zu berechnen. Ein abgelaufenes Angebot oder inzwischen ausgegebene Eingänge erfordern eine erneute Prüfung. Die Aufnahme in die lokale Warteschlange ist noch keine Bestätigung in einem Block.

Bei gewöhnlichen P2WPKH-Zahlungen erzeugt die Wallet Low-R-/Low-S-Signaturen mit höchstens 71 Byte einschließlich des SIGHASH_ALL-Bytes. Das ist eine Signatur- und Schätzrichtlinie, keine neue Konsensgrenze für andere gültige Signaturen. Kürzere Signaturen können die tatsächliche virtuelle Größe verringern. Die vorgeschlagenen Sätze beruhen weiterhin auf der lokalen Warteschlange; eine ähnliche Größenberechnung wie bei Bitcoin übernimmt nicht dessen Netzwerkgebühren.

## Kompatibilität der Android-Signatur

Wallet-Dateiformate, Adressen und vorhandene Coins bleiben unverändert. Die vorhandene verschlüsselte Sicherung lässt sich in der neuen App wiederherstellen, um dieselbe Wallet weiterzuverwenden. Der Android-Knoten 0.6.103 und die Wallet 1.1.14 verwenden einen neu erzeugten Veröffentlichungsschlüssel. Sie können keine mit einem anderen Schlüssel signierte Installation ersetzen. Bewahren Sie die alte App und ihre Daten auf, bis eine verschlüsselte Wallet-Sicherung und ein funktionierender Wiederherstellungsweg vorliegen. Deinstallieren Sie die alte App nicht nur, um die Installation eines Updates zu erzwingen.

<!-- /payment-policy-20261116 -->

Nach einer gültigen Versionsantwort gibt der Knoten der Gegenstelle Zeit für die Bestätigung. Führen zwei ausgehende Verbindungen zum selben Knoten, bleibt ein Weg offen, bis die Synchronisierung über eine der Verbindungen abgeschlossen ist. Der integrierte Selbsttest nimmt einen Block mit gültigem Arbeitsnachweis an, bevor der Verbindungsnachweis vorliegt. Anschließend prüft er die Unterschriften der drei Zeugen, die Weiterleitung des Nachweises und seine Verfügbarkeit nach einem Neustart.
