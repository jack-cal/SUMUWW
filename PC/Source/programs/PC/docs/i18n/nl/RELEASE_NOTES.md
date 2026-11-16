# SUMUWW · Versieopmerkingen

Bij één invoer van 1 SMW hangen de kosten af van de vraag of je wisselgeld terugkrijgt. Zijn de invoer en alle uitvoeren van het type P2WPKH, dan kost een betaling van 0.99999890 SMW bij een tarief van 1 yugeon/vB precies 110 yugeon en blijft er geen wisselgeld over. Verstuur je vanuit dezelfde invoer 0.8 SMW, dan komt er een uitvoer voor wisselgeld bij en betaal je 141 yugeon. De wallet geeft wisselgeld terug als het bedrag dat na aftrek van de kosten overblijft een minimum bereikt. Dat minimum houdt rekening met de kosten om het wisselgeld later uit te geven. Een kleiner restant wordt opgenomen in de kosten die je vóór de bevestiging ziet. Bij een native SegWit-invoer van de wallet (P2WPKH) rekent de schatting op maximaal 71 bytes voor de handtekening, inclusief het hashtype.


0.57.61 · Als u van taal wisselt terwijl de app geopend is, verandert ook het pictogram op de Windows-taakbalk.

Het knooppunt opent gewoonlijk 10 uitgaande verbindingen. De meeste geven blokken en transacties door. Een geverifieerde reserveverbinding kan blokken doorgeven. Om andere knooppunten te vinden kan er kort een elfde verbinding bijkomen. De totale limiet is 125. Er zijn maximaal 117 inkomende verbindingen mogelijk, of 115 bij 10 uitgaande verbindingen. De desktopapp toont nu alleen het totale aantal verbonden knooppunten. Elke miner bouwt zijn eigen blokken. De pc-node stuurt voltooide blokken door en weigert aanvragen voor miningwerk en oplossingen van telefoons.

Na een herstart gaat het knooppunt verder vanaf het laatste lokaal geverifieerde blok en controleert het nieuwe blokken. Als het opgeslagen verificatierecord ontbreekt of niet klopt, controleert het de opgeslagen geschiedenis opnieuw.


SUMUWW PC 0.57.61 · De node valideert, bewaart, verspreidt en ontsluit ketengegevens.

## Ondertekenformaat

De optionele broncode-SDK stelt transacties samen en controleert aangeleverde handtekeningen zonder sleutels of netwerk. Het is geen ondertekenprogramma of nodecommando. De P2WPKH-beperking geldt voor het voorbeeldformaat, niet de node. De bestaande persoonlijke wallet blijft beschikbaar.

## RPC- en HTTP-API

validateaddress controleert controlesom en gekozen netwerk. decoderawtransaction geeft decoded_only, geen bewijs van een geldige handtekening of bevestiging. OP_RETURN bewaart gegevens voor externe programma’s. De node biedt kostenopvragen, controle vóór verzending, de status van RBF-vervangingen en gegevens in blokvolgorde. Vervangingen worden gecontroleerd voordat wachtende transacties worden verwijderd. Meervoudige handtekeningen en vergrendelde outputs zijn geïmplementeerd voor afzonderlijke activeringstests; ze zijn nog niet actief op het openbare netwerk.

## Verificatie

Installeer de afhankelijkheden en voer python examples/node_contract.py uit vanuit de broncode. Openbare testsleutels en tijdelijk regtest testen indiening, afwijzing, bevestigingen, reorganisatie en gegevensbehoud. Er worden geen echte tegoeden, gebruikersprofielen of hardwareondertekenaars gebruikt.

[Documentatie](README.html) · [Node-interface](EXCHANGE_INTEGRATION.html) · [RPC- en HTTP-API](RPC_API.html) · [Nodebeheer](NETWORK_RUNBOOK.html) · [Verificatie](EXCHANGE_EXAMPLES.html)

[Uitgebreide Engelse referentie](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Kosten, gecontroleerde transactie en compatibiliteit

De transactiekosten zijn de som van de inputs min de som van de outputs. De schatting telt een wisselgelduitgang alleen mee wanneer de wallet daadwerkelijk voldoende wisselgeld aanmaakt. Een restbedrag onder de walletdrempel wordt bij de kosten opgeteld; de uiteindelijke kosten en de totale afschrijving worden ter controle getoond. Het tarief wordt uitgedrukt in yugeon/vB. De virtuele grootte is het transactiegewicht gedeeld door vier, naar boven afgerond.

De wallet kiest de inputs en outputs één keer en ondertekent datzelfde transactieplan. Na bevestiging wordt de opgeslagen ondertekende transactie ingediend, zonder deze opnieuw op te bouwen of de kosten opnieuw te berekenen. Een verlopen prijsopgave of inmiddels uitgegeven inputs vereisen een nieuwe controle. Opname in de lokale wachtrij betekent nog geen bevestiging in een blok.

Voor gewone P2WPKH-betalingen maakt de wallet low-R- en low-S-handtekeningen van maximaal 71 bytes, inclusief de SIGHASH_ALL-byte. Dit is beleid voor ondertekening en grootteschatting, geen nieuwe consensuslimiet voor andere geldige handtekeningen. Een kortere handtekening kan de werkelijke virtuele grootte verkleinen. Voorgestelde tarieven blijven gebaseerd op de lokale wachtrij; een vergelijkbare grootteberekening als bij Bitcoin neemt niet de tarieven van het Bitcoin-netwerk over.

## Windows-I2P-component en beveiligingscontrole

De Windows-pakketten bevatten de officiële i2pd 3.0.0 met bijgewerkte hashes en certificaten voor de eerste verbinding. In de vastgelegde controle detecteert Defender het officiële I2P-programmabestand en oorspronkelijke ZIP nog steeds. Een overeenkomende officiële hash bewijst geen veiligheid en bevestigt geen foutpositieve melding. Een lokale bestandsuitsluiting geldt uitsluitend op de pc waarop deze is ingesteld; het openbare pakket voegt die niet toe. Andere computers kunnen dezelfde bestanden blokkeren.

<!-- /payment-policy-20261116 -->
