"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
operador = input('Digite qual operador [+,-,*,/]:')

resultado = 0

if operador == '+':
    resultado = num1 + num2
    print(f'Resultado da operação: {resultado}')
elif operador == '-':
    resultado = num1 - num2
    print(f'Resultado da operação: {resultado}')
elif operador == '*':
    resultado = num1 * num2
    print(f'Resultado da operação: {resultado}')
elif operador == '/':
    resultado = num1 / num2
    print(f'Resultado da operação: {resultado}')

if resultado == round(resultado):
    print('Inteiro')
    if resultado % 2 == 0.0:
        print('Par')
        if resultado > 0.0:
            print('Positivo')
        else:
            print('Negativo')
    else:
        print('Impar')
else:
    print('Decimal')

