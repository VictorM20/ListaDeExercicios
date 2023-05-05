"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            litros_abastecidos = self.quantidade_combustivel
        valor_total = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        print(
            f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}. Valor total: R$ {valor_total:.2f}")

    def abastecer_por_litro(self, litros):
        valor_total = litros * self.valor_litro
        if litros > self.quantidade_combustivel:
            litros = self.quantidade_combustivel
            valor_total = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        print(f"Abastecidos {litros:.2f} litros de {self.tipo_combustivel}. Valor total: R$ {valor_total:.2f}")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

    def __str__(self):
        return f"Bomba de {self.tipo_combustivel} - valor/litro: R$ {self.valor_litro:.2f}, quantidade: {self.quantidade_combustivel:.2f} litros"


# criando uma bomba de combustível com gasolina, valor de R$ 5,00 por litro e 100 litros disponíveis
bomba = BombaCombustivel("gasolina", 5.0, 100)

# mostrando as informações da bomba
print(bomba)

# abastecendo por valor R$ 50,00
bomba.abastecer_por_valor(50)

# mostrando as informações atualizadas da bomba
print(bomba)

# abastecendo por litro 20 litros
bomba.abastecer_por_litro(20)

# mostrando as informações atualizadas da bomba
print(bomba)

# alterando o valor do litro para R$ 4,50
bomba.alterar_valor(4.5)

# alterando o tipo de combustível para etanol
bomba.alterar_combustivel("etanol")

# alterando a quantidade de combustível para 150 litros
bomba.alterar_quantidade_combustivel(150)

# mostrando as informações atualizadas da bomba
print(bomba)
