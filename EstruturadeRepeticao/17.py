"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)