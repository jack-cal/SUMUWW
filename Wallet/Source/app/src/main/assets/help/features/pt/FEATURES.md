# SUMUWW Wallet Android 1.1.9

O nó normalmente abre 10 conexões de saída. A maioria retransmite blocos e transações. Uma conexão de reserva já verificada pode retransmitir blocos, e uma 11ª conexão pode ser aberta por pouco tempo para descobrir outros nós. O limite total é de 125. O nó aceita até 117 conexões de entrada, ou 115 quando há 10 de saída.


1 SMW = 100.000.000 yugeon. As taxas automáticas oferecem três níveis com base nas observações locais, sem garantir o tempo de confirmação. Pode introduzir uma taxa em yugeon/vB. Confira a comissão final e o total em SMW antes de enviar. Uma transação rejeitada não desconta o saldo.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

A taxa automática considera o volume pendente, a capacidade dos blocos e a prioridade das transações. Não usa taxas de blocos anteriores. Com pouca espera, mantém a taxa mínima. A prévia se atualiza; a confirmação final fixa a taxa. Os dados abrangem o nó local conectado, não todos os nós.

O histórico de substituições registrado por este nó permanece após reiniciar a carteira. As transações removidas não afetam o saldo.


O histórico de mineração separa a nova emissão, as taxas e a recompensa total de cada bloco. O valor recebido pela sua carteira aparece separadamente. Uma reivindicação parcial não permite atribuir os valores de cada componente. O nó oferece 28 métodos RPC, incluindo estimativa de taxas, e valida e retransmite transações assinadas.
