"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
qtd_cds = int(input('Digite a quantidade de CDs: '))
i = 1
total_valor = 0
while i <= qtd_cds:
    valor = float(input(f'Digite o valor do {i}° CD: '))
    total_valor += valor
    i += 1
media_valor = total_valor / qtd_cds
print(f'O valor total investido na sua coleção de CDs é  de R${total_valor:.2f}')
print(f'O preço médio de cada CDs é de R${media_valor:.2f}')