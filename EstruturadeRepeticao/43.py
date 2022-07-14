"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""
total = 0
while True:
    codigo = int(input('Digite o código do pedido: '))
    qtd = int(input('Digite a quantidade: '))
    
    if codigo == 100:
        valor = 1.20 * qtd
    elif codigo == 101:
        valor = 1.30 * qtd
    elif codigo == 102:
        valor = 1.50 * qtd
    elif codigo == 103:
        valor = 1.20 * qtd
    elif codigo == 104:
        valor = 1.30 * qtd
    elif codigo == 105:
        valor = 1.00 * qtd
    total += valor
    sair = input('Deseja Finalizar o pedido? S/N ')
    if sair.upper() == 'S':
        break
print(f'Valor total do pedido: {total:.2f}')