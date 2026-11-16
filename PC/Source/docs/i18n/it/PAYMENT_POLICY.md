# Commissioni, transazione verificata e compatibilità

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Commissioni, transazione verificata e compatibilità

La commissione è la somma degli input meno la somma degli output. La stima include un output di resto soltanto se il portafoglio crea effettivamente un resto sufficiente. Un residuo inferiore alla soglia del portafoglio viene aggiunto alla commissione; la commissione risultante e l’addebito totale sono mostrati per la verifica. La tariffa è espressa in yugeon/vB. La dimensione virtuale è il peso della transazione diviso per quattro e arrotondato per eccesso.

Il portafoglio sceglie input e output una sola volta e firma quello stesso piano di transazione. La conferma invia la transazione firmata conservata, senza ricostruirla né ricalcolare la commissione. Una stima scaduta o input già spesi richiedono una nuova verifica. L’accettazione nella coda locale non equivale alla conferma in un blocco.

Per i normali pagamenti P2WPKH, il portafoglio genera firme low-R e low-S lunghe al massimo 71 byte, incluso il byte SIGHASH_ALL. È una politica di firma e di stima delle dimensioni, non un nuovo limite di consenso per altre firme valide. Una firma più corta può ridurre la dimensione virtuale effettiva. Le tariffe suggerite dipendono ancora dalla coda locale: seguire un calcolo delle dimensioni simile a Bitcoin non significa adottare le tariffe della rete Bitcoin.

## Componente I2P di Windows e controlli di sicurezza

I pacchetti Windows includono i2pd 3.0.0 ufficiale con hash e certificati per il collegamento iniziale aggiornati. Nel controllo registrato, Defender continua a rilevare l’eseguibile I2P e lo ZIP ufficiali. La corrispondenza con l’hash ufficiale non dimostra la sicurezza né conferma un falso positivo. Un’esclusione locale riguarda solo il PC su cui viene impostata; il pacchetto pubblico non la configura. Altri computer possono bloccare gli stessi file.

## Compatibilità della firma Android

Il formato dei file del portafoglio, gli indirizzi e le monete esistenti non sono cambiati. Il precedente backup cifrato può essere ripristinato nella nuova app per continuare a usare lo stesso portafoglio. Il nodo Android 0.6.103 e il portafoglio 1.1.14 utilizzano una nuova chiave di firma delle versioni. Non possono sostituire un’installazione firmata con una chiave diversa. Conservate la vecchia app e i suoi dati finché non disponete di un backup cifrato del portafoglio e di un metodo di ripristino funzionante. Non disinstallate la vecchia app soltanto per forzare l’aggiornamento.

<!-- /payment-policy-20261116 -->

Dopo una risposta di versione valida, il nodo lascia al suo interlocutore il tempo di inviare la conferma. Se due connessioni in uscita raggiungono lo stesso nodo, un percorso disponibile resta aperto finché una delle due completa la sincronizzazione. La diagnostica integrata accetta un blocco con prova di lavoro valida prima di ricevere la prova di connessione. Verifica poi le firme dei tre testimoni, la propagazione della prova e la sua conservazione dopo il riavvio.
