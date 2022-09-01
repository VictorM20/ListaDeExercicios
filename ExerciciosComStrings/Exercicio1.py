"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

"""


def tamanho(string, string2):
    a = len(string)
    b = len(string2)
    if a == b:
        return 'As duas strings são de tamanhos iguais.'
    else:
        return 'As duas strings são de tamanhos diferentes'


def comparar(string, string2):
    if string == string2:
        return 'As duas string possuem conteúdo iguais.'
    else:
        return 'As duas string possuem conteúdo diferentes.'


string = input('Digite alguma coisa: ')
string2 = input('Digite alguma coisa: ')
print()
print('Compara duas strings')
print(f'String 1: {string}')
print(f'String 2: {string2}')
print(f'Tamanho de {string}: {len(string)} caracteres')
print(f'Tamanho de {string}: {len(string2)} caracteres')
print(tamanho(string, string2))
print(comparar(string, string2))
