"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""
num25 = []
num50 = []
num75 = []
num100 = []
num = True
while num > 0:
    num = int(input('Digite um número: '))
    if num > 0 and num <= 25:
        num25.append(num)
    elif num > 25 and num <= 50:
        num50.append(num)
    elif num > 50 and num <= 75:
        num75.append(num)
    elif num > 75 and num <= 100:
        num100.append(num)
print('Números de [0-25]: ', len(num25))
print('Números de [26-50]: ', len(num50))
print('Números de [51-75]: ', len(num75))
print('Números de [76-100]: ', len(num100))
