# SUMUWW Android 0.6.103 · Versieopmerkingen

Bij één invoer van 1 SMW hangen de kosten af van de vraag of je wisselgeld terugkrijgt. Zijn de invoer en alle uitvoeren van het type P2WPKH, dan kost een betaling van 0.99999890 SMW bij een tarief van 1 yugeon/vB precies 110 yugeon en blijft er geen wisselgeld over. Verstuur je vanuit dezelfde invoer 0.8 SMW, dan komt er een uitvoer voor wisselgeld bij en betaal je 141 yugeon. De wallet geeft wisselgeld terug als het bedrag dat na aftrek van de kosten overblijft een minimum bereikt. Dat minimum houdt rekening met de kosten om het wisselgeld later uit te geven. Een kleiner restant wordt opgenomen in de kosten die je vóór de bevestiging ziet. Bij een native SegWit-invoer van de wallet (P2WPKH) rekent de schatting op maximaal 71 bytes voor de handtekening, inclusief het hashtype.

Na een herstart gaat het knooppunt verder vanaf het laatste lokaal geverifieerde blok en controleert het nieuwe blokken. Als het opgeslagen verificatierecord ontbreekt of niet klopt, controleert het de opgeslagen geschiedenis opnieuw.

SUMUWW Android 0.6.103 · De node valideert, bewaart, verspreidt en ontsluit ketengegevens.

[Documentatie](../../integration/docs/i18n/nl/RELEASE_NOTES.html)

<!-- payment-policy-20261116 -->

## Kosten, gecontroleerde transactie en compatibiliteit

De transactiekosten zijn de som van de inputs min de som van de outputs. De schatting telt een wisselgelduitgang alleen mee wanneer de wallet daadwerkelijk voldoende wisselgeld aanmaakt. Een restbedrag onder de walletdrempel wordt bij de kosten opgeteld; de uiteindelijke kosten en de totale afschrijving worden ter controle getoond. Het tarief wordt uitgedrukt in yugeon/vB. De virtuele grootte is het transactiegewicht gedeeld door vier, naar boven afgerond.

De wallet kiest de inputs en outputs één keer en ondertekent datzelfde transactieplan. Na bevestiging wordt de opgeslagen ondertekende transactie ingediend, zonder deze opnieuw op te bouwen of de kosten opnieuw te berekenen. Een verlopen prijsopgave of inmiddels uitgegeven inputs vereisen een nieuwe controle. Opname in de lokale wachtrij betekent nog geen bevestiging in een blok.

Voor gewone P2WPKH-betalingen maakt de wallet low-R- en low-S-handtekeningen van maximaal 71 bytes, inclusief de SIGHASH_ALL-byte. Dit is beleid voor ondertekening en grootteschatting, geen nieuwe consensuslimiet voor andere geldige handtekeningen. Een kortere handtekening kan de werkelijke virtuele grootte verkleinen. 

## Compatibiliteit van Android-handtekeningen

Wallet-bestandsformaten, adressen en bestaande coins zijn niet gewijzigd. De bestaande versleutelde back-up kan in de nieuwe app worden hersteld om dezelfde wallet te blijven gebruiken. De Android-node 0.6.103 en wallet 1.1.14 gebruiken een nieuwe releasesleutel voor ondertekening. Ze kunnen een installatie die met een andere sleutel is ondertekend niet vervangen. Bewaar de oude app en gegevens totdat een versleutelde walletback-up en een werkende herstelmethode beschikbaar zijn. Verwijder de oude app niet alleen om een update te kunnen forceren.

<!-- /payment-policy-20261116 -->
