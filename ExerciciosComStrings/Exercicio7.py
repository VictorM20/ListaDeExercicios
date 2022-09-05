"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.

"""
frase = input('Digite uma frase: ').lower()

print('Existe %d espaços em brancos nessa frase' % frase.count(" "))
print(f'Vogal "A" aparece: {frase.count("a")} vezes\n'
      f'Vogal "E" aparece: {frase.count("e")} vezes\n'
      f'Vogal "I" aparece: {frase.count("i")} vezes\n'
      f'Vogal "O" aparece: {frase.count("o")} vezes\n'
      f'Vogal "U" aparece: {frase.count("u")} vezes')