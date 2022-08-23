"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
vetor = []
for i in range(10):
    vetor.append(int(input('Digite o número: ')))
for num in vetor:
    print('%d^2 = %d' % (num, (num**2)))