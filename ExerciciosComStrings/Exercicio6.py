"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

data = input('Digite uma data por extenso.(DD/MM/AAAA): ')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6::])

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

novaData = str(dia) + ' de ' + meses[mes - 1] + ' de ' + str(ano)

print(novaData)
