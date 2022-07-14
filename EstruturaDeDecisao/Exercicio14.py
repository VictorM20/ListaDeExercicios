"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
"""

aluno = input('Digite o nome do aluno(a): ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2) / 2

if media < 4.0:
    print(f'Aluno(a): {aluno}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Nota conceito: E')
    print(f'Média em nota: {media}')
    print('Está Reprovado!')
if media >= 4.0 and media < 6.0:
    print(f'Aluno(a): {aluno}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Nota conceito: D')
    print(f'Média em nota: {media}')
    print('Está Reprovado!')
if media >= 6.0 and media < 7.5:
    print(f'Aluno(a): {aluno}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Nota conceito: C')
    print(f'Média em nota: {media}')
    print('Está Aprovado!')
if media >= 7.5 and media < 9.0:
    print(f'Aluno(a): {aluno}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Nota conceito: B')
    print(f'Média em nota: {media}')
    print('Está Aprovado!')
if media >= 9.0 and media < 10.0:
    print(f'Aluno(a): {aluno}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Nota conceito: A')
    print(f'Média em nota: {media}')
    print('Está Aprovado!')



