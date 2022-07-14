"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

valido = False

#Meses com 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    valido = True
#Meses com 30 dias
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    valido = True
#Fevereiro
elif mes == 2:
    #Testando bissexto
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if(dia <=29):
            valido = True
    elif(dia <=28):
        valido = True
if(valido):
    print('Data válida')
else:
    print('Data inválida')