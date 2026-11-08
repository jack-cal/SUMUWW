# SUMUWW · Notas de versión

El nodo suele abrir 10 conexiones salientes. La mayoría retransmite bloques y transacciones. Puede usar una conexión de respaldo verificada para los bloques y abrir brevemente una conexión más para descubrir otros nodos. El límite total es de 125. Admite hasta 117 conexiones entrantes, o 115 si hay 10 salientes. La aplicación de escritorio ahora muestra solo el número total de nodos conectados. Cada dispositivo minero construye sus propios bloques. El nodo de PC retransmite los bloques completos y rechaza las solicitudes de trabajo minero y las soluciones enviadas por el móvil.


SUMUWW PC 0.57.53 · El nodo valida, guarda, retransmite y permite consultar la cadena.

## Formato de firma

El SDK opcional de código fuente construye transacciones y verifica firmas recibidas sin claves ni red. No es un firmador ni un comando del nodo. La limitación P2WPKH corresponde al formato del ejemplo, no al nodo. La cartera personal existente sigue disponible.

## API RPC y HTTP

validateaddress comprueba la suma de verificación y la red seleccionada. decoderawtransaction devuelve decoded_only, sin certificar firmas ni confirmaciones. Las salidas OP_RETURN conservan datos para programas externos. El nodo incorpora consultas de comisiones, comprobaciones previas al envío, estado de sustituciones RBF y registros de datos ordenados por bloque. Se valida la sustitución antes de eliminar transacciones pendientes. Las firmas múltiples y las salidas bloqueadas están implementadas para pruebas aisladas; aún no están activadas en la red pública.

## Verificación

Ejecute python examples/node_contract.py desde el código fuente con sus dependencias. Claves públicas de prueba y un regtest temporal verifican envío, rechazo, confirmaciones, reorganización y persistencia. No se usan fondos reales, perfiles personales ni firmadores físicos.

[Documentación](README.html) · [Interfaz del nodo](EXCHANGE_INTEGRATION.html) · [API RPC y HTTP](RPC_API.html) · [Operación del nodo](NETWORK_RUNBOOK.html) · [Verificación](EXCHANGE_EXAMPLES.html)

[Referencia ampliada en inglés](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
