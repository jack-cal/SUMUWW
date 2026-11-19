# SUMUWW Android 0.6.103 · Documentatie

SUMUWW Android 0.6.103 · De node valideert, bewaart, verspreidt en ontsluit ketengegevens.

## Netwerk en adressen

Het publieke netwerk is `sumuww`, intern ook `dora`. Controleer de genesis-hash hieronder. Native adressen gebruiken witness-v0-P2WPKH en HASH160 van een gecomprimeerde secp256k1-publieke sleutel. Memo of tag is niet verplicht. Verwerp adressen van een verkeerd netwerk en ongeldige controlesommen. Noteer HD-ontvangst-/wisselgeldtak en index; neem geen Bitcoin-afleidingspad aan.

## Bedragen en beschikbare outputs

`_units` zijn gehele kleinste eenheden; `_smw` is tekst met 8 decimalen; `_dora` een compatibiliteitsalias. Er bestaat geen bedragveld `_sumuww`. 1 SMW = 100000000 eenheden. `gettxout` heeft geen `spendable` en kan onrijpe coinbase-outputs geven. Voor besteding in het volgende blok zijn minstens 100 bevestigingen nodig. Filter `listunspent` op `spendable`; available bij `getaddressbalance` sluit onrijpe en in wachtende transacties bestede middelen uit. Nieuwe mempool-outputs zijn niet bevestigd. Controleer de ketentop tussen pagina’s en valideer gekozen inputs opnieuw.

1 SMW = 100.000.000 yugeon. Automatische kosten bieden drie niveaus op basis van lokale waarnemingen, zonder de bevestigingstijd te garanderen. U kunt een tarief in yugeon/vB invoeren. Controleer vóór verzending de definitieve kosten en het totaal in SMW. Een geweigerde transactie verlaagt het saldo niet.

Bij één invoer van 1 SMW hangen de kosten af van de vraag of je wisselgeld terugkrijgt. Zijn de invoer en alle uitvoeren van het type P2WPKH, dan kost een betaling van 0.99999890 SMW bij een tarief van 1 yugeon/vB precies 110 yugeon en blijft er geen wisselgeld over. Verstuur je vanuit dezelfde invoer 0.8 SMW, dan komt er een uitvoer voor wisselgeld bij en betaal je 141 yugeon. De wallet geeft wisselgeld terug als het bedrag dat na aftrek van de kosten overblijft een minimum bereikt. Dat minimum houdt rekening met de kosten om het wisselgeld later uit te geven. Een kleiner restant wordt opgenomen in de kosten die je vóór de bevestiging ziet. Bij een native SegWit-invoer van de wallet (P2WPKH) rekent de schatting op maximaal 71 bytes voor de handtekening, inclusief het hashtype.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Automatische kosten volgen het wachtende datavolume, de blokcapaciteit en de transactieprioriteit. Kosten uit eerdere blokken tellen niet mee. Bij weinig wachtrij blijft het minimumtarief gelden. Het voorbeeld wordt vernieuwd; de definitieve bevestiging legt de kosten vast. De waarneming geldt voor de verbonden lokale node, niet voor alle nodes.

De door dit knooppunt vastgelegde vervangingsgeschiedenis blijft na het herstarten van de wallet bewaard. Verwijderde transacties veranderen het saldo niet.

De mininggeschiedenis toont nieuwe uitgifte, transactiekosten en totale beloning per blok afzonderlijk. Het bedrag dat uw wallet ontvangt staat apart. Bij een gedeeltelijk opgeëiste beloning wordt de verdeling niet aangenomen. De node biedt 28 RPC-methoden, waaronder kostenschatting, en controleert en verspreidt ondertekende transacties.

## Transacties en blokken opzoeken

`getrawtransaction` doorzoekt actieve keten en mempool, geen uitsluitend verweesde transacties. Inputs verwijzen naar eerdere outputs, niet één afzenderadres. `getblock` gebruikt booleaanse `verbose`; opgeslagen inactieve blokken hebben `active=false`, `confirmations=-1`. Hun ruwe transacties blijven via blokhash beschikbaar. `findspendingtransaction` zoekt alleen bevestigde actieve bestedingen; null bewijst geen beschikbaarheid. Controleer `gettxout` met `include_mempool=true`. Bevestigingen en actieve status kunnen veranderen na reorganisatie.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Kosten, gecontroleerde transactie en compatibiliteit

De transactiekosten zijn de som van de inputs min de som van de outputs. De schatting telt een wisselgelduitgang alleen mee wanneer de wallet daadwerkelijk voldoende wisselgeld aanmaakt. Een restbedrag onder de walletdrempel wordt bij de kosten opgeteld; de uiteindelijke kosten en de totale afschrijving worden ter controle getoond. Het tarief wordt uitgedrukt in yugeon/vB. De virtuele grootte is het transactiegewicht gedeeld door vier, naar boven afgerond.

De wallet kiest de inputs en outputs één keer en ondertekent datzelfde transactieplan. Na bevestiging wordt de opgeslagen ondertekende transactie ingediend, zonder deze opnieuw op te bouwen of de kosten opnieuw te berekenen. Een verlopen prijsopgave of inmiddels uitgegeven inputs vereisen een nieuwe controle. Opname in de lokale wachtrij betekent nog geen bevestiging in een blok.

Voor gewone P2WPKH-betalingen maakt de wallet low-R- en low-S-handtekeningen van maximaal 71 bytes, inclusief de SIGHASH_ALL-byte. Dit is beleid voor ondertekening en grootteschatting, geen nieuwe consensuslimiet voor andere geldige handtekeningen. Een kortere handtekening kan de werkelijke virtuele grootte verkleinen. 

## Compatibiliteit van Android-handtekeningen

Wallet-bestandsformaten, adressen en bestaande coins zijn niet gewijzigd. De bestaande versleutelde back-up kan in de nieuwe app worden hersteld om dezelfde wallet te blijven gebruiken. De Android-node 0.6.103 en wallet 1.1.14 gebruiken een nieuwe releasesleutel voor ondertekening. Ze kunnen een installatie die met een andere sleutel is ondertekend niet vervangen. Bewaar de oude app en gegevens totdat een versleutelde walletback-up en een werkende herstelmethode beschikbaar zijn. Verwijder de oude app niet alleen om een update te kunnen forceren.

<!-- /payment-policy-20261116 -->

Na een geldig antwoord met de versiegegevens geeft de node de andere node tijd om een bevestiging te sturen. Als twee uitgaande verbindingen naar dezelfde node leiden, blijft er een route open totdat de synchronisatie via een van beide is voltooid. 
