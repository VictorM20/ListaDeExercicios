"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
hora_trab = int(input('Digite a quantidade de horas trabalhadas: '))
valor_hora = float(input('Digite o valor da sua hora trabalhada: '))

sal_bruto = hora_trab * valor_hora
inss = sal_bruto * 0.10
fgts = sal_bruto * 0.11

if sal_bruto <= 900:
    pass
elif sal_bruto <= 1500:
    ir = sal_bruto * 0.05
    perc = '5%'
elif sal_bruto <= 2500:
    ir = sal_bruto * 0.10
    perc = '10%'
else:
    ir = sal_bruto * 0.20
    perc = '20%'

total_desc = inss + ir
sal_liquido = sal_bruto - total_desc

print(f'Salário Bruto       : R$ {sal_bruto:.2f}')
print(f'(-) IR ({perc})        : R$ {ir:.2f}')
print(f'(-) INSS (10%)      : R$ {inss:.2f}')
print(f'(*) FGTS (11%)      : R$ {fgts:.2f}')
print(f'Total de descontos  : R$ {total_desc:.2f}')
print(f'Salário Liquido     : R$ {sal_liquido:.2f}')