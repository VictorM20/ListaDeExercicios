"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de
itens que o cliente comprou e ao lado o valor da conta.
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos.
"""
print('Lojas Quase Dois - Tabela de preços')
i = 1
for i in range(1,51):
    res = 1.99 * i
    print(f'{i} - R$ {res:.2f}')