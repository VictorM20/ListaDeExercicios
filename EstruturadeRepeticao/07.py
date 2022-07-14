"""
Faça um programa que leia 5 números e informe o maior número.
"""
numeros=int(input("Quantos numeros: "))

primeiro=int(input("Numero 1: "))

count=1
maior=primeiro

while count< numeros:
    count += 1
    temp=int(input("Numero %d: " % count))
    if temp>maior:
        maior = temp
print(maior)