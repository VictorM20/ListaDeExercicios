"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
print('Estatísticas de cincos cidades Brasileiras')
codigo = []
num_veiculos = []
num_acidentes = []
acidentes_2000 = []
total_veiculos = 0
for i in range(5):
    cidade = int(input('Digite o codigo da cidade: '))
    veiculos = int(input('Digite o números de veiculos de passeio: '))
    acidentes = int(input('Digite o número de acidentes de trânsito com vítimas: '))
    codigo.append(cidade)
    num_veiculos.append(veiculos)
    num_acidentes.append(acidentes)
    total_veiculos += veiculos
    if veiculos > 2000:
        acidentes_2000.append(acidentes)
        num_acidentes.append(acidentes)
    else:
        num_acidentes.append(acidentes)

maior_indice = num_acidentes.index(max(num_acidentes))
menor_indice = num_acidentes.index(min(num_acidentes))
media_veiculos = total_veiculos / 5

print('Maior índice de acidentes de trânsito é a cidade ', codigo[maior_indice], ' com ', max(num_acidentes))
print('Menor índice de acidentes de trânsito é a cidade ', codigo[menor_indice], 'com ', min(num_acidentes))
print(f'A média de veículos das cinco cidades juntas é de {media_veiculos}')
media_acidentes_2000 = sum(acidentes_2000) / len(acidentes_2000)
print(f'Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_2000}')