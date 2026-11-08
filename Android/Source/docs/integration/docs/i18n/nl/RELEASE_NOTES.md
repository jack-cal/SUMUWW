# SUMUWW Android 0.6.98 · Versieopmerkingen

De telefoon maakt verbinding met een volledige SUMUWW-node met versie 0.57.49 of hoger. Hij controleert de beloning en berekent het werkbewijs zonder de hele transactiegeschiedenis te downloaden.

De API-specificatie beschrijft de ingebouwde nodekern. De Android-app heeft geen RPC-instellingenscherm.

## RPC- en HTTP-API

validateaddress controleert controlesom en gekozen netwerk. decoderawtransaction geeft decoded_only, geen bewijs van een geldige handtekening of bevestiging. OP_RETURN bewaart gegevens voor externe programma’s. De node biedt kostenopvragen, controle vóór verzending, de status van RBF-vervangingen en gegevens in blokvolgorde. Vervangingen worden gecontroleerd voordat wachtende transacties worden verwijderd. Meervoudige handtekeningen en vergrendelde outputs zijn geïmplementeerd voor afzonderlijke activeringstests; ze zijn nog niet actief op het openbare netwerk.

[API_CONTRACT.json](../../../API_CONTRACT.json)
