"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
"""

tabuada = int(input('Digite o número da tabuada: '))
print(f'Tabuada de {tabuada}:')
for i in range(11):
    res = tabuada * i
    print(f'{tabuada} X {i} = {res}')