"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""
class Televisao:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    def aumentar_volume(self):
        self.volume += 1
    def diminuir_volume(self):
        self.volume -= 1
    def aumentar_canal(self):
        self.canal += 1
    def diminuir_canal(self):
        self.canal -= 1
    def __str__(self):
        return f"Canal: {self.canal} Volume: {self.volume}"

tv = Televisao(1, 1)
print(tv)
tv.aumentar_volume()
print(tv)
tv.diminuir_volume()
print(tv)
tv.aumentar_canal()
print(tv)
tv.diminuir_canal()
print(tv)
