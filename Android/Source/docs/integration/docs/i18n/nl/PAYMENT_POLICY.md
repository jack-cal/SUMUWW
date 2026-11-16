# Kosten, gecontroleerde transactie en compatibiliteit

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Kosten, gecontroleerde transactie en compatibiliteit

De transactiekosten zijn de som van de inputs min de som van de outputs. De schatting telt een wisselgelduitgang alleen mee wanneer de wallet daadwerkelijk voldoende wisselgeld aanmaakt. Een restbedrag onder de walletdrempel wordt bij de kosten opgeteld; de uiteindelijke kosten en de totale afschrijving worden ter controle getoond. Het tarief wordt uitgedrukt in yugeon/vB. De virtuele grootte is het transactiegewicht gedeeld door vier, naar boven afgerond.

De wallet kiest de inputs en outputs één keer en ondertekent datzelfde transactieplan. Na bevestiging wordt de opgeslagen ondertekende transactie ingediend, zonder deze opnieuw op te bouwen of de kosten opnieuw te berekenen. Een verlopen prijsopgave of inmiddels uitgegeven inputs vereisen een nieuwe controle. Opname in de lokale wachtrij betekent nog geen bevestiging in een blok.

Voor gewone P2WPKH-betalingen maakt de wallet low-R- en low-S-handtekeningen van maximaal 71 bytes, inclusief de SIGHASH_ALL-byte. Dit is beleid voor ondertekening en grootteschatting, geen nieuwe consensuslimiet voor andere geldige handtekeningen. Een kortere handtekening kan de werkelijke virtuele grootte verkleinen. Voorgestelde tarieven blijven gebaseerd op de lokale wachtrij; een vergelijkbare grootteberekening als bij Bitcoin neemt niet de tarieven van het Bitcoin-netwerk over.

## Windows-I2P-component en beveiligingscontrole

De Windows-pakketten bevatten de officiële i2pd 3.0.0 met bijgewerkte hashes en certificaten voor de eerste verbinding. In de vastgelegde controle detecteert Defender het officiële I2P-programmabestand en oorspronkelijke ZIP nog steeds. Een overeenkomende officiële hash bewijst geen veiligheid en bevestigt geen foutpositieve melding. Een lokale bestandsuitsluiting geldt uitsluitend op de pc waarop deze is ingesteld; het openbare pakket voegt die niet toe. Andere computers kunnen dezelfde bestanden blokkeren.

## Compatibiliteit van Android-handtekeningen

Wallet-bestandsformaten, adressen en bestaande coins zijn niet gewijzigd. De bestaande versleutelde back-up kan in de nieuwe app worden hersteld om dezelfde wallet te blijven gebruiken. De Android-node 0.6.103 en wallet 1.1.14 gebruiken een nieuwe releasesleutel voor ondertekening. Ze kunnen een installatie die met een andere sleutel is ondertekend niet vervangen. Bewaar de oude app en gegevens totdat een versleutelde walletback-up en een werkende herstelmethode beschikbaar zijn. Verwijder de oude app niet alleen om een update te kunnen forceren.

<!-- /payment-policy-20261116 -->

Na een geldig antwoord met de versiegegevens geeft de node de andere node tijd om een bevestiging te sturen. Als twee uitgaande verbindingen naar dezelfde node leiden, blijft er een route open totdat de synchronisatie via een van beide is voltooid. De ingebouwde zelftest accepteert een blok met een geldig werkbewijs voordat het verbindingsbewijs beschikbaar is. Daarna controleert de test de handtekeningen van de drie getuigen, de doorgifte van het bewijs en het behoud ervan na een herstart.
