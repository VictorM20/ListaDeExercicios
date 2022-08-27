"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados.
"""
import random

num = [0] * 6
for i in range(1, 100):
    n = random.randint(1, 6)
    num[n - 1] = num[n - 1] + 1

cont = 1
for n in num:
    print(f'{cont} teve {n} lançamentos')
    cont += 1
