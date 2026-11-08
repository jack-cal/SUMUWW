# SUMUWW Android 0.6.98 · Notas de versión

El teléfono se conecta a un nodo completo de SUMUWW con la versión 0.57.49 o posterior. Comprueba la recompensa y calcula la prueba de trabajo sin descargar todo el historial de transacciones.

La especificación API describe el núcleo del nodo integrado. La aplicación Android no tiene pantalla de configuración RPC.

## API RPC y HTTP

validateaddress comprueba la suma de verificación y la red seleccionada. decoderawtransaction devuelve decoded_only, sin certificar firmas ni confirmaciones. Las salidas OP_RETURN conservan datos para programas externos. El nodo incorpora consultas de comisiones, comprobaciones previas al envío, estado de sustituciones RBF y registros de datos ordenados por bloque. Se valida la sustitución antes de eliminar transacciones pendientes. Las firmas múltiples y las salidas bloqueadas están implementadas para pruebas aisladas; aún no están activadas en la red pública.

[API_CONTRACT.json](../../../API_CONTRACT.json)
