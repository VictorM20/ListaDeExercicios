"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
nome = input('Digite o Usuário: ')
senha = input('Digite sua senha: ')

while nome == senha:
    senha = input('Error, digite uma senha diferente do nome de usuário!\n'
                  'Digite sua senha: ')