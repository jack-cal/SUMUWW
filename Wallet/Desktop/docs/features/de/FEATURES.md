# SUMUWW Wallet PC 1.0.15

Der Knoten baut normalerweise 10 ausgehende Verbindungen auf. Die meisten leiten Blöcke und Transaktionen weiter. Eine geprüfte Ersatzverbindung kann Blöcke weiterleiten. Zur Suche nach weiteren Knoten kann kurzzeitig eine elfte Verbindung hinzukommen. Insgesamt sind 125 Verbindungen möglich. Bei 10 ausgehenden Verbindungen sind bis zu 115 eingehende möglich, sonst höchstens 117.

1 SMW = 100.000.000 yugeon. Die automatische Berechnung bietet drei Stufen anhand lokaler Beobachtungen, ohne Bestätigungszeiten zu garantieren. Sie können einen Satz in yugeon/vB eingeben. Prüfen Sie vor dem Senden die endgültige Gebühr und die Summe in SMW. Abgelehnte Transaktionen belasten das Guthaben nicht.

Bei einem Eingang von 1 SMW hängt die Gebühr davon ab, ob Wechselgeld zurückgeht. Sind alle Ein- und Ausgänge vom Typ P2WPKH, kostet eine Zahlung von 0.99999890 SMW bei 1 yugeon/vB genau 110 yugeon. Es bleibt kein Wechselgeld. Bei 0.8 SMW aus demselben Eingang kommt ein Wechselgeldausgang hinzu. Die Gebühr beträgt dann 141 yugeon. Die Wallet gibt Wechselgeld zurück, wenn der Rest nach Abzug der Gebühr einen Mindestbetrag erreicht. Dieser berücksichtigt die Kosten, die beim späteren Ausgeben des Wechselgelds anfallen. Kleinere Restbeträge fließen in die vor der Bestätigung angezeigte Gebühr ein. Bei einem nativen SegWit-Eingang (P2WPKH) rechnet die Wallet mit bis zu 71 Byte für die Signatur einschließlich des Hash-Typs.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Automatische Gebühren berücksichtigen das ausstehende Datenvolumen, die Blockkapazität und die Transaktionspriorität. Frühere Blockgebühren werden nicht verwendet. Bei geringer Auslastung gilt der Mindestsatz. Die Vorschau wird aktualisiert; die abschließende Bestätigung legt die Gebühr fest. Die Beobachtung erfasst den verbundenen lokalen Knoten, nicht alle Knoten.

Die von diesem Knoten erfassten Ersetzungen bleiben nach dem Neustart der Wallet erhalten. Entfernte Transaktionen ändern das Guthaben nicht.

Der Mining-Verlauf zeigt neue Ausgabe, Transaktionsgebühren und Gesamtbelohnung jedes Blocks getrennt. Der von Ihrer Wallet empfangene Betrag wird separat angezeigt. Bei einer teilweise beanspruchten Belohnung wird die Aufteilung nicht angenommen. Der Knoten bietet 28 RPC-Methoden einschließlich Gebührenschätzung und prüft und verbreitet signierte Transaktionen.

<!-- payment-policy-20261116 -->

## Gebühren, geprüfte Transaktion und Kompatibilität

Die Gebühr ist die Summe der Eingänge abzüglich der Summe der Ausgänge. Ein Wechselgeldausgang wird nur dann geschätzt, wenn die Wallet tatsächlich ausreichend Wechselgeld erzeugt. Ein Rest unterhalb der Wallet-Schwelle wird der Gebühr zugeschlagen; die resultierende Gebühr und die gesamte Belastung erscheinen zur Prüfung. Der Gebührensatz wird in yugeon/vB angegeben. Die virtuelle Größe entspricht dem Transaktionsgewicht geteilt durch vier, aufgerundet auf eine ganze Zahl.

Die Wallet wählt Eingänge und Ausgänge genau einmal und signiert diesen Transaktionsplan. Beim Bestätigen wird die gespeicherte signierte Transaktion eingereicht, ohne sie neu aufzubauen oder die Gebühr neu zu berechnen. Ein abgelaufenes Angebot oder inzwischen ausgegebene Eingänge erfordern eine erneute Prüfung. Die Aufnahme in die lokale Warteschlange ist noch keine Bestätigung in einem Block.

Bei gewöhnlichen P2WPKH-Zahlungen erzeugt die Wallet Low-R-/Low-S-Signaturen mit höchstens 71 Byte einschließlich des SIGHASH_ALL-Bytes. Das ist eine Signatur- und Schätzrichtlinie, keine neue Konsensgrenze für andere gültige Signaturen. Kürzere Signaturen können die tatsächliche virtuelle Größe verringern. 

<!-- /payment-policy-20261116 -->

Nach einer gültigen Versionsantwort gibt der Knoten der Gegenstelle Zeit für die Bestätigung. Führen zwei ausgehende Verbindungen zum selben Knoten, bleibt ein Weg offen, bis die Synchronisierung über eine der Verbindungen abgeschlossen ist. 
