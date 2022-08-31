"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""

def reverso(n):
    return n[::-1]

n = input('Digite um número inteiro: ')
print(f'Inverso desse número: {reverso(n)}')