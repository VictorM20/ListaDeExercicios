"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
maca = int(input('Digite a quantidade de maça: '))
morango = int(input('Digite a quantidade de morangos: '))

total_kg = maca + morango

if maca <= 5:
    valor_maca = 1.80
    valor_ttmaca = valor_maca * maca
else:
    valor_maca = 1.50
    valor_ttmaca = valor_maca * maca

if morango <= 5:
    valor_morango = 2.50
    valor_ttmorango = valor_morango * morango
else:
    valor_morango = 2.20
    valor_ttmorango = valor_morango * morango

preco_total = valor_ttmorango + valor_ttmaca

if total_kg >= 8 or preco_total >= 25:
    desconto = preco_total * 0.1
    preco_final = preco_total - desconto
    print(f'Total do pedido foi de {total_kg}Kg com valor de R${preco_final:.2f}')