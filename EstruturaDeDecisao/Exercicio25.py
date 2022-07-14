"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
lista = []

resposta = input("Telefonou para a vítima?[S/N]: ")
if resposta.lower() == 's':
    lista.append(resposta)
resposta = input("Esteve no local do crime?[S/N]: ")
if resposta.lower() == 's':
    lista.append(resposta)
resposta = input("Mora perto da vítima?[S/N]: ")
if resposta.lower() == 's':
    lista.append(resposta)
resposta = input("Devia para a vítima?[S/N]: ")
if resposta.lower() == 's':
    lista.append(resposta)
resposta = input("Já trabalhou com a vítima?[S/N]: ")
if resposta.lower() == 's':
    lista.append(resposta)

tam = len(lista)

if tam == 5:
    print(f"Por responder que 'Sim' a {tam} perguntas, vocé é considerado Assassino!")
elif tam >= 3:
    print(f"Por responder que 'Sim' a {tam} perguntas, vocé é considerado Cúmplice")
elif tam == 2:
    print(f"Por responder que 'Sim' a {tam} perguntas, vocé é considerado Suspeita")
else:
    print(f"Por responder que 'Sim' a {tam} perguntas, vocé é considerado Inocente")





