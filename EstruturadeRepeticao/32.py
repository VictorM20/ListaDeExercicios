"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""
import math
numero = int(input("\nDigite o numero que quer realizar a fatorial : "))
count = numero
fatorial = math.factorial(numero)
for i in range(numero - 1):
    print(count, end=" . ")
    count -= 1
print("1 = ", fatorial)