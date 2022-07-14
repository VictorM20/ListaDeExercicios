"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
nome = input('Digite seu nome: ')
while len(nome) <= 3:
    nome = input('Digite seu nome: ')
print('Computado!')
idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Digite sua idade: '))
print('Computado!')

salario = float(input('Digite seu salário: '))
while salario < 0:
    salario = float(input('Digite seu salário: '))
print('Computado!')

sexo = input('Digite seu sexo [F]eminino ou [M]asculino: ')
while sexo != 'f' and sexo != 'm':
    sexo = input('Informe a inicial do seu sexo: ')
print('Computado!')

civil = input('Digite seu estado civil [S]olteiro, [C]asado, [V]iuvo, [D]ivorciado: ')
while civil != 's' and civil != 'c' and civil != 'v' and civil != 'd':
    civil = input('Informe a inicial do seu estado civil: ')
print('Computado!')