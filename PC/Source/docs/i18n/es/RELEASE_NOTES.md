# SUMUWW · Notas de versión

Con una entrada de 1 SMW, la comisión depende de si hay que devolver cambio. Si todas las entradas y salidas son P2WPKH y la tarifa es de 1 yugeon/vB, enviar 0.99999890 SMW cuesta 110 yugeon y no queda cambio. Si envías 0.8 SMW con la misma entrada, se añade una salida de cambio y la comisión asciende a 141 yugeon. La cartera devuelve el cambio si lo que queda después de pagar la comisión alcanza un mínimo que tiene en cuenta el coste de gastar ese cambio más adelante. Si queda menos, el resto se incluye en la comisión que ves antes de confirmar. Para una entrada de la cartera que usa SegWit nativo (P2WPKH), el cálculo reserva hasta 71 bytes para la firma, incluido el tipo de hash.

0.57.61 · Al cambiar de idioma con la aplicación abierta, también cambia el icono de la barra de tareas de Windows.

El nodo suele abrir 10 conexiones salientes. La mayoría retransmite bloques y transacciones. Puede usar una conexión de respaldo verificada para los bloques y abrir brevemente una conexión más para descubrir otros nodos. El límite total es de 125. Admite hasta 117 conexiones entrantes, o 115 si hay 10 salientes. La aplicación de escritorio ahora muestra solo el número total de nodos conectados. Cada dispositivo minero construye sus propios bloques. El nodo de PC retransmite los bloques completos y rechaza las solicitudes de trabajo minero y las soluciones enviadas por el móvil.

Al reiniciarse, el nodo retoma la verificación desde el último bloque que comprobó localmente y verifica los bloques nuevos. Si el registro de verificación guardado falta o es incoherente, vuelve a comprobar el historial almacenado.

SUMUWW PC 0.57.61 · El nodo valida, guarda, retransmite y permite consultar la cadena.

## Formato de firma

El SDK opcional de código fuente construye transacciones y verifica firmas recibidas sin claves ni red. No es un firmador ni un comando del nodo. La limitación P2WPKH corresponde al formato del ejemplo, no al nodo. La cartera personal existente sigue disponible.

## API RPC y HTTP

validateaddress comprueba la suma de verificación y la red seleccionada. decoderawtransaction devuelve decoded_only, sin certificar firmas ni confirmaciones. Las salidas OP_RETURN conservan datos para programas externos. El nodo incorpora consultas de comisiones, comprobaciones previas al envío, estado de sustituciones RBF y registros de datos ordenados por bloque. Se valida la sustitución antes de eliminar transacciones pendientes. Las firmas múltiples y las salidas bloqueadas están implementadas para pruebas aisladas; aún no están activadas en la red pública.

## Verificación

Ejecute python examples/node_contract.py desde el código fuente con sus dependencias. Claves públicas de prueba y un regtest temporal verifican envío, rechazo, confirmaciones, reorganización y persistencia. No se usan fondos reales, perfiles personales ni firmadores físicos.

[Documentación](README.html) · [Interfaz del nodo](EXCHANGE_INTEGRATION.html) · [API RPC y HTTP](RPC_API.html) · [Operación del nodo](NETWORK_RUNBOOK.html) · [Verificación](EXCHANGE_EXAMPLES.html)

[Referencia ampliada en inglés](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Comisiones, transacción revisada y compatibilidad

La comisión es la suma de las entradas menos la suma de las salidas. La estimación solo incluye una salida de cambio cuando el monedero realmente va a crear un cambio suficiente. Si el sobrante no alcanza el umbral del monedero, se añade a la comisión; antes de confirmar se muestran la comisión resultante y el débito total. La tarifa se expresa en yugeon/vB. El tamaño virtual es el peso de la transacción dividido entre cuatro, redondeado hacia arriba.

El monedero selecciona las entradas y las salidas una sola vez y firma ese mismo plan. Al confirmar, envía la transacción firmada que conserva, sin reconstruirla ni recalcular la comisión. Si la estimación caduca o alguna entrada ya se ha gastado, hay que revisarla de nuevo. La aceptación en la cola local no equivale a una confirmación en un bloque.

En pagos P2WPKH normales, el monedero genera firmas low-R y low-S de hasta 71 bytes, incluido el byte SIGHASH_ALL. Es una política de firma y estimación, no un nuevo límite de consenso para otras firmas válidas. Una firma más corta puede reducir el tamaño virtual real. 

<!-- /payment-policy-20261116 -->
