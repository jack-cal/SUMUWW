# SUMUWW Android 0.6.103 · API RPC e HTTP

SUMUWW Android 0.6.103 · O nó valida, guarda, retransmite e permite consultar a cadeia.

[Documentação](../../integration/docs/i18n/pt/RPC_API.html)

<!-- payment-policy-20261116 -->

## Taxas, transação conferida e compatibilidade

A taxa corresponde à soma das entradas menos a soma das saídas. A estimativa só inclui uma saída de troco quando a carteira realmente cria um troco acima do limite definido. Um valor restante abaixo desse limite é incorporado à taxa; a taxa resultante e o débito total são exibidos para conferência. A tarifa é expressa em yugeon/vB. O tamanho virtual é o peso da transação dividido por quatro, arredondado para cima.

A carteira seleciona as entradas e as saídas uma única vez e assina esse mesmo plano. A confirmação envia a transação assinada que foi armazenada, sem reconstruí-la nem recalcular a taxa. Uma estimativa vencida ou entradas já gastas exigem nova conferência. A aceitação na fila local não equivale à confirmação em um bloco.

Nos pagamentos P2WPKH comuns, a carteira gera assinaturas low-R e low-S de até 71 bytes, incluindo o byte SIGHASH_ALL. Essa é uma política de assinatura e estimativa, não um novo limite de consenso para outras assinaturas válidas. Assinaturas menores podem reduzir o tamanho virtual real. 

## Compatibilidade da assinatura no Android

O formato dos arquivos da carteira, os endereços e as moedas existentes não mudaram. O backup criptografado anterior pode ser restaurado no novo aplicativo para continuar usando a mesma carteira. O nó Android 0.6.103 e a carteira 1.1.14 usam uma nova chave de assinatura de distribuição. Não podem substituir uma instalação assinada com outra chave. Mantenha o aplicativo antigo e seus dados até obter um backup criptografado da carteira e um método de recuperação funcional. Não desinstale o aplicativo antigo apenas para forçar a instalação da atualização.

<!-- /payment-policy-20261116 -->
