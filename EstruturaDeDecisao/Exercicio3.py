"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = input('Digite [F]eminino ou [M]asculino: ')

if sexo == 'F' or sexo == 'f':
    print('Sexo Feminino definido.')
elif sexo == 'M' or sexo == 'm':
    print('Sexo Masculino definido.')
else:
    print('Sexo inválido.')