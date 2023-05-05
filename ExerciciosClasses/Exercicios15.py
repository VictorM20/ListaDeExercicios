"""
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e
por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
"""
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 50
        self.tedio = 50

    def __str__(self):
        return f"{self.nome}: Fome({self.fome}) Saúde({self.saude}) Tédio({self.tedio})"

    def alimentar(self, quantidade):
        self.fome += quantidade
        if self.fome > 100:
            self.fome = 100

    def brincar(self, minutos):
        self.tedio += int(minutos / 10)
        if self.tedio > 100:
            self.tedio = 100

    def verificar_saude(self):
        self.saude = 100 - self.fome - self.tedio
        if self.saude < 0:
            self.saude = 0

    def verificar_fome(self):
        self.fome -= 2

    def verificar_tedio(self):
        self.tedio -= 2

    def verificar_bichinho(self):
        self.verificar_fome()
        self.verificar_tedio()
        self.verificar_saude()

    def mostrar_status(self):
        print(self)


bicho = BichinhoVirtual("Bichinho")
bicho.mostrar_status()

# Alimentando o bichinho com 30 unidades de comida
bicho.alimentar(30)
bicho.mostrar_status()

# Brincando com o bichinho por 50 minutos
bicho.brincar(50)
bicho.mostrar_status()
