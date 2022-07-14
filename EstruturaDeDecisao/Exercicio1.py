"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print(f'O número {num1} é maior que o {num2}.')
else:
    print(f'O número {num2} é maior que o {num1}.')