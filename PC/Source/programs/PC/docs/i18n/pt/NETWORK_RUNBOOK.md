# SUMUWW · Operação do nó

O nó normalmente abre 10 conexões de saída. A maioria retransmite blocos e transações. Uma conexão de reserva já verificada pode retransmitir blocos, e uma 11ª conexão pode ser aberta por pouco tempo para descobrir outros nós. O limite total é de 125. O nó aceita até 117 conexões de entrada, ou 115 quando há 10 de saída. O aplicativo para computador agora exibe apenas o número total de nós conectados. Cada dispositivo de mineração cria seus próprios blocos. O nó no PC retransmite os blocos completos e rejeita os pedidos de tarefas de mineração e as soluções enviadas pelo celular.

Ao reiniciar, o nó retoma a partir do último bloco que verificou localmente e verifica os novos blocos. Se o registro de verificação salvo estiver ausente ou inconsistente, o nó verifica novamente o histórico armazenado.

SUMUWW PC 0.57.61 · O nó valida, guarda, retransmite e permite consultar a cadeia.

## Rede e endereços

A rede pública é `sumuww`; `dora` é seu alias interno. Confira o hash de gênese abaixo. Endereços nativos usam P2WPKH witness v0 e HASH160 de uma chave pública secp256k1 comprimida. Não há memo ou tag obrigatórios. Rejeite endereços de outra rede e checksums inválidos. Registre ramo HD de recebimento/troco e índice; não presuma a derivação do Bitcoin.

## Autenticação e limites

Ative RPC explicitamente no loopback numérico `127.0.0.1:18443`, com seu token Bearer privado. Não há desbloqueio de carteira nem assinatura remota. Use serviço local ou túnel autenticado; pedidos de navegador com Origin/Referer são rejeitados. JSON-RPC usa POST `/rpc`, `params` objeto/array e `id`; notificações retornam HTTP 204. Limites: corpo 8004096 bytes, cabeçalhos 8192, lote 16, pedidos simultâneos 16, prazo 10 segundos; limit 1–1000 e offset 0–1000000. São 28 métodos e 11 rotas REST.

## Consulta de transações e blocos

`getrawtransaction` pesquisa a cadeia ativa e o mempool, não transações apenas órfãs. Entradas identificam saídas anteriores, não um remetente único. `getblock` recebe `verbose` booleano; blocos inativos armazenados têm `active=false` e `confirmations=-1`. Suas transações brutas continuam acessíveis pelo hash do bloco. `findspendingtransaction` busca apenas gastos confirmados ativos; null não prova disponibilidade. Consulte `gettxout` com `include_mempool=true`. Confirmações e estado ativo podem mudar após reorganização.

## Verificação

Execute python examples/node_contract.py no código-fonte com as dependências instaladas. Chaves públicas de teste e regtest temporário verificam envio, rejeição, confirmações, reorganização e persistência. Não são usados fundos reais, perfis pessoais nem assinadores físicos.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Documentação](README.html) · [Interface do nó](EXCHANGE_INTEGRATION.html) · [API RPC e HTTP](RPC_API.html) · [Notas da versão](RELEASE_NOTES.html) · [Verificação](EXCHANGE_EXAMPLES.html)

[Referência detalhada em inglês](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Taxas, transação conferida e compatibilidade

A taxa corresponde à soma das entradas menos a soma das saídas. A estimativa só inclui uma saída de troco quando a carteira realmente cria um troco acima do limite definido. Um valor restante abaixo desse limite é incorporado à taxa; a taxa resultante e o débito total são exibidos para conferência. A tarifa é expressa em yugeon/vB. O tamanho virtual é o peso da transação dividido por quatro, arredondado para cima.

A carteira seleciona as entradas e as saídas uma única vez e assina esse mesmo plano. A confirmação envia a transação assinada que foi armazenada, sem reconstruí-la nem recalcular a taxa. Uma estimativa vencida ou entradas já gastas exigem nova conferência. A aceitação na fila local não equivale à confirmação em um bloco.

Nos pagamentos P2WPKH comuns, a carteira gera assinaturas low-R e low-S de até 71 bytes, incluindo o byte SIGHASH_ALL. Essa é uma política de assinatura e estimativa, não um novo limite de consenso para outras assinaturas válidas. Assinaturas menores podem reduzir o tamanho virtual real. 

<!-- /payment-policy-20261116 -->

Depois de receber uma resposta de versão válida, o nó dá ao par tempo para enviar a confirmação. Se duas ligações de saída chegarem ao mesmo nó, mantém uma via disponível até que uma delas conclua a sincronização. 
