# SUMUWW Wallet PC 1.0.15

Il nodo apre normalmente 10 connessioni in uscita. La maggior parte inoltra blocchi e transazioni. Può usare una connessione di riserva verificata per i blocchi e aprirne brevemente un’undicesima per cercare altri nodi. Il limite complessivo è 125. Sono ammesse fino a 117 connessioni in ingresso, o 115 con 10 in uscita.

1 SMW = 100.000.000 yugeon. Le commissioni automatiche offrono tre livelli basati sulle osservazioni locali, senza garantire i tempi di conferma. Puoi inserire una tariffa in yugeon/vB. Prima di inviare, controlla commissione finale e totale in SMW. Una transazione rifiutata non riduce il saldo.

Con un input di 1 SMW, la commissione dipende dalla presenza del resto. Se gli input e gli output sono P2WPKH e la tariffa è di 1 yugeon/vB, inviare 0.99999890 SMW costa 110 yugeon e non lascia resto. Inviare 0.8 SMW dallo stesso input aggiunge un output per il resto e porta la commissione a 141 yugeon. Il portafoglio restituisce il resto se l’importo rimasto dopo la commissione raggiunge una soglia che tiene conto del costo per spenderlo in seguito. Sotto questa soglia, il resto viene incluso nella commissione mostrata prima della conferma. Per un input del portafoglio in SegWit nativo (P2WPKH), la stima prevede fino a 71 byte per la firma, incluso il tipo di hash.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

La commissione automatica considera il volume in attesa, la capacità dei blocchi e la priorità delle transazioni. Non usa le commissioni dei blocchi passati. Con poca attesa mantiene la tariffa minima. L’anteprima si aggiorna; la conferma finale fissa la commissione. I dati riguardano il nodo locale connesso, non tutti i nodi.

La cronologia delle sostituzioni registrate da questo nodo rimane disponibile dopo il riavvio del portafoglio. Le transazioni rimosse non modificano il saldo.

La cronologia di mining distingue nuova emissione, commissioni e ricompensa totale di ogni blocco. L’importo ricevuto dal portafoglio è mostrato separatamente. Una riscossione parziale non determina la ripartizione dei due componenti. Il nodo offre 28 metodi RPC, inclusa la stima delle commissioni, e verifica e inoltra le transazioni firmate.

<!-- payment-policy-20261116 -->

## Commissioni, transazione verificata e compatibilità

La commissione è la somma degli input meno la somma degli output. La stima include un output di resto soltanto se il portafoglio crea effettivamente un resto sufficiente. Un residuo inferiore alla soglia del portafoglio viene aggiunto alla commissione; la commissione risultante e l’addebito totale sono mostrati per la verifica. La tariffa è espressa in yugeon/vB. La dimensione virtuale è il peso della transazione diviso per quattro e arrotondato per eccesso.

Il portafoglio sceglie input e output una sola volta e firma quello stesso piano di transazione. La conferma invia la transazione firmata conservata, senza ricostruirla né ricalcolare la commissione. Una stima scaduta o input già spesi richiedono una nuova verifica. L’accettazione nella coda locale non equivale alla conferma in un blocco.

Per i normali pagamenti P2WPKH, il portafoglio genera firme low-R e low-S lunghe al massimo 71 byte, incluso il byte SIGHASH_ALL. È una politica di firma e di stima delle dimensioni, non un nuovo limite di consenso per altre firme valide. Una firma più corta può ridurre la dimensione virtuale effettiva. 

<!-- /payment-policy-20261116 -->

Dopo una risposta di versione valida, il nodo lascia al suo interlocutore il tempo di inviare la conferma. Se due connessioni in uscita raggiungono lo stesso nodo, un percorso disponibile resta aperto finché una delle due completa la sincronizzazione. 
