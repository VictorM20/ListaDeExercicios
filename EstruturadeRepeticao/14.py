"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

par = 0
impar = 0
cont = 1
while cont < 11:
    num = int(input(f'Digite o {cont}° número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    cont += 1
print('Total de números parses: ', par)
print('Total de números impares: ', impar)
