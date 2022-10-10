"""
Criar arquivos.py com nome Exercicios9 até Exercicios17

"""

def criarArquivos():
    for i in range(9, 18):
        nome = f"Exercicios{i}.py"
        arquivo = open(nome, 'w')
        arquivo.close()

criarArquivos()