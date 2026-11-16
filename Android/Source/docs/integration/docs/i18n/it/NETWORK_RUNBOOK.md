# SUMUWW Android 0.6.103 · Gestione del nodo

Al riavvio il nodo riparte dall’ultimo blocco verificato localmente e controlla i nuovi blocchi. Se la verifica salvata manca o i dati non corrispondono, ricontrolla la cronologia archiviata.

SUMUWW Android 0.6.103 · Il nodo verifica, conserva, inoltra e rende consultabili i dati della catena.

## Rete e indirizzi

La rete pubblica è `sumuww`, con alias interno `dora`. Verificare l’hash di genesi qui sotto. Gli indirizzi nativi usano P2WPKH witness v0 e HASH160 di una chiave pubblica secp256k1 compressa. Nessun memo o tag obbligatorio. Rifiutare rete errata e checksum non validi. Registrare ramo HD ricezione/resto e indice; non presumere il percorso di derivazione Bitcoin.

## Ricerca di transazioni e blocchi

`getrawtransaction` cerca nella catena attiva e nel mempool, non transazioni presenti solo in rami orfani. Gli input indicano output precedenti, non un mittente univoco. `getblock` richiede `verbose` booleano; blocchi inattivi salvati hanno `active=false` e `confirmations=-1`. Le transazioni grezze restano accessibili tramite hash del blocco. `findspendingtransaction` cerca solo spese attive confermate; null non prova disponibilità. Verificare `gettxout` con `include_mempool=true`. Conferme e stato attivo possono cambiare dopo riorganizzazione.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Commissioni, transazione verificata e compatibilità

La commissione è la somma degli input meno la somma degli output. La stima include un output di resto soltanto se il portafoglio crea effettivamente un resto sufficiente. Un residuo inferiore alla soglia del portafoglio viene aggiunto alla commissione; la commissione risultante e l’addebito totale sono mostrati per la verifica. La tariffa è espressa in yugeon/vB. La dimensione virtuale è il peso della transazione diviso per quattro e arrotondato per eccesso.

Il portafoglio sceglie input e output una sola volta e firma quello stesso piano di transazione. La conferma invia la transazione firmata conservata, senza ricostruirla né ricalcolare la commissione. Una stima scaduta o input già spesi richiedono una nuova verifica. L’accettazione nella coda locale non equivale alla conferma in un blocco.

Per i normali pagamenti P2WPKH, il portafoglio genera firme low-R e low-S lunghe al massimo 71 byte, incluso il byte SIGHASH_ALL. È una politica di firma e di stima delle dimensioni, non un nuovo limite di consenso per altre firme valide. Una firma più corta può ridurre la dimensione virtuale effettiva. Le tariffe suggerite dipendono ancora dalla coda locale: seguire un calcolo delle dimensioni simile a Bitcoin non significa adottare le tariffe della rete Bitcoin.

## Compatibilità della firma Android

Il formato dei file del portafoglio, gli indirizzi e le monete esistenti non sono cambiati. Il precedente backup cifrato può essere ripristinato nella nuova app per continuare a usare lo stesso portafoglio. Il nodo Android 0.6.103 e il portafoglio 1.1.14 utilizzano una nuova chiave di firma delle versioni. Non possono sostituire un’installazione firmata con una chiave diversa. Conservate la vecchia app e i suoi dati finché non disponete di un backup cifrato del portafoglio e di un metodo di ripristino funzionante. Non disinstallate la vecchia app soltanto per forzare l’aggiornamento.

<!-- /payment-policy-20261116 -->

Dopo una risposta di versione valida, il nodo lascia al suo interlocutore il tempo di inviare la conferma. Se due connessioni in uscita raggiungono lo stesso nodo, un percorso disponibile resta aperto finché una delle due completa la sincronizzazione. La diagnostica integrata accetta un blocco con prova di lavoro valida prima di ricevere la prova di connessione. Verifica poi le firme dei tre testimoni, la propagazione della prova e la sua conservazione dopo il riavvio.
