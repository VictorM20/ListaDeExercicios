"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
respostas = []
perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]

for i in perguntas:
    resposta = input('%s ' % i).upper()
    print(resposta)

    if resposta == 'S':
        respostas.append(resposta)

if len(respostas) == 2:
    print('Suspeita')
elif len(respostas) == 3 and len(respostas) == 4:
    print('Cúmplice')
elif len(respostas) == 5:
    print('Assassino')
else:
    print('Inocente')