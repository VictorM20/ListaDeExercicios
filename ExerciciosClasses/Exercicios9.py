"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Retangulo:
    def __init__(self, largura, altura, ponto):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto

    def centro(self):
        x = self.ponto.x + self.largura / 2
        y = self.ponto.y + self.altura / 2
        return Ponto(x, y)

    def alterar_largura(self, nova_largura):
        self.largura = nova_largura

    def alterar_altura(self, nova_altura):
        self.altura = nova_altura

    def __str__(self):
        return f"Retângulo de largura {self.largura} e altura {self.altura} com ponto de partida em {self.ponto}"


def imprimir_ponto(ponto):
    print(f"Ponto: {ponto}")


# criando um retângulo com largura 5, altura 3 e ponto de partida em (2, 2)
retangulo = Retangulo(5, 3, Ponto(2, 2))

# mostrando as informações do retângulo
print(retangulo)

# mostrando o centro do retângulo
centro = retangulo.centro()
imprimir_ponto(centro)

# alterando a largura do retângulo para 7
retangulo.alterar_largura(7)

# mostrando as informações atualizadas do retângulo
print(retangulo)

# mostrando o novo centro do retângulo
centro = retangulo.centro()
imprimir_ponto(centro)
