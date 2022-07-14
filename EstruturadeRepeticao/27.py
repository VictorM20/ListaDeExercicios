"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""
import math
turmas = int(input('Digite a quantidade de turmas: '))
i = 1
total_alunos = 0
while i <= turmas:
    qtd_alunos = int(input(f'Digite a quantidade de alunos da {i}º turma:'))
    if qtd_alunos > 40:
        print('A turma não pode ter mais de 40 alunos.')
        continue
    total_alunos += qtd_alunos
    i += 1
media = total_alunos / turmas
print(f'Número média de alunos por turma é {math.ceil(media)}')