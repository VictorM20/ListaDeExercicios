"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input('Digite uma letra: ')

if letra.isalpha():
    if letra == 'a' or letra == 'A':
        print('Essa letra é vogal.')
    elif letra == 'e' or letra == 'E':
        print('Essa letra é vogal.')
    elif letra == 'i' or letra == 'I':
        print('Essa letra é vogal.')
    elif letra == 'o' or letra == 'O':
        print('Essa letra é vogal.')
    elif letra == 'u' or letra == 'U':
        print('Essa letra é vogal.')
    else:
        print('Essa letra é consoante.')
else:
    print('Não é uma letra.')