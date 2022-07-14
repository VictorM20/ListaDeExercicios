"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
salario_hora = float(input('Digite seu rendimento por hora: '))
tempo_trabalhado = int(input('Digite o número de horas trabalhadas no mês: '))
salario =  salario_hora * tempo_trabalhado

print(f'Seu é salário é de: {salario}')