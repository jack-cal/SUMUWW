# SUMUWW · Documentatie

SUMUWW PC 0.57.51 · De node valideert, bewaart, verspreidt en ontsluit ketengegevens.

## Ondertekenformaat

De optionele broncode-SDK stelt transacties samen en controleert aangeleverde handtekeningen zonder sleutels of netwerk. Het is geen ondertekenprogramma of nodecommando. De P2WPKH-beperking geldt voor het voorbeeldformaat, niet de node. De bestaande persoonlijke wallet blijft beschikbaar.

## RPC- en HTTP-API

validateaddress controleert controlesom en gekozen netwerk. decoderawtransaction geeft decoded_only, geen bewijs van een geldige handtekening of bevestiging. OP_RETURN bewaart gegevens voor externe programma’s. De node biedt kostenopvragen, controle vóór verzending, de status van RBF-vervangingen en gegevens in blokvolgorde. Vervangingen worden gecontroleerd voordat wachtende transacties worden verwijderd. Meervoudige handtekeningen en vergrendelde outputs zijn geïmplementeerd voor afzonderlijke activeringstests; ze zijn nog niet actief op het openbare netwerk.

## Verificatie

Installeer de afhankelijkheden en voer python examples/node_contract.py uit vanuit de broncode. Openbare testsleutels en tijdelijk regtest testen indiening, afwijzing, bevestigingen, reorganisatie en gegevensbehoud. Er worden geen echte tegoeden, gebruikersprofielen of hardwareondertekenaars gebruikt.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Node-interface](EXCHANGE_INTEGRATION.html) · [RPC- en HTTP-API](RPC_API.html) · [Nodebeheer](NETWORK_RUNBOOK.html) · [Versieopmerkingen](RELEASE_NOTES.html) · [Verificatie](EXCHANGE_EXAMPLES.html)

[Uitgebreide Engelse referentie](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Kosten, gecontroleerde transactie en compatibiliteit

De transactiekosten zijn de som van de inputs min de som van de outputs. De schatting telt een wisselgelduitgang alleen mee wanneer de wallet daadwerkelijk voldoende wisselgeld aanmaakt. Een restbedrag onder de walletdrempel wordt bij de kosten opgeteld; de uiteindelijke kosten en de totale afschrijving worden ter controle getoond. Het tarief wordt uitgedrukt in yugeon/vB. De virtuele grootte is het transactiegewicht gedeeld door vier, naar boven afgerond.

De wallet kiest de inputs en outputs één keer en ondertekent datzelfde transactieplan. Na bevestiging wordt de opgeslagen ondertekende transactie ingediend, zonder deze opnieuw op te bouwen of de kosten opnieuw te berekenen. Een verlopen prijsopgave of inmiddels uitgegeven inputs vereisen een nieuwe controle. Opname in de lokale wachtrij betekent nog geen bevestiging in een blok.

Voor gewone P2WPKH-betalingen maakt de wallet low-R- en low-S-handtekeningen van maximaal 71 bytes, inclusief de SIGHASH_ALL-byte. Dit is beleid voor ondertekening en grootteschatting, geen nieuwe consensuslimiet voor andere geldige handtekeningen. Een kortere handtekening kan de werkelijke virtuele grootte verkleinen. 

<!-- /payment-policy-20261116 -->
