"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""
qtd = int(input('Digite a quantidade de eleitores: '))
i = 0
idades = 0
cand_x = 0
cand_y = 0
cand_z = 0
while i < qtd:
    voto = int(input('Digite seu Voto: "1 para candidato X", "2 para candidato Y", "3 para candidato Z": '))
    if voto == 1:
        cand_x += 1
    elif voto == 2:
        cand_y += 1
    else:
        cand_z += 1
    i += 1
print('Votação Encerrada!')
print(f'Candidato X teve {cand_x} votos computados.')
print(f'Candidato Z teve {cand_y} votos computados.')
print(f'Candidato X teve {cand_z} votos computados.')