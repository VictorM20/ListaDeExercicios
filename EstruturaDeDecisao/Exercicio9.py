"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

if num1 < num2:
    num1, num3 = num3, num1

if num1 < num2:
    num1, num2 = num2, num1

if num2 < num3:
    num2, num3 = num3, num2

print(f'A ordem decrescente é {num1}, {num2} e {num3}')