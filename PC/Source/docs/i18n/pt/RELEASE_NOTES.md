# SUMUWW · Notas da versão

O nó normalmente abre 10 conexões de saída. A maioria retransmite blocos e transações. Uma conexão de reserva já verificada pode retransmitir blocos, e uma 11ª conexão pode ser aberta por pouco tempo para descobrir outros nós. O limite total é de 125. O nó aceita até 117 conexões de entrada, ou 115 quando há 10 de saída. O aplicativo para computador agora exibe apenas o número total de nós conectados. Cada dispositivo de mineração cria seus próprios blocos. O nó no PC retransmite os blocos completos e rejeita os pedidos de tarefas de mineração e as soluções enviadas pelo celular.

Ao reiniciar, o nó retoma a partir do último bloco que verificou localmente e verifica os novos blocos. Se o registro de verificação salvo estiver ausente ou inconsistente, o nó verifica novamente o histórico armazenado.


SUMUWW PC 0.57.54 · O nó valida, guarda, retransmite e permite consultar a cadeia.

## Formato de assinatura

O SDK opcional no código-fonte monta transações e verifica assinaturas recebidas sem chaves nem rede. Não é um assinador nem um comando do nó. A limitação P2WPKH pertence ao formato do exemplo, não ao nó. A carteira pessoal existente continua disponível.

## API RPC e HTTP

validateaddress verifica a soma de verificação e a rede escolhida. decoderawtransaction retorna decoded_only, sem comprovar assinatura ou confirmação. As saídas OP_RETURN preservam dados para programas externos. O nó inclui consultas de taxas, verificação antes do envio, estado de substituições RBF e leitura ordenada dos dados dos blocos. A substituição é validada antes de remover transações pendentes. As assinaturas múltiplas e as saídas bloqueadas estão implementadas para testes isolados; ainda não estão ativas na rede pública.

## Verificação

Execute python examples/node_contract.py no código-fonte com as dependências instaladas. Chaves públicas de teste e regtest temporário verificam envio, rejeição, confirmações, reorganização e persistência. Não são usados fundos reais, perfis pessoais nem assinadores físicos.

[Documentação](README.html) · [Interface do nó](EXCHANGE_INTEGRATION.html) · [API RPC e HTTP](RPC_API.html) · [Operação do nó](NETWORK_RUNBOOK.html) · [Verificação](EXCHANGE_EXAMPLES.html)

[Referência detalhada em inglês](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)
