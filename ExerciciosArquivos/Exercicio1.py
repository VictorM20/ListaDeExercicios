"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""


def validadorIP(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    for i in ip:
        if int(i) < 0 or int(i) > 255:
            return False
    return True


file = open('lista-ip.txt', 'r')

linhas = file.readlines()

file.close()

validar = []
invalidos = []

for j in linhas:
    validadorIP(j)
    if validadorIP(j):
        validar.append(j)
    else:
        invalidos.append(j)

file = open('relatorio.txt', 'w')
file.write('[Endereços válidos:]\n')
for y in validar:
    file.write(y)
file.write('\n[Endereços inválidos:]\n')
for z in invalidos:
    file.write(z)

file.close()
