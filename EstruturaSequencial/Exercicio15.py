"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
sal_hora = float(input('Digite seu salário por hora: '))
hora_trab = int(input('Digite a quantidade de horas trabalhadas no mês: '))

sal_bruto = sal_hora * hora_trab
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sind = sal_bruto * 0.05
sal_liquido = sal_bruto - (ir + inss + sind)

print(f'+ Salário Bruto: R$ {sal_bruto}')
print(f'- IR (11%): R$ {ir}')
print(f'- INSS (8%): R$ {inss}')
print(f'- Sindicato (5%): R$ {sind}')
print(f'= Salário Liquido: R$ {sal_liquido}')