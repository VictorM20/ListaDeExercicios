"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
f = int(input('Digite uma temperatura em Fahrenheit: '))
c = 5 * ((f - 32) / 9)

print(f'Temperatura convertida em Celsius: {c:.1f}')