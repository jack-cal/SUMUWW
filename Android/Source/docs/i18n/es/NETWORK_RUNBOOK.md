# SUMUWW Android 0.6.103 · Operación del nodo

Al reiniciarse, el nodo retoma la verificación desde el último bloque que comprobó localmente y verifica los bloques nuevos. Si el registro de verificación guardado falta o es incoherente, vuelve a comprobar el historial almacenado.

SUMUWW Android 0.6.103 · El nodo valida, guarda, retransmite y permite consultar la cadena.

[Documentación](../../integration/docs/i18n/es/NETWORK_RUNBOOK.html)

<!-- payment-policy-20261116 -->

## Comisiones, transacción revisada y compatibilidad

La comisión es la suma de las entradas menos la suma de las salidas. La estimación solo incluye una salida de cambio cuando el monedero realmente va a crear un cambio suficiente. Si el sobrante no alcanza el umbral del monedero, se añade a la comisión; antes de confirmar se muestran la comisión resultante y el débito total. La tarifa se expresa en yugeon/vB. El tamaño virtual es el peso de la transacción dividido entre cuatro, redondeado hacia arriba.

El monedero selecciona las entradas y las salidas una sola vez y firma ese mismo plan. Al confirmar, envía la transacción firmada que conserva, sin reconstruirla ni recalcular la comisión. Si la estimación caduca o alguna entrada ya se ha gastado, hay que revisarla de nuevo. La aceptación en la cola local no equivale a una confirmación en un bloque.

En pagos P2WPKH normales, el monedero genera firmas low-R y low-S de hasta 71 bytes, incluido el byte SIGHASH_ALL. Es una política de firma y estimación, no un nuevo límite de consenso para otras firmas válidas. Una firma más corta puede reducir el tamaño virtual real. 

## Compatibilidad de firmas en Android

El formato de los archivos del monedero, las direcciones y las monedas existentes no cambian. Puede restaurar la copia cifrada anterior en la nueva aplicación y seguir usando el mismo monedero. El nodo Android 0.6.103 y el monedero 1.1.14 usan una nueva clave de firma de publicación. No pueden sustituir una instalación firmada con otra clave. Conserve la aplicación anterior y sus datos hasta disponer de una copia cifrada del monedero y de un método de recuperación que funcione. No desinstale la aplicación antigua solo para forzar la instalación.

<!-- /payment-policy-20261116 -->

Tras recibir una respuesta de versión válida, el nodo da tiempo al otro nodo para enviar la confirmación. Si dos conexiones salientes llegan al mismo nodo, mantiene una vía disponible hasta que una de ellas se sincroniza. 
