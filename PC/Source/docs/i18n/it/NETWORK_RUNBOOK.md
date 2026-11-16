# SUMUWW · Gestione del nodo

Il nodo apre normalmente 10 connessioni in uscita. La maggior parte inoltra blocchi e transazioni. Può usare una connessione di riserva verificata per i blocchi e aprirne brevemente un’undicesima per cercare altri nodi. Il limite complessivo è 125. Sono ammesse fino a 117 connessioni in ingresso, o 115 con 10 in uscita. L’app per computer ora mostra solo il numero totale di nodi connessi. Ogni dispositivo di mining costruisce i propri blocchi. Il nodo su PC inoltra i blocchi completi e rifiuta le richieste di lavoro e le soluzioni di mining inviate dal telefono.

Al riavvio il nodo riparte dall’ultimo blocco verificato localmente e controlla i nuovi blocchi. Se la verifica salvata manca o i dati non corrispondono, ricontrolla la cronologia archiviata.


SUMUWW PC 0.57.61 · Il nodo verifica, conserva, inoltra e rende consultabili i dati della catena.

## Rete e indirizzi

La rete pubblica è `sumuww`, con alias interno `dora`. Verificare l’hash di genesi qui sotto. Gli indirizzi nativi usano P2WPKH witness v0 e HASH160 di una chiave pubblica secp256k1 compressa. Nessun memo o tag obbligatorio. Rifiutare rete errata e checksum non validi. Registrare ramo HD ricezione/resto e indice; non presumere il percorso di derivazione Bitcoin.

## Autenticazione e limiti

Abilitare esplicitamente RPC sul loopback numerico `127.0.0.1:18443` con token Bearer privato. Nessuno sblocco del portafoglio o firma remota è esposto. Usare un servizio locale o tunnel autenticato; richieste browser Origin/Referer respinte. JSON-RPC usa POST `/rpc`, `params` oggetto/array e `id`; notifiche con HTTP 204. Limiti: corpo 8004096 byte, intestazioni 8192, batch 16, richieste simultanee 16, scadenza 10 secondi; limit 1–1000, offset 0–1000000. Sono disponibili 28 metodi e 11 percorsi REST.

## Ricerca di transazioni e blocchi

`getrawtransaction` cerca nella catena attiva e nel mempool, non transazioni presenti solo in rami orfani. Gli input indicano output precedenti, non un mittente univoco. `getblock` richiede `verbose` booleano; blocchi inattivi salvati hanno `active=false` e `confirmations=-1`. Le transazioni grezze restano accessibili tramite hash del blocco. `findspendingtransaction` cerca solo spese attive confermate; null non prova disponibilità. Verificare `gettxout` con `include_mempool=true`. Conferme e stato attivo possono cambiare dopo riorganizzazione.

## Verifica

Installate le dipendenze, eseguire python examples/node_contract.py dai sorgenti. Chiavi pubbliche di prova e regtest temporaneo verificano invio, rifiuto, conferme, riorganizzazione e persistenza. Non vengono usati fondi reali, profili personali o dispositivi di firma.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Documentazione](README.html) · [Interfaccia del nodo](EXCHANGE_INTEGRATION.html) · [API RPC e HTTP](RPC_API.html) · [Note di versione](RELEASE_NOTES.html) · [Verifica](EXCHANGE_EXAMPLES.html)

[Riferimento esteso in inglese](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Commissioni, transazione verificata e compatibilità

La commissione è la somma degli input meno la somma degli output. La stima include un output di resto soltanto se il portafoglio crea effettivamente un resto sufficiente. Un residuo inferiore alla soglia del portafoglio viene aggiunto alla commissione; la commissione risultante e l’addebito totale sono mostrati per la verifica. La tariffa è espressa in yugeon/vB. La dimensione virtuale è il peso della transazione diviso per quattro e arrotondato per eccesso.

Il portafoglio sceglie input e output una sola volta e firma quello stesso piano di transazione. La conferma invia la transazione firmata conservata, senza ricostruirla né ricalcolare la commissione. Una stima scaduta o input già spesi richiedono una nuova verifica. L’accettazione nella coda locale non equivale alla conferma in un blocco.

Per i normali pagamenti P2WPKH, il portafoglio genera firme low-R e low-S lunghe al massimo 71 byte, incluso il byte SIGHASH_ALL. È una politica di firma e di stima delle dimensioni, non un nuovo limite di consenso per altre firme valide. Una firma più corta può ridurre la dimensione virtuale effettiva. Le tariffe suggerite dipendono ancora dalla coda locale: seguire un calcolo delle dimensioni simile a Bitcoin non significa adottare le tariffe della rete Bitcoin.

## Componente I2P di Windows e controlli di sicurezza

I pacchetti Windows includono i2pd 3.0.0 ufficiale con hash e certificati per il collegamento iniziale aggiornati. Nel controllo registrato, Defender continua a rilevare l’eseguibile I2P e lo ZIP ufficiali. La corrispondenza con l’hash ufficiale non dimostra la sicurezza né conferma un falso positivo. Un’esclusione locale riguarda solo il PC su cui viene impostata; il pacchetto pubblico non la configura. Altri computer possono bloccare gli stessi file.

<!-- /payment-policy-20261116 -->

Dopo una risposta di versione valida, il nodo lascia al suo interlocutore il tempo di inviare la conferma. Se due connessioni in uscita raggiungono lo stesso nodo, un percorso disponibile resta aperto finché una delle due completa la sincronizzazione. La diagnostica integrata accetta un blocco con prova di lavoro valida prima di ricevere la prova di connessione. Verifica poi le firme dei tre testimoni, la propagazione della prova e la sua conservazione dopo il riavvio.
