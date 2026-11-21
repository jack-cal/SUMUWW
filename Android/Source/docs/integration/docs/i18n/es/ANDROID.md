# SUMUWW Android 0.7.8 · Documentación

SUMUWW Android 0.7.8 · El nodo valida, guarda, retransmite y permite consultar la cadena.

## Red y direcciones

La red pública es `sumuww`; `dora` es su alias interno. Compruebe el hash de génesis indicado abajo. Las direcciones nativas usan P2WPKH witness v0 y HASH160 de una clave pública secp256k1 comprimida. No hay memo ni etiqueta obligatorios. Rechace direcciones de otra red o con suma de comprobación inválida. Registre la rama HD de recepción/cambio y el índice; no suponga la ruta de derivación de Bitcoin.

## Importes y salidas disponibles

`_units` son unidades mínimas enteras; `_smw` es una cadena de 8 decimales; `_dora` es un alias de compatibilidad. No existe un campo monetario `_sumuww`. 1 SMW = 100000000 unidades. `gettxout` no tiene `spendable` y puede devolver recompensas inmaduras. Una coinbase necesita al menos 100 confirmaciones para gastarse en el siguiente bloque. Filtre `listunspent` por `spendable`; el importe available de `getaddressbalance` excluye fondos inmaduros y comprometidos en gastos pendientes. Las nuevas salidas del mempool no están confirmadas. Compruebe la punta entre páginas y revalide las entradas elegidas.

1 SMW = 100.000.000 yugeon. Las tarifas automáticas ofrecen tres niveles según las observaciones locales, sin garantizar el tiempo de confirmación. Puedes introducir una tarifa en yugeon/vB. Revisa la comisión final y el total en SMW antes de enviar. Una transacción rechazada no descuenta saldo.

Con una entrada de 1 SMW, la comisión depende de si hay que devolver cambio. Si todas las entradas y salidas son P2WPKH y la tarifa es de 1 yugeon/vB, enviar 0.99999890 SMW cuesta 110 yugeon y no queda cambio. Si envías 0.8 SMW con la misma entrada, se añade una salida de cambio y la comisión asciende a 141 yugeon. La cartera devuelve el cambio si lo que queda después de pagar la comisión alcanza un mínimo que tiene en cuenta el coste de gastar ese cambio más adelante. Si queda menos, el resto se incluye en la comisión que ves antes de confirmar. Para una entrada de la cartera que usa SegWit nativo (P2WPKH), el cálculo reserva hasta 71 bytes para la firma, incluido el tipo de hash.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

La tarifa automática considera el volumen pendiente, la capacidad de los bloques y la prioridad de las transacciones. No usa tarifas de bloques anteriores. Con poca espera mantiene la tarifa mínima. La vista previa se actualiza; la confirmación final fija la tarifa. Los datos corresponden al nodo local conectado, no a todos los nodos.

El historial de sustituciones registrado por este nodo se conserva al reiniciar la cartera. Las transacciones retiradas no afectan al saldo.

El historial de minería separa la nueva emisión, las comisiones y la recompensa total de cada bloque. El importe recibido por tu cartera se muestra por separado. Si la recompensa se reclama parcialmente, no se inventa un reparto entre sus componentes. El nodo ofrece 28 métodos RPC, incluida la estimación de comisiones, y valida y retransmite transacciones firmadas.

## Consulta de transacciones y bloques

`getrawtransaction` busca en la cadena activa y el mempool, no transacciones exclusivamente huérfanas. Las entradas identifican salidas anteriores, no un remitente único. `getblock` acepta `verbose` booleano; los bloques inactivos guardados tienen `active=false` y `confirmations=-1`. Sus transacciones en bruto siguen accesibles por hash de bloque. `findspendingtransaction` solo busca gastos confirmados de la cadena activa; null no demuestra disponibilidad. Compruebe `gettxout` con `include_mempool=true`. Confirmaciones y estado activo pueden cambiar tras una reorganización.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Comisiones, transacción revisada y compatibilidad

La comisión es la suma de las entradas menos la suma de las salidas. La estimación solo incluye una salida de cambio cuando el monedero realmente va a crear un cambio suficiente. Si el sobrante no alcanza el umbral del monedero, se añade a la comisión; antes de confirmar se muestran la comisión resultante y el débito total. La tarifa se expresa en yugeon/vB. El tamaño virtual es el peso de la transacción dividido entre cuatro, redondeado hacia arriba.

El monedero selecciona las entradas y las salidas una sola vez y firma ese mismo plan. Al confirmar, envía la transacción firmada que conserva, sin reconstruirla ni recalcular la comisión. Si la estimación caduca o alguna entrada ya se ha gastado, hay que revisarla de nuevo. La aceptación en la cola local no equivale a una confirmación en un bloque.

En pagos P2WPKH normales, el monedero genera firmas low-R y low-S de hasta 71 bytes, incluido el byte SIGHASH_ALL. Es una política de firma y estimación, no un nuevo límite de consenso para otras firmas válidas. Una firma más corta puede reducir el tamaño virtual real. 

## Compatibilidad de firmas en Android

El formato de los archivos del monedero, las direcciones y las monedas existentes no cambian. Puede restaurar la copia cifrada anterior en la nueva aplicación y seguir usando el mismo monedero. El nodo Android 0.6.103 y el monedero 1.1.14 usan una nueva clave de firma de publicación. No pueden sustituir una instalación firmada con otra clave. Conserve la aplicación anterior y sus datos hasta disponer de una copia cifrada del monedero y de un método de recuperación que funcione. No desinstale la aplicación antigua solo para forzar la instalación.

<!-- /payment-policy-20261116 -->

Tras recibir una respuesta de versión válida, el nodo da tiempo al otro nodo para enviar la confirmación. Si dos conexiones salientes llegan al mismo nodo, mantiene una vía disponible hasta que una de ellas se sincroniza.

<!-- poll-recovery-20261119 -->

La actualización de la sincronización se vuelve a intentar tras un error interno. Un error en un par ya no detiene las actualizaciones de los demás. La minería sigue requiriendo un par verificado recientemente; mantener una conexión abierta no basta. Al iniciar la minería en el móvil, se espera a que termine la sincronización en lugar de detenerse de inmediato. Se corrigieron los bloqueos de red al verificar pruebas de conexión y consultar el historial. La minería en segundo plano sigue activa.
