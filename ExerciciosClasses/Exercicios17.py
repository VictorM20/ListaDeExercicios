"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista.
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho,
exija que ele tome conta da fazenda inteira.
Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos,
brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante,
dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""
import random


class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)

    def __str__(self):
        return f"{self.nome}: fome={self.fome}, tédio={self.tedio}"

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def fome(self):
        self.fome -= 1
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo):
        self.tedio -= tempo
        if self.tedio < 0:
            self.tedio = 0

    def alimentar(self, comida):
        self.fome += comida


class FazendaBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionarBichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentarBichinhos(self):
        comida = int(input("Quantidade de comida: "))
        for bichinho in self.bichinhos:
            bichinho.alimentar(comida)

    def brincarBichinhos(self):
        tempo = int(input("Tempo de brincadeira: "))
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)

    def ouvirBichinhos(self):
        for bichinho in self.bichinhos:
            print(bichinho)

    def executarOpcao(self, opcao):
        if opcao == 1:
            self.alimentarBichinhos()
        elif opcao == 2:
            self.brincarBichinhos()
        elif opcao == 3:
            self.ouvirBichinhos()
        elif opcao == 4:
            print("Fim do programa.")
            return False
        else:
            print("Opção inválida. Tente novamente.")
        return True


fazenda = FazendaBichinhos()

# Adicionando bichinhos
fazenda.adicionarBichinho(Bichinho("Bichinho 1"))
fazenda.adicionarBichinho(Bichinho("Bichinho 2"))
fazenda.adicionarBichinho(Bichinho("Bichinho 3"))

# Executando o programa
continuar = True
while continuar:
    print("\n=== Fazenda de Bichinhos ===")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))
    continuar = fazenda.executarOpcao(opcao)
