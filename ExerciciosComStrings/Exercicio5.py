"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F

"""
nome = input('Digite seu nome: ')

for i in range(len(nome), 0, - 1):
    for j in range(0, i):
        print(nome[j], end='')
    print('')
