"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

populacaoA = int(input('Digite a população da Cidade A: '))
populacaoB = int(input('Digite a população da Cidade B: '))
taxaA = float(input('Digite a taxa de crescimento da Cidade A: '))
taxaB = float(input('Digite a taxa de crescimento da Cidade B: '))

ano = 0
while populacaoA <= populacaoB:
    populacaoA += round((populacaoA * taxaA)/100)
    populacaoB += round((populacaoB * taxaB)/100)
    ano = ano + 1

print("Levará", ano, "anos para população da cidade A ser maior que a cidade B")
print("População B:", populacaoB, "habitantes")
print("População A:", populacaoA, "habitantes")