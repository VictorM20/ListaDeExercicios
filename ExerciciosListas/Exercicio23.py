"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet,
ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que
gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser
 feita através de uma função separada, que será chamada pelo programa principal.
 O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""
with open("usuarios.txt", "r") as arquivo:  # Abrindo o arquivo
    usuarios = arquivo.readlines()  # Lendo o arquivo
    usuarios = [usuario.strip().split() for usuario in usuarios]  # Separando os dados
    usuarios = [[usuario[0], int(usuario[1])] for usuario in usuarios]  # Transformando o espaço em inteiro
    usuarios = sorted(usuarios, key=lambda usuario: usuario[1], reverse=True)  # Ordenando os dados
    total = sum([usuario[1] for usuario in usuarios])  # Somando o total de espaço
    media = total / len(usuarios)  # Calculando a média
    with open("relatorio.txt", "w") as relatorio:  # Abrindo o arquivo de relatório
        relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")  # Escrevendo o cabeçalho
        relatorio.write("-" * 80 + "\n")  # Escrevendo o cabeçalho
        relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")  # Escrevendo o cabeçalho
        for i, usuario in enumerate(usuarios):  # Percorrendo os usuários
            relatorio.write(
                f"{i + 1:<4} {usuario[0]:<15} {usuario[1] / 1024 / 1024:10.2f} MB {usuario[1] / total * 100:10.2f}%\n")  # Escrevendo os dados
        relatorio.write(f"\nEspaço total ocupado: {total / 1024 / 1024:10.2f} MB\n")  # Escrevendo o total
        relatorio.write(f"Espaço médio ocupado: {media / 1024 / 1024:10.2f} MB\n")  # Escrevendo a média
