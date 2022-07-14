"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

produto = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) + n3
cubo = n3 ** 3

print(f'Produto do dobro do primeiro com metado do segundo: {produto}')
print(f'Soma do triplo do primeiro com o terceiro: {soma}')
print(f'Terceiro elevado ao cubo: {cubo:.2f}')