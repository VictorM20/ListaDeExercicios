"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e
o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""
cod_aluno = []
altura_aluno = []
for i in range(1,10):
    aluno = int(input(f'Digite o número do {i}º aluno: '))
    altura = float(input(f'Digite a altura do {i}º aluno: '))
    cod_aluno.append(aluno)
    altura_aluno.append(altura)

cod_alto = altura_aluno.index(max(altura_aluno))
cod_baixo = altura_aluno.index(min(altura_aluno))
print("Aluno mais alto: ", cod_aluno[cod_alto], "e sua altura: ", max(altura_aluno))
print("Aluno mais baixo: ", cod_aluno[cod_baixo], "e sua altura: ", min(altura_aluno))