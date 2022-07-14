"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
metros = int(input('Digite a área quadrado a ser pintado: '))
litros = metros / 3
#1 litro = 3 metros quadrados
#lata de 18 litros = R$ 80.00

if metros % 54 == 0:
	latas = metros / 54
else:
	latas = int(metros / 54) + 1

preco = latas * 80
print (f'{latas} latas')
print (f'R$ {preco:.2f}')