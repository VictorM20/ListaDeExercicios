"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
print('Posto Ipiranga')
combustivel = input('Digite o combutível que deseja: A- Álcool ou G-Gasolina: ')
qtd_combu = int(input('Digite quantos litros deseja abastecer: '))

alcool = 1.90
gasolina = 2.50

if combustivel == 'G' or combustivel == 'g':
    if qtd_combu < 20:
        parcial = qtd_combu * gasolina
        desconto = parcial * 0.04
        total = parcial - desconto
        print(f'Total a ser pago: R${total:.2f}')
    else:
        parcial = qtd_combu * gasolina
        desconto = parcial * 0.06
        total = parcial - desconto
        print(f'Total a ser pago: R${total:.2f}')
if combustivel == 'a' or combustivel == 'A':
    if qtd_combu < 20:
        parcial = qtd_combu * alcool
        desconto = parcial * 0.03
        total = parcial - desconto
        print(f'Total a ser pago: R${total:.2f}')
    else:
        parcial = qtd_combu * alcool
        desconto = parcial * 0.05
        total = parcial - desconto
        print(f'Total a ser pago: R${total:.2f}')
