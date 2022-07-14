"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
mb = int(input('Digite o tamanho do arquivo em (MB): '))
mbps = int(input('Digite a velocidade da internet em (Mbps): '))

download = (mb / mbps) * 60
print(f'Tempo aproximado de download em minutos: {download:.2f} min')