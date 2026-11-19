# SUMUWW Android 0.6.103 · Documentazione

Con un input di 1 SMW, la commissione dipende dalla presenza del resto. Se gli input e gli output sono P2WPKH e la tariffa è di 1 yugeon/vB, inviare 0.99999890 SMW costa 110 yugeon e non lascia resto. Inviare 0.8 SMW dallo stesso input aggiunge un output per il resto e porta la commissione a 141 yugeon. Il portafoglio restituisce il resto se l’importo rimasto dopo la commissione raggiunge una soglia che tiene conto del costo per spenderlo in seguito. Sotto questa soglia, il resto viene incluso nella commissione mostrata prima della conferma. Per un input del portafoglio in SegWit nativo (P2WPKH), la stima prevede fino a 71 byte per la firma, incluso il tipo di hash.

SUMUWW Android 0.6.103 · Il nodo verifica, conserva, inoltra e rende consultabili i dati della catena.

[Documentazione](../../integration/docs/i18n/it/ANDROID.html)

<!-- payment-policy-20261116 -->

## Commissioni, transazione verificata e compatibilità

La commissione è la somma degli input meno la somma degli output. La stima include un output di resto soltanto se il portafoglio crea effettivamente un resto sufficiente. Un residuo inferiore alla soglia del portafoglio viene aggiunto alla commissione; la commissione risultante e l’addebito totale sono mostrati per la verifica. La tariffa è espressa in yugeon/vB. La dimensione virtuale è il peso della transazione diviso per quattro e arrotondato per eccesso.

Il portafoglio sceglie input e output una sola volta e firma quello stesso piano di transazione. La conferma invia la transazione firmata conservata, senza ricostruirla né ricalcolare la commissione. Una stima scaduta o input già spesi richiedono una nuova verifica. L’accettazione nella coda locale non equivale alla conferma in un blocco.

Per i normali pagamenti P2WPKH, il portafoglio genera firme low-R e low-S lunghe al massimo 71 byte, incluso il byte SIGHASH_ALL. È una politica di firma e di stima delle dimensioni, non un nuovo limite di consenso per altre firme valide. Una firma più corta può ridurre la dimensione virtuale effettiva. 

## Compatibilità della firma Android

Il formato dei file del portafoglio, gli indirizzi e le monete esistenti non sono cambiati. Il precedente backup cifrato può essere ripristinato nella nuova app per continuare a usare lo stesso portafoglio. Il nodo Android 0.6.103 e il portafoglio 1.1.14 utilizzano una nuova chiave di firma delle versioni. Non possono sostituire un’installazione firmata con una chiave diversa. Conservate la vecchia app e i suoi dati finché non disponete di un backup cifrato del portafoglio e di un metodo di ripristino funzionante. Non disinstallate la vecchia app soltanto per forzare l’aggiornamento.

<!-- /payment-policy-20261116 -->

Dopo una risposta di versione valida, il nodo lascia al suo interlocutore il tempo di inviare la conferma. Se due connessioni in uscita raggiungono lo stesso nodo, un percorso disponibile resta aperto finché una delle due completa la sincronizzazione. 
