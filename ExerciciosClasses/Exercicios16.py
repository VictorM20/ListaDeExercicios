"""
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto.
Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário.
Dica: acrescente um método especial str() à classe Bichinho.
"""
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
        self.fome = 0
        self.saude = 100
        self.brincando = False

    def __str__(self):
        return f'BichinhoVirtual(nome={self.nome}, idade={self.idade}, fome={self.fome}, saude={self.saude}, brincando={self.brincando})'

    def mostrar_menu(self):
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Dormir")
        print("4 - Exibir atributos do bichinho (secreto)")
        print("0 - Sair")

    def escolher_opcao(self):
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def alimentar(self, quantidade):
        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 0
        self.saude += 10
        if self.saude > 100:
            self.saude = 100
        self.idade += 1

    def brincar(self, tempo):
        self.fome += tempo
        if self.fome > 100:
            self.fome = 100
        self.saude -= tempo
        if self.saude < 0:
            self.saude = 0
        self.idade += 1
        self.brincando = True

    def dormir(self):
        self.fome += 10
        if self.fome > 100:
            self.fome = 100
        self.saude += 10
        if self.saude > 100:
            self.saude = 100
        self.idade += 1
        self.brincando = False

    def mostrar_atributos(self):
        print(self)

# programa principal
bichinho = BichinhoVirtual("Pikachu")
while True:
    bichinho.mostrar_menu()
    opcao = bichinho.escolher_opcao()
    if opcao == 1:
        quantidade = int(input("Digite a quantidade de comida: "))
        bichinho.alimentar(quantidade)
    elif opcao == 2:
        tempo = int(input("Digite a quantidade de minutos que deseja brincar: "))
        bichinho.brincar(tempo)
    elif opcao == 3:
        bichinho.dormir()
    elif opcao == 4:
        senha = input("Digite a senha secreta: ")
        if senha == "1234":
            bichinho.mostrar_atributos()
        else:
            print("Senha incorreta!")
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")
