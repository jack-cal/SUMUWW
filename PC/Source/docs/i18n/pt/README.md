# SUMUWW · Documentação

Com uma entrada de 1 SMW, a taxa depende de ser preciso devolver troco. Se as entradas e saídas forem P2WPKH e a taxa por tamanho for de 1 yugeon/vB, enviar 0.99999890 SMW custa 110 yugeon e não há troco. Enviar 0.8 SMW com a mesma entrada acrescenta uma saída de troco e eleva a taxa para 141 yugeon. A carteira devolve o troco se o valor restante após a taxa atingir um mínimo que tem em conta o custo de gastar esse troco mais tarde. Se ficar abaixo desse mínimo, o valor restante é incluído na taxa apresentada antes da confirmação. Para uma entrada da carteira em SegWit nativo (P2WPKH), a estimativa reserva até 71 bytes para a assinatura, incluindo o tipo de hash.

SUMUWW PC 0.57.51 · O nó valida, guarda, retransmite e permite consultar a cadeia.

## Formato de assinatura

O SDK opcional no código-fonte monta transações e verifica assinaturas recebidas sem chaves nem rede. Não é um assinador nem um comando do nó. A limitação P2WPKH pertence ao formato do exemplo, não ao nó. A carteira pessoal existente continua disponível.

## API RPC e HTTP

validateaddress verifica a soma de verificação e a rede escolhida. decoderawtransaction retorna decoded_only, sem comprovar assinatura ou confirmação. As saídas OP_RETURN preservam dados para programas externos. O nó inclui consultas de taxas, verificação antes do envio, estado de substituições RBF e leitura ordenada dos dados dos blocos. A substituição é validada antes de remover transações pendentes. As assinaturas múltiplas e as saídas bloqueadas estão implementadas para testes isolados; ainda não estão ativas na rede pública.

## Verificação

Execute python examples/node_contract.py no código-fonte com as dependências instaladas. Chaves públicas de teste e regtest temporário verificam envio, rejeição, confirmações, reorganização e persistência. Não são usados fundos reais, perfis pessoais nem assinadores físicos.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Interface do nó](EXCHANGE_INTEGRATION.html) · [API RPC e HTTP](RPC_API.html) · [Operação do nó](NETWORK_RUNBOOK.html) · [Notas da versão](RELEASE_NOTES.html) · [Verificação](EXCHANGE_EXAMPLES.html)

[Referência detalhada em inglês](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Taxas, transação conferida e compatibilidade

A taxa corresponde à soma das entradas menos a soma das saídas. A estimativa só inclui uma saída de troco quando a carteira realmente cria um troco acima do limite definido. Um valor restante abaixo desse limite é incorporado à taxa; a taxa resultante e o débito total são exibidos para conferência. A tarifa é expressa em yugeon/vB. O tamanho virtual é o peso da transação dividido por quatro, arredondado para cima.

A carteira seleciona as entradas e as saídas uma única vez e assina esse mesmo plano. A confirmação envia a transação assinada que foi armazenada, sem reconstruí-la nem recalcular a taxa. Uma estimativa vencida ou entradas já gastas exigem nova conferência. A aceitação na fila local não equivale à confirmação em um bloco.

Nos pagamentos P2WPKH comuns, a carteira gera assinaturas low-R e low-S de até 71 bytes, incluindo o byte SIGHASH_ALL. Essa é uma política de assinatura e estimativa, não um novo limite de consenso para outras assinaturas válidas. Assinaturas menores podem reduzir o tamanho virtual real. 

<!-- /payment-policy-20261116 -->
