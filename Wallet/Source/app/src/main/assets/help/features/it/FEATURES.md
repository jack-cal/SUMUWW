# SUMUWW Wallet Android 1.1.9

Il nodo apre normalmente 10 connessioni in uscita. La maggior parte inoltra blocchi e transazioni. Può usare una connessione di riserva verificata per i blocchi e aprirne brevemente un’undicesima per cercare altri nodi. Il limite complessivo è 125. Sono ammesse fino a 117 connessioni in ingresso, o 115 con 10 in uscita.


1 SMW = 100.000.000 yugeon. Le commissioni automatiche offrono tre livelli basati sulle osservazioni locali, senza garantire i tempi di conferma. Puoi inserire una tariffa in yugeon/vB. Prima di inviare, controlla commissione finale e totale in SMW. Una transazione rifiutata non riduce il saldo.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

La commissione automatica considera il volume in attesa, la capacità dei blocchi e la priorità delle transazioni. Non usa le commissioni dei blocchi passati. Con poca attesa mantiene la tariffa minima. L’anteprima si aggiorna; la conferma finale fissa la commissione. I dati riguardano il nodo locale connesso, non tutti i nodi.

La cronologia delle sostituzioni registrate da questo nodo rimane disponibile dopo il riavvio del portafoglio. Le transazioni rimosse non modificano il saldo.


La cronologia di mining distingue nuova emissione, commissioni e ricompensa totale di ogni blocco. L’importo ricevuto dal portafoglio è mostrato separatamente. Una riscossione parziale non determina la ripartizione dei due componenti. Il nodo offre 28 metodi RPC, inclusa la stima delle commissioni, e verifica e inoltra le transazioni firmate.
