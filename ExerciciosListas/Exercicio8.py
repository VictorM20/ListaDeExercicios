"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
idade = []
altura = []
for i in range(5):
    idade.append(int(input('Digite sua idade: ')))
    altura.append(float(input('Digite sua altura: ')))
    print()
print(f'Ordem lida: {idade}')
print(f'Ordem lida: {altura}')
print()
idade.reverse()
altura.reverse()
print(f'Ordem inversa: {idade}')
print(f'Ordem inversa: {altura}')