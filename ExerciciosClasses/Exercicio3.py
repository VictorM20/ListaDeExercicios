"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""
class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValorLados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def retornarValorLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)


ladoA = float(input("Digite o valor do lado A: "))
ladoB = float(input("Digite o valor do lado B: "))
retangulo = Retangulo(ladoA, ladoB)
print("Area do retangulo: ", retangulo.calcularArea())
print("Perimetro do retangulo: ", retangulo.calcularPerimetro())