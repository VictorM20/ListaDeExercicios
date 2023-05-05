"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(),
verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        print(f"{self.nome} tem no bucho: {self.bucho}")

    def digerir(self):
        self.bucho = []

    def __str__(self):
        return self.nome

macaco1 = Macaco("Maurício")
macaco2 = Macaco("Gustavo")

macaco1.comer("banana")
macaco1.comer("maçã")
macaco1.comer("laranja")

macaco2.comer("cenoura")
macaco2.comer("beterraba")
macaco2.comer("couve")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()
