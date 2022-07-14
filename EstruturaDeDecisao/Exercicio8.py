"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""
produto_1 = input('Nome do produto: ')
preco_1 = float(input('Digite o preço do primeiro produto: '))
produto_2 = input('Nome do produto: ')
preco_2 = float(input('Digite o preço do segundo produto: '))
produto_3 = input('Nome do produto: ')
preco_3 = float(input('Digite o preço do terceiro produto: '))

menor = preco_1

if preco_2 < menor:
    menor = preco_2
if preco_3 < menor:
    menor = preco_3

if menor == preco_1:
    print(f'O produto ideal é o {produto_1} com valor {preco_1}.')
elif menor == preco_2:
    print(f'O produto ideal é o {produto_2} com valor {preco_2}.')
else:
    print(f'O produto ideal é o {produto_3} com valor {preco_3}.')
