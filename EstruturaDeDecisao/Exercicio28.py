"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

carne = input('Digite qual carne deseja comprar [FileDuplo, Alcatra, Picanha]: ')
qtd_carne = int(input('Digite a quantidade de carne: '))
cartao = input('Possui cartão Tabajara[S/N]: ')
total = 0
desconto = 0
total_pagar = 0
if carne == 'fileduplo':
    if qtd_carne >= 5:
        preco_file = 4.90
        total = qtd_carne * preco_file
    else:
        preco_file = 5.80
        total = qtd_carne * preco_file
if carne == 'alcatra':
    if qtd_carne >= 5:
        preco_alcatra = 5.90
        total = qtd_carne * preco_alcatra
    else:
        preco_alcatra = 6.80
        total = qtd_carne * preco_alcatra
if carne == 'picanha':
    if qtd_carne >= 5:
        preco_picanha = 6.90
        total = qtd_carne * preco_picanha
    else:
        preco_picanha = 7.80
        total = qtd_carne * preco_picanha

if cartao == 'S' or cartao == 's':
    desconto = total * 0.05
    total_pagar = total - desconto
else:
    total_pagar = total

print(f'Tipo de carne: {carne}')
print(f'Quantidade de carne: {qtd_carne}')
print(f'Preço total de carne: {total}')
print(f'Tipo de pagamento: {cartao}')
print(f'Descontos: {desconto}')
print(f'Total a pagar: {total_pagar}')

