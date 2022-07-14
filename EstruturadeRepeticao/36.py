"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
"""
num_tabuada = int(input('Digite o número para a tabuada: '))
num_start = int(input('Digite o número para iniciar a tabuada no: '))
num_stop = int(input('Digite o número para finalizar a tabuada no: '))

print(f'Montar a tabuada de: {num_tabuada}')
print(f'Começar por: {num_start}')
print(f'Terminar em: {num_stop}')
print(f'Vou montar a tabuada de {num_tabuada} começando em {num_start} e terminando em {num_stop}:')
for i in range(num_start,num_stop +1):
    res = num_tabuada * i
    print(f'{num_tabuada} X {i} = {res}')