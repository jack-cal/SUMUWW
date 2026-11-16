# SUMUWW Android 0.6.103 · Documentação

SUMUWW Android 0.6.103 · O nó valida, guarda, retransmite e permite consultar a cadeia.

## Rede e endereços

A rede pública é `sumuww`; `dora` é seu alias interno. Confira o hash de gênese abaixo. Endereços nativos usam P2WPKH witness v0 e HASH160 de uma chave pública secp256k1 comprimida. Não há memo ou tag obrigatórios. Rejeite endereços de outra rede e checksums inválidos. Registre ramo HD de recebimento/troco e índice; não presuma a derivação do Bitcoin.

## Valores e saídas disponíveis

`_units` representa unidades mínimas inteiras; `_smw`, texto com 8 casas decimais; `_dora`, alias de compatibilidade. Não existe campo monetário `_sumuww`. 1 SMW = 100000000 unidades. `gettxout` não tem `spendable` e pode retornar recompensas imaturas. Coinbase precisa de pelo menos 100 confirmações para gasto no próximo bloco. Filtre `listunspent` por `spendable`; o valor available de `getaddressbalance` exclui fundos imaturos e comprometidos em gastos pendentes. Novas saídas do mempool não estão confirmadas. Verifique a ponta entre páginas e revalide as entradas escolhidas.

1 SMW = 100.000.000 yugeon. As taxas automáticas oferecem três níveis com base nas observações locais, sem garantir o tempo de confirmação. Pode introduzir uma taxa em yugeon/vB. Confira a comissão final e o total em SMW antes de enviar. Uma transação rejeitada não desconta o saldo.

Com uma entrada de 1 SMW, a taxa depende de ser preciso devolver troco. Se as entradas e saídas forem P2WPKH e a taxa por tamanho for de 1 yugeon/vB, enviar 0.99999890 SMW custa 110 yugeon e não há troco. Enviar 0.8 SMW com a mesma entrada acrescenta uma saída de troco e eleva a taxa para 141 yugeon. A carteira devolve o troco se o valor restante após a taxa atingir um mínimo que tem em conta o custo de gastar esse troco mais tarde. Se ficar abaixo desse mínimo, o valor restante é incluído na taxa apresentada antes da confirmação. Para uma entrada da carteira em SegWit nativo (P2WPKH), a estimativa reserva até 71 bytes para a assinatura, incluindo o tipo de hash.


`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

A taxa automática considera o volume pendente, a capacidade dos blocos e a prioridade das transações. Não usa taxas de blocos anteriores. Com pouca espera, mantém a taxa mínima. A prévia se atualiza; a confirmação final fixa a taxa. Os dados abrangem o nó local conectado, não todos os nós.

O histórico de substituições registrado por este nó permanece após reiniciar a carteira. As transações removidas não afetam o saldo.

O histórico de mineração separa a nova emissão, as taxas e a recompensa total de cada bloco. O valor recebido pela sua carteira aparece separadamente. Uma reivindicação parcial não permite atribuir os valores de cada componente. O nó oferece 28 métodos RPC, incluindo estimativa de taxas, e valida e retransmite transações assinadas.

## Consulta de transações e blocos

`getrawtransaction` pesquisa a cadeia ativa e o mempool, não transações apenas órfãs. Entradas identificam saídas anteriores, não um remetente único. `getblock` recebe `verbose` booleano; blocos inativos armazenados têm `active=false` e `confirmations=-1`. Suas transações brutas continuam acessíveis pelo hash do bloco. `findspendingtransaction` busca apenas gastos confirmados ativos; null não prova disponibilidade. Consulte `gettxout` com `include_mempool=true`. Confirmações e estado ativo podem mudar após reorganização.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Taxas, transação conferida e compatibilidade

A taxa corresponde à soma das entradas menos a soma das saídas. A estimativa só inclui uma saída de troco quando a carteira realmente cria um troco acima do limite definido. Um valor restante abaixo desse limite é incorporado à taxa; a taxa resultante e o débito total são exibidos para conferência. A tarifa é expressa em yugeon/vB. O tamanho virtual é o peso da transação dividido por quatro, arredondado para cima.

A carteira seleciona as entradas e as saídas uma única vez e assina esse mesmo plano. A confirmação envia a transação assinada que foi armazenada, sem reconstruí-la nem recalcular a taxa. Uma estimativa vencida ou entradas já gastas exigem nova conferência. A aceitação na fila local não equivale à confirmação em um bloco.

Nos pagamentos P2WPKH comuns, a carteira gera assinaturas low-R e low-S de até 71 bytes, incluindo o byte SIGHASH_ALL. Essa é uma política de assinatura e estimativa, não um novo limite de consenso para outras assinaturas válidas. Assinaturas menores podem reduzir o tamanho virtual real. As tarifas sugeridas continuam usando a fila local; seguir o cálculo de tamanho do Bitcoin não significa adotar as tarifas daquela rede.

## Compatibilidade da assinatura no Android

O formato dos arquivos da carteira, os endereços e as moedas existentes não mudaram. O backup criptografado anterior pode ser restaurado no novo aplicativo para continuar usando a mesma carteira. O nó Android 0.6.103 e a carteira 1.1.14 usam uma nova chave de assinatura de distribuição. Não podem substituir uma instalação assinada com outra chave. Mantenha o aplicativo antigo e seus dados até obter um backup criptografado da carteira e um método de recuperação funcional. Não desinstale o aplicativo antigo apenas para forçar a instalação da atualização.

<!-- /payment-policy-20261116 -->

Depois de receber uma resposta de versão válida, o nó dá ao par tempo para enviar a confirmação. Se duas ligações de saída chegarem ao mesmo nó, mantém uma via disponível até que uma delas conclua a sincronização. O diagnóstico integrado aceita um bloco com prova de trabalho válida antes de receber a prova de conexão. Em seguida, verifica as assinaturas das três testemunhas, a propagação da prova e sua preservação após a reinicialização.
