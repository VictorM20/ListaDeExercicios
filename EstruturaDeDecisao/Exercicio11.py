"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input('Digite seu salário atual: R$ '))

if salario <= 280.00:
    aumento = salario * 0.2
    reajuste = salario * 1.20
    percentual = '20'
elif salario <= 700.00:
    aumento = salario * 0.15
    reajuste = salario * 1.15
    percentual = '15'
elif salario <= 1500:
    aumento = salario * 0.10
    reajuste = salario * 1.10
    percentual = '10'
else:
    aumento = salario * 0.05
    reajuste = salario * 1.05
    percentual = '5'

print(f'Salário atual: R${salario:.2f}')
print(f'Percentual de aumento aplicado: {percentual}%')
print(f'Valor do aumento: R${aumento:.2f}')
print(f'Valor do novo salário: R${reajuste:.2f}')

