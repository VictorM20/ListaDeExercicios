"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
qtd = int(input('Digite a quantidade de notas a ser calculada: '))
i = 0
notas = 0
while i < qtd:
    nota = float(input('Digite a nota: '))
    notas += nota
    i += 1

media = notas / qtd
print(f'A média aritmética é {media:.2f}')