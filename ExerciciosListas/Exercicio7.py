"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
import math
vetor = []
for i in range(5):
    vetor.append(int(input('Digite o número: ')))

soma = sum(vetor)
produto = math.prod(vetor)
print(f'Números do vetor: {vetor}')
print(f'Números do vetor somados: {soma}')
print(f'Números do vetor multiplicados: {produto}')