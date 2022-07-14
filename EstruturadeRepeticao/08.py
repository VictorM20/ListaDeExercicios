"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
numeros=int(input("Quantos numeros: "))

primeiro=int(input("Numero 1: "))

count=1
soma=primeiro

while count< numeros:
    count += 1
    temp=int(input("Numero %d: " % count))
    soma += temp

media = soma / numeros
print('Soma:' ,soma)
print('Média: %.2f' % (soma/numeros))