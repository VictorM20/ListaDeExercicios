"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
num = []
while True:
    numeros = float(input('Digite algum número: '))

    if numeros < 0:
        print('**Programa Encerrado**')
        break
    num.append(numeros)
media = sum(num) / len(num)
acima_media = 0
abaixo_media = 0
for n in num:
    if n > media:
        acima_media += 1
    if n < 7:
        abaixo_media += 1
print(f'Todos números: {num}')
print('Valores na ordem inversa: ')
num.reverse()
print(num)
print(f'Soma dos valores: {sum(num)}')
print(f'Média dos valores: {sum(num) / len(num)}')
print(f'Quantidade de valores acima da média calculada: {acima_media}')
print(f'Mostre a quantidade de valores abaixo de sete: {abaixo_media}')
print('**Programa Encerrado**')
