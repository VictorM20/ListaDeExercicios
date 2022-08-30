"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""
def imprimir(n):
    if isinstance(n, int):
        x = 1
        while x <= n:
            y = 1
            texto = ''
            while y <= x:
                texto += str(y) + "\t"
                y += 1
            print(texto)
            x += 1
n = int(input('Digite um número: '))
imprimir(n)