"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def __str__(self):
        return f"Conta: {self.numero} - Nome: {self.nome} - Saldo: {self.saldo}"

alterarNome = ContaCorrente(123, "João")
print(alterarNome)
alterarNome.alterarNome("Maria")
print(alterarNome)
deposito = ContaCorrente(123, "João")
print(deposito)
deposito.deposito(100)
print(deposito)
saque = ContaCorrente(123, "João")
print(saque)
saque.saque(500)
print(saque)

