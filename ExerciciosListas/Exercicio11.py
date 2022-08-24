"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
print('Primeiro vetor')
for i in range(1, 11):
    vetor1.append(int(input('Digite o %dº número: ' % i)))
print('Segundo vetor')
for i in range(1, 11):
    vetor2.append(int(input('Digite o %dº número: ' % i)))
print('Terceiro vetor')
for i in range(1, 11):
    vetor3.append(int(input('Digite o %dº número: ' % i)))
print(vetor3)
for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
print(vetor4)