"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo,
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

cod_clientes = []
altura_clientes = []
peso_clientes = []
i = 1
codigo = True
while codigo != 0:
    print('Academia Fit')
    codigo = int(input('Digite seu código de acesso: '))
    if codigo == 0:
        break
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    cod_clientes.append(codigo)
    altura_clientes.append(altura)
    peso_clientes.append(peso)
    i += 1

cod_magro = peso_clientes.index(min(peso_clientes))
cod_gordo = peso_clientes.index(max(peso_clientes))
cod_alto = altura_clientes.index(min(altura_clientes))
cod_baixo = altura_clientes.index(max(altura_clientes))
print("Código do mais magro: ", cod_clientes[cod_magro])
print("Código do mais gordo: ", cod_clientes[cod_gordo])
print("Código do mais alto: ", cod_clientes[cod_alto])
print("Código do mais baixo: ", cod_clientes[cod_baixo])
print("Média de altura: ", sum(altura_clientes) / len(altura_clientes))
print("Média de peso: ", sum(peso_clientes) / len(peso_clientes))

