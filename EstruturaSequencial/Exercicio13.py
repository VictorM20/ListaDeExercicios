"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

"""
h = float(input('Digite sua altura: '))
sexo = input('Digite [f]eminino ou [m]asculino: ')

if sexo == 'f':
    peso = (62.1 * h) - 44.7
    print(f'Seu peso ideal é: {peso:.2f}kg')
else:
    peso = (72.7 * h) - 58
    print(f'Seu peso ideal é: {peso:.2f}kg')