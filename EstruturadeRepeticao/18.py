"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
from math import inf #Constante 'infinito'

numeros = []
while True:
    valor = input('Digite um número: ')
    if valor.upper() == "P":
        break
    numeros.append(float(valor))

menor_num = inf
for numero in numeros:
    if numero < menor_num:
        menor_num = numero
print(f'Menor número é {menor_num}')

maior_num = -inf
for numero in numeros:
    if numero > maior_num:
        maior_num = numero
print(f'Maior número é {maior_num}')

soma = 0
for numero in numeros:
    soma += numero
print(f'Soma dos números é {soma}')

