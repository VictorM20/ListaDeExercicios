"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""

vetor = []
for i in range(5):
    try:
        vetor.append(int(input('Digite um número: ')))
    except:
        print('Digite um número inteiro!')
        vetor.append(int(input('Digite um número: ')))
print(vetor)
