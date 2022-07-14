"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero: '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro
menor = primeiro
#Comparando maior
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
#Comparando menor
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('Maior: ',maior)
print('Menor: ',menor)