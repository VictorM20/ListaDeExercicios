"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""
alunos = []
media_maior = 0
medias = []
notas = []
for i in range(10):
    alunos.append(input('Digite o nome do Aluno(a): '))
    for a in range(4):
        notas.append(float(input('Nota: ' )))
    media = sum(notas) / len(notas)
    medias.append(media)
    if media >= 7.0:
        media_maior += 1
print(f'Número de alunos com média acima de 7.0: {media_maior}')
