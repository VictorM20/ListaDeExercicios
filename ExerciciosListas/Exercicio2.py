"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
vetor = []
for i in range(10):
    try:
        vetor.append(float(input('Digite um número: ')))
    except:
        print('Digite um número inteiro!')
        vetor.append(float(input('Digite um número: ')))
vetor.reverse()
print(vetor)
