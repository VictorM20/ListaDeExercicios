"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
"""

unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
f_dezena = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo']
dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

numero = int(input('Digite um número de 0 a 99: '))
if (numero < 0) or (numero > 99):
    print('O numero informado deve estar entre 0 e 99')
else:
    dezena = numero / 10
    unidade = numero % 10

    if (numero >= 20):
        print('%s' % dezenas[int(dezena)], end="")
        if (unidade != 0):
            print(' e %s' % unidades[int(unidade)])
        print('')
    elif (numero >= 10):
        print('%s' % f_dezena[int(unidade)])
    else:
        print('%s' % unidades[int(unidade)])
