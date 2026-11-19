# SUMUWW · Documentación

SUMUWW PC 0.57.51 · El nodo valida, guarda, retransmite y permite consultar la cadena.

## Formato de firma

El SDK opcional de código fuente construye transacciones y verifica firmas recibidas sin claves ni red. No es un firmador ni un comando del nodo. La limitación P2WPKH corresponde al formato del ejemplo, no al nodo. La cartera personal existente sigue disponible.

## API RPC y HTTP

validateaddress comprueba la suma de verificación y la red seleccionada. decoderawtransaction devuelve decoded_only, sin certificar firmas ni confirmaciones. Las salidas OP_RETURN conservan datos para programas externos. El nodo incorpora consultas de comisiones, comprobaciones previas al envío, estado de sustituciones RBF y registros de datos ordenados por bloque. Se valida la sustitución antes de eliminar transacciones pendientes. Las firmas múltiples y las salidas bloqueadas están implementadas para pruebas aisladas; aún no están activadas en la red pública.

## Verificación

Ejecute python examples/node_contract.py desde el código fuente con sus dependencias. Claves públicas de prueba y un regtest temporal verifican envío, rechazo, confirmaciones, reorganización y persistencia. No se usan fondos reales, perfiles personales ni firmadores físicos.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Interfaz del nodo](EXCHANGE_INTEGRATION.html) · [API RPC y HTTP](RPC_API.html) · [Operación del nodo](NETWORK_RUNBOOK.html) · [Notas de versión](RELEASE_NOTES.html) · [Verificación](EXCHANGE_EXAMPLES.html)

[Referencia ampliada en inglés](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Comisiones, transacción revisada y compatibilidad

La comisión es la suma de las entradas menos la suma de las salidas. La estimación solo incluye una salida de cambio cuando el monedero realmente va a crear un cambio suficiente. Si el sobrante no alcanza el umbral del monedero, se añade a la comisión; antes de confirmar se muestran la comisión resultante y el débito total. La tarifa se expresa en yugeon/vB. El tamaño virtual es el peso de la transacción dividido entre cuatro, redondeado hacia arriba.

El monedero selecciona las entradas y las salidas una sola vez y firma ese mismo plan. Al confirmar, envía la transacción firmada que conserva, sin reconstruirla ni recalcular la comisión. Si la estimación caduca o alguna entrada ya se ha gastado, hay que revisarla de nuevo. La aceptación en la cola local no equivale a una confirmación en un bloque.

En pagos P2WPKH normales, el monedero genera firmas low-R y low-S de hasta 71 bytes, incluido el byte SIGHASH_ALL. Es una política de firma y estimación, no un nuevo límite de consenso para otras firmas válidas. Una firma más corta puede reducir el tamaño virtual real. 

<!-- /payment-policy-20261116 -->
