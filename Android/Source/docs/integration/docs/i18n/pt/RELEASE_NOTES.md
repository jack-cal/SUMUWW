# SUMUWW Android 0.6.103 · Notas da versão

Com uma entrada de 1 SMW, a taxa depende de ser preciso devolver troco. Se as entradas e saídas forem P2WPKH e a taxa por tamanho for de 1 yugeon/vB, enviar 0.99999890 SMW custa 110 yugeon e não há troco. Enviar 0.8 SMW com a mesma entrada acrescenta uma saída de troco e eleva a taxa para 141 yugeon. A carteira devolve o troco se o valor restante após a taxa atingir um mínimo que tem em conta o custo de gastar esse troco mais tarde. Se ficar abaixo desse mínimo, o valor restante é incluído na taxa apresentada antes da confirmação. Para uma entrada da carteira em SegWit nativo (P2WPKH), a estimativa reserva até 71 bytes para a assinatura, incluindo o tipo de hash.

Ao reiniciar, o nó retoma a partir do último bloco que verificou localmente e verifica os novos blocos. Se o registro de verificação salvo estiver ausente ou inconsistente, o nó verifica novamente o histórico armazenado.

SUMUWW Android 0.6.103 · O nó valida, guarda, retransmite e permite consultar a cadeia.

A especificação API descreve o núcleo do nó integrado. O aplicativo Android não tem tela de configuração RPC.

## API RPC e HTTP

validateaddress verifica a soma de verificação e a rede escolhida. decoderawtransaction retorna decoded_only, sem comprovar assinatura ou confirmação. As saídas OP_RETURN preservam dados para programas externos. O nó inclui consultas de taxas, verificação antes do envio, estado de substituições RBF e leitura ordenada dos dados dos blocos. A substituição é validada antes de remover transações pendentes. As assinaturas múltiplas e as saídas bloqueadas estão implementadas para testes isolados; ainda não estão ativas na rede pública.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Taxas, transação conferida e compatibilidade

A taxa corresponde à soma das entradas menos a soma das saídas. A estimativa só inclui uma saída de troco quando a carteira realmente cria um troco acima do limite definido. Um valor restante abaixo desse limite é incorporado à taxa; a taxa resultante e o débito total são exibidos para conferência. A tarifa é expressa em yugeon/vB. O tamanho virtual é o peso da transação dividido por quatro, arredondado para cima.

A carteira seleciona as entradas e as saídas uma única vez e assina esse mesmo plano. A confirmação envia a transação assinada que foi armazenada, sem reconstruí-la nem recalcular a taxa. Uma estimativa vencida ou entradas já gastas exigem nova conferência. A aceitação na fila local não equivale à confirmação em um bloco.

Nos pagamentos P2WPKH comuns, a carteira gera assinaturas low-R e low-S de até 71 bytes, incluindo o byte SIGHASH_ALL. Essa é uma política de assinatura e estimativa, não um novo limite de consenso para outras assinaturas válidas. Assinaturas menores podem reduzir o tamanho virtual real. 

## Compatibilidade da assinatura no Android

O formato dos arquivos da carteira, os endereços e as moedas existentes não mudaram. O backup criptografado anterior pode ser restaurado no novo aplicativo para continuar usando a mesma carteira. O nó Android 0.6.103 e a carteira 1.1.14 usam uma nova chave de assinatura de distribuição. Não podem substituir uma instalação assinada com outra chave. Mantenha o aplicativo antigo e seus dados até obter um backup criptografado da carteira e um método de recuperação funcional. Não desinstale o aplicativo antigo apenas para forçar a instalação da atualização.

<!-- /payment-policy-20261116 -->
