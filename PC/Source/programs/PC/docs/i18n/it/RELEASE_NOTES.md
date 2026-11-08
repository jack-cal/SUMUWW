# SUMUWW · Note di versione

Il nodo apre normalmente 10 connessioni in uscita. La maggior parte inoltra blocchi e transazioni. Può usare una connessione di riserva verificata per i blocchi e aprirne brevemente un’undicesima per cercare altri nodi. Il limite complessivo è 125. Sono ammesse fino a 117 connessioni in ingresso, o 115 con 10 in uscita. L’app per computer ora mostra solo il numero totale di nodi connessi. Ogni dispositivo di mining costruisce i propri blocchi. Il nodo su PC inoltra i blocchi completi e rifiuta le richieste di lavoro e le soluzioni di mining inviate dal telefono.

Al riavvio il nodo riparte dall’ultimo blocco verificato localmente e controlla i nuovi blocchi. Se la verifica salvata manca o i dati non corrispondono, ricontrolla la cronologia archiviata.


SUMUWW PC 0.57.54 · Il nodo verifica, conserva, inoltra e rende consultabili i dati della catena.

## Formato di firma

L’SDK opzionale nei sorgenti costruisce transazioni e verifica firme ricevute senza chiavi né rete. Non è un programma di firma o un comando del nodo. Il limite P2WPKH riguarda il formato dell’esempio, non il nodo. Il portafoglio personale esistente resta disponibile.

## API RPC e HTTP

validateaddress controlla checksum e rete scelta. decoderawtransaction restituisce decoded_only, senza attestare validità della firma o conferma. OP_RETURN conserva dati per programmi esterni. Il nodo aggiunge consultazione delle commissioni, verifica prima dell’invio, stato delle sostituzioni RBF e lettura dei dati nell’ordine dei blocchi. La sostituzione viene verificata prima di rimuovere le transazioni in attesa. Firme multiple e output bloccati sono implementati per test isolati di attivazione; non sono ancora attivi sulla rete pubblica.

## Verifica

Installate le dipendenze, eseguire python examples/node_contract.py dai sorgenti. Chiavi pubbliche di prova e regtest temporaneo verificano invio, rifiuto, conferme, riorganizzazione e persistenza. Non vengono usati fondi reali, profili personali o dispositivi di firma.

[Documentazione](README.html) · [Interfaccia del nodo](EXCHANGE_INTEGRATION.html) · [API RPC e HTTP](RPC_API.html) · [Gestione del nodo](NETWORK_RUNBOOK.html) · [Verifica](EXCHANGE_EXAMPLES.html)

[Riferimento esteso in inglese](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
