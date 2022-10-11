"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""
class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_fome(self, fome):
        self.fome = fome

    def alterar_saude(self, saude):
        self.saude = saude

    def alterar_idade(self, idade):
        self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        return self.fome + self.saude

    def __str__(self):
        return f'Nome: {self.nome} Fome: {self.fome} Saúde: {self.saude} Idade: {self.idade} Humor: {self.retornar_humor()}'


bichinho = BichinhoVirtual('Bichinho', 10, 10, 10)
print(bichinho)
bichinho.alterar_fome(20)
bichinho.alterar_saude(20)
print(bichinho)
