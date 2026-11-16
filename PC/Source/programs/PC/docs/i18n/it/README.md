# SUMUWW · Documentazione

SUMUWW PC 0.57.51 · Il nodo verifica, conserva, inoltra e rende consultabili i dati della catena.

## Formato di firma

L’SDK opzionale nei sorgenti costruisce transazioni e verifica firme ricevute senza chiavi né rete. Non è un programma di firma o un comando del nodo. Il limite P2WPKH riguarda il formato dell’esempio, non il nodo. Il portafoglio personale esistente resta disponibile.

## API RPC e HTTP

validateaddress controlla checksum e rete scelta. decoderawtransaction restituisce decoded_only, senza attestare validità della firma o conferma. OP_RETURN conserva dati per programmi esterni. Il nodo aggiunge consultazione delle commissioni, verifica prima dell’invio, stato delle sostituzioni RBF e lettura dei dati nell’ordine dei blocchi. La sostituzione viene verificata prima di rimuovere le transazioni in attesa. Firme multiple e output bloccati sono implementati per test isolati di attivazione; non sono ancora attivi sulla rete pubblica.

## Verifica

Installate le dipendenze, eseguire python examples/node_contract.py dai sorgenti. Chiavi pubbliche di prova e regtest temporaneo verificano invio, rifiuto, conferme, riorganizzazione e persistenza. Non vengono usati fondi reali, profili personali o dispositivi di firma.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Interfaccia del nodo](EXCHANGE_INTEGRATION.html) · [API RPC e HTTP](RPC_API.html) · [Gestione del nodo](NETWORK_RUNBOOK.html) · [Note di versione](RELEASE_NOTES.html) · [Verifica](EXCHANGE_EXAMPLES.html)

[Riferimento esteso in inglese](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Commissioni, transazione verificata e compatibilità

La commissione è la somma degli input meno la somma degli output. La stima include un output di resto soltanto se il portafoglio crea effettivamente un resto sufficiente. Un residuo inferiore alla soglia del portafoglio viene aggiunto alla commissione; la commissione risultante e l’addebito totale sono mostrati per la verifica. La tariffa è espressa in yugeon/vB. La dimensione virtuale è il peso della transazione diviso per quattro e arrotondato per eccesso.

Il portafoglio sceglie input e output una sola volta e firma quello stesso piano di transazione. La conferma invia la transazione firmata conservata, senza ricostruirla né ricalcolare la commissione. Una stima scaduta o input già spesi richiedono una nuova verifica. L’accettazione nella coda locale non equivale alla conferma in un blocco.

Per i normali pagamenti P2WPKH, il portafoglio genera firme low-R e low-S lunghe al massimo 71 byte, incluso il byte SIGHASH_ALL. È una politica di firma e di stima delle dimensioni, non un nuovo limite di consenso per altre firme valide. Una firma più corta può ridurre la dimensione virtuale effettiva. Le tariffe suggerite dipendono ancora dalla coda locale: seguire un calcolo delle dimensioni simile a Bitcoin non significa adottare le tariffe della rete Bitcoin.

## Componente I2P di Windows e controlli di sicurezza

I pacchetti Windows includono i2pd 3.0.0 ufficiale con hash e certificati per il collegamento iniziale aggiornati. Nel controllo registrato, Defender continua a rilevare l’eseguibile I2P e lo ZIP ufficiali. La corrispondenza con l’hash ufficiale non dimostra la sicurezza né conferma un falso positivo. Un’esclusione locale riguarda solo il PC su cui viene impostata; il pacchetto pubblico non la configura. Altri computer possono bloccare gli stessi file.

<!-- /payment-policy-20261116 -->
