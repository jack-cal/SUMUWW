# SUMUWW Wallet PC 1.0.15

Het knooppunt opent gewoonlijk 10 uitgaande verbindingen. De meeste geven blokken en transacties door. Een geverifieerde reserveverbinding kan blokken doorgeven. Om andere knooppunten te vinden kan er kort een elfde verbinding bijkomen. De totale limiet is 125. Er zijn maximaal 117 inkomende verbindingen mogelijk, of 115 bij 10 uitgaande verbindingen.


1 SMW = 100.000.000 yugeon. Automatische kosten bieden drie niveaus op basis van lokale waarnemingen, zonder de bevestigingstijd te garanderen. U kunt een tarief in yugeon/vB invoeren. Controleer vóór verzending de definitieve kosten en het totaal in SMW. Een geweigerde transactie verlaagt het saldo niet.

Bij één invoer van 1 SMW hangen de kosten af van de vraag of je wisselgeld terugkrijgt. Zijn de invoer en alle uitvoeren van het type P2WPKH, dan kost een betaling van 0.99999890 SMW bij een tarief van 1 yugeon/vB precies 110 yugeon en blijft er geen wisselgeld over. Verstuur je vanuit dezelfde invoer 0.8 SMW, dan komt er een uitvoer voor wisselgeld bij en betaal je 141 yugeon. De wallet geeft wisselgeld terug als het bedrag dat na aftrek van de kosten overblijft een minimum bereikt. Dat minimum houdt rekening met de kosten om het wisselgeld later uit te geven. Een kleiner restant wordt opgenomen in de kosten die je vóór de bevestiging ziet. Bij een native SegWit-invoer van de wallet (P2WPKH) rekent de schatting op maximaal 71 bytes voor de handtekening, inclusief het hashtype.


`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Automatische kosten volgen het wachtende datavolume, de blokcapaciteit en de transactieprioriteit. Kosten uit eerdere blokken tellen niet mee. Bij weinig wachtrij blijft het minimumtarief gelden. Het voorbeeld wordt vernieuwd; de definitieve bevestiging legt de kosten vast. De waarneming geldt voor de verbonden lokale node, niet voor alle nodes.

De door dit knooppunt vastgelegde vervangingsgeschiedenis blijft na het herstarten van de wallet bewaard. Verwijderde transacties veranderen het saldo niet.


De mininggeschiedenis toont nieuwe uitgifte, transactiekosten en totale beloning per blok afzonderlijk. Het bedrag dat uw wallet ontvangt staat apart. Bij een gedeeltelijk opgeëiste beloning wordt de verdeling niet aangenomen. De node biedt 28 RPC-methoden, waaronder kostenschatting, en controleert en verspreidt ondertekende transacties.

<!-- payment-policy-20261116 -->

## Kosten, gecontroleerde transactie en compatibiliteit

De transactiekosten zijn de som van de inputs min de som van de outputs. De schatting telt een wisselgelduitgang alleen mee wanneer de wallet daadwerkelijk voldoende wisselgeld aanmaakt. Een restbedrag onder de walletdrempel wordt bij de kosten opgeteld; de uiteindelijke kosten en de totale afschrijving worden ter controle getoond. Het tarief wordt uitgedrukt in yugeon/vB. De virtuele grootte is het transactiegewicht gedeeld door vier, naar boven afgerond.

De wallet kiest de inputs en outputs één keer en ondertekent datzelfde transactieplan. Na bevestiging wordt de opgeslagen ondertekende transactie ingediend, zonder deze opnieuw op te bouwen of de kosten opnieuw te berekenen. Een verlopen prijsopgave of inmiddels uitgegeven inputs vereisen een nieuwe controle. Opname in de lokale wachtrij betekent nog geen bevestiging in een blok.

Voor gewone P2WPKH-betalingen maakt de wallet low-R- en low-S-handtekeningen van maximaal 71 bytes, inclusief de SIGHASH_ALL-byte. Dit is beleid voor ondertekening en grootteschatting, geen nieuwe consensuslimiet voor andere geldige handtekeningen. Een kortere handtekening kan de werkelijke virtuele grootte verkleinen. Voorgestelde tarieven blijven gebaseerd op de lokale wachtrij; een vergelijkbare grootteberekening als bij Bitcoin neemt niet de tarieven van het Bitcoin-netwerk over.

## Windows-I2P-component en beveiligingscontrole

De Windows-pakketten bevatten de officiële i2pd 3.0.0 met bijgewerkte hashes en certificaten voor de eerste verbinding. In de vastgelegde controle detecteert Defender het officiële I2P-programmabestand en oorspronkelijke ZIP nog steeds. Een overeenkomende officiële hash bewijst geen veiligheid en bevestigt geen foutpositieve melding. Een lokale bestandsuitsluiting geldt uitsluitend op de pc waarop deze is ingesteld; het openbare pakket voegt die niet toe. Andere computers kunnen dezelfde bestanden blokkeren.

<!-- /payment-policy-20261116 -->

Na een geldig antwoord met de versiegegevens geeft de node de andere node tijd om een bevestiging te sturen. Als twee uitgaande verbindingen naar dezelfde node leiden, blijft er een route open totdat de synchronisatie via een van beide is voltooid. De ingebouwde zelftest accepteert een blok met een geldig werkbewijs voordat het verbindingsbewijs beschikbaar is. Daarna controleert de test de handtekeningen van de drie getuigen, de doorgifte van het bewijs en het behoud ervan na een herstart.
