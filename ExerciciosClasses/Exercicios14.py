"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
"""
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def aumentarSalario(self, porcentualDeAumento):
        aumento = self.salario * (porcentualDeAumento / 100)
        self.salario += aumento

harry = Funcionario("Harry", 25000)
print(harry.get_nome(), harry.get_salario()) # Harry 25000
harry.aumentarSalario(10)
print(harry.get_nome(), harry.get_salario()) # Harry 27500.0
