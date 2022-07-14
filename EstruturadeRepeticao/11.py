"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
num1 = int(input('Digite primeiro número: '))
num2 = int(input('Digite segundo número: '))
soma = 0
while (num1<num2-1):
    num1=num1+1
    print(num1)
    soma = num1+soma

print('Soma dos intervalos: ', soma)
