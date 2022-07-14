"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""
from math import inf
while True:
    i = 1
    total = 0
    temp = 0
    menor_temp = inf
    maior_temp = -inf
    while i >= 0:
        temp = input(f'Digite a {i}ªtemperatura ou "s" para sair: ')
        if temp.upper() == "S":
            break
        temp = float(temp)
        total += temp

        if temp < menor_temp:
            menor_temp = temp
        if temp > maior_temp:
            maior_temp = temp
        i += 1
    media_temp = total / i
    print(f'A média de temperaturas é {media_temp:.2f}')
    print(f'A menor temperatura é {menor_temp}')
    print(f'A maior temperatura é {maior_temp}')
    res = input('\n '
                'Deseja sair do programa [S]im ou [N]ão: ')
    if res.upper() == 'S':
        print('Finalizando programa!')
        break
    else:
        continue