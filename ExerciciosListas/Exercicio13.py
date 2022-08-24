"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
temp = []
for i in range(1, 13):
    temp.append(float(input('Digite a temperatura %d° mês: ' % i)))

media = sum(temp) / 12

i = 0
meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
print('Meses com tempuratura acima da médial anual:')
for j in temp:
    if j > media:
        print(f'{meses_ano[i]}')

    i += 1
