"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
vetor = []
vogais = ['a','e','i','o','u']
cont = 0
y = 1
cont_vogal = 0
while y <= 10:
    caracter = input('Caractere: ')
    y += 1
    vetor.append(caracter)
    if caracter in vogais:
        cont += 1
    else:
        cont_vogal += 1
print('Consoantes: ',(len(vetor))-cont)
print('Vogais: ',(len(vetor))-cont_vogal)
