# SUMUWW Android 0.6.103 · Nodebeheer

Na een herstart gaat het knooppunt verder vanaf het laatste lokaal geverifieerde blok en controleert het nieuwe blokken. Als het opgeslagen verificatierecord ontbreekt of niet klopt, controleert het de opgeslagen geschiedenis opnieuw.

SUMUWW Android 0.6.103 · De node valideert, bewaart, verspreidt en ontsluit ketengegevens.

[Documentatie](../../integration/docs/i18n/nl/NETWORK_RUNBOOK.html)

<!-- payment-policy-20261116 -->

## Kosten, gecontroleerde transactie en compatibiliteit

De transactiekosten zijn de som van de inputs min de som van de outputs. De schatting telt een wisselgelduitgang alleen mee wanneer de wallet daadwerkelijk voldoende wisselgeld aanmaakt. Een restbedrag onder de walletdrempel wordt bij de kosten opgeteld; de uiteindelijke kosten en de totale afschrijving worden ter controle getoond. Het tarief wordt uitgedrukt in yugeon/vB. De virtuele grootte is het transactiegewicht gedeeld door vier, naar boven afgerond.

De wallet kiest de inputs en outputs één keer en ondertekent datzelfde transactieplan. Na bevestiging wordt de opgeslagen ondertekende transactie ingediend, zonder deze opnieuw op te bouwen of de kosten opnieuw te berekenen. Een verlopen prijsopgave of inmiddels uitgegeven inputs vereisen een nieuwe controle. Opname in de lokale wachtrij betekent nog geen bevestiging in een blok.

Voor gewone P2WPKH-betalingen maakt de wallet low-R- en low-S-handtekeningen van maximaal 71 bytes, inclusief de SIGHASH_ALL-byte. Dit is beleid voor ondertekening en grootteschatting, geen nieuwe consensuslimiet voor andere geldige handtekeningen. Een kortere handtekening kan de werkelijke virtuele grootte verkleinen. 

## Compatibiliteit van Android-handtekeningen

Wallet-bestandsformaten, adressen en bestaande coins zijn niet gewijzigd. De bestaande versleutelde back-up kan in de nieuwe app worden hersteld om dezelfde wallet te blijven gebruiken. De Android-node 0.6.103 en wallet 1.1.14 gebruiken een nieuwe releasesleutel voor ondertekening. Ze kunnen een installatie die met een andere sleutel is ondertekend niet vervangen. Bewaar de oude app en gegevens totdat een versleutelde walletback-up en een werkende herstelmethode beschikbaar zijn. Verwijder de oude app niet alleen om een update te kunnen forceren.

<!-- /payment-policy-20261116 -->

Na een geldig antwoord met de versiegegevens geeft de node de andere node tijd om een bevestiging te sturen. Als twee uitgaande verbindingen naar dezelfde node leiden, blijft er een route open totdat de synchronisatie via een van beide is voltooid. 
