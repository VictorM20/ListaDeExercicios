"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

"""
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer()

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self):
        self.altura += 0.5

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}'


pessoa = Pessoa('Fulano', 20, 80, 1.80)
print(pessoa)
pessoa.envelhecer()
print(pessoa)
pessoa.engordar(10)
print(pessoa)
pessoa.emagrecer(5)
print(pessoa)
pessoa.crescer()
print(pessoa)
