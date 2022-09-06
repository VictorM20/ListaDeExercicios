"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone,
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

print('Validador de número de Telefone')
newnumber = ''
number = int(input('Digite um número de telefone: '))
if len(str(number)) < 8:
    dif = 8 - len(str(number))
    newnumber = '3' * dif

numberFormat = newnumber + str(number)
numberFormat = numberFormat[0:4] + '-' + numberFormat[4:]

print('Telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(number)))
print('Telefone corrigido sem formatação: %d' % number)
print('Telefone corrigido com formatação: %s' % numberFormat)
