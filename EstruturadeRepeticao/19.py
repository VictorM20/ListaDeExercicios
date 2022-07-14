"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
from math import inf #Constante 'infinito'

numeros = []
while True:
    valor = input('Digite um número entre 0 e 1000: ')
    if valor.upper() == "P":
        break
    valor = float(valor)
    if valor >= 0 or valor <= 1000:
        print('Digite apenas números entre 0 e 1000!')
        continue
    numeros.append(valor)

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