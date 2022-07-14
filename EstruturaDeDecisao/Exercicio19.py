"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = int(input('Digite um número inteiro: '))

#Extraindo a unidade
unidade = num % 10
#Tirando a unidade do número
num = (num - unidade) / 10
#Extraindo a dezena
dezena = num % 10
#Tirando a dezena do número
num = (num - dezena)/10
centena = num

dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s)',dezena,'dezena(s) e',unidade,'unidade(s)')