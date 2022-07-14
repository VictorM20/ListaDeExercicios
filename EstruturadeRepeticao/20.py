"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
limitando o fatorial a números inteiros positivos e menores que 16.
"""
while True:
    resultado = 1
    count = 1
    print('Digite um número para calcular o Fatorial ou "P" para sair do programa.')
    valor = input("Fatorial de: ")
    if valor.upper() == 'P':
        print('Finalizando programa')
        break

    numero = int(valor)
    if numero <= 0 or numero >= 16:
        print('Digite um número entre 1 e 15!')
        continue
    while count <= numero:
        resultado *= count
        count += 1

    print(resultado)