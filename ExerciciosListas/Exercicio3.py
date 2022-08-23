"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas = []
for i in range(4):
    notas.append(float(input('Digite uma nota: ')))

media = sum(notas) / len(notas)
for i in notas:
    print(f'Notas: {i}')
print(f'Média: {media:.2f}')