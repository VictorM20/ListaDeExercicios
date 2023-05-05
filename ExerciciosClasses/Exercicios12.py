"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""
class contaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicioneJuros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros

# criando uma conta de investimento com saldo inicial de R$1000,00 e taxa de juros de 10%
poupanca = contaInvestimento(1000, 10)

# adicionando juros 5 vezes
for i in range(5):
    poupanca.adicioneJuros()

# imprimindo o saldo resultante
print("Saldo da poupança após 5 meses de juros: R$%.2f" % poupanca.saldo)
