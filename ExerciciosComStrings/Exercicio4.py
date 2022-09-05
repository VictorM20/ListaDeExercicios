"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""
nome = input('Digite seu nome: ')

for i in range(1, len(nome) + 1):
    for j in range(0, i):
        print(nome[j], end='')
    print('')