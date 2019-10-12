# funcao se chama método e variável se chama atributo
class Bola:
    def __init__(self, cor, material):
        self.cor = cor
        self.material = material

    def somar(self, n1, n2):
        return n1 + n2

    def info(self):
        return f"Minha bola tem a cor {self.cor} e é feita de {self.material}"


bola_da_pelada = Bola(cor="branca", material="plastico")
print(bola_da_pelada.__dict__)

print(bola_da_pelada.somar(1, 2))
print(bola_da_pelada.info())


class Bolinha(Bola):    #herança
    def __init__(self, cor, material, raio):
        super().__init__(cor, material)
        self.raio = raio


bola = Bolinha(cor="amarelinho", material="ferro", raio=5)
print(bola.info())