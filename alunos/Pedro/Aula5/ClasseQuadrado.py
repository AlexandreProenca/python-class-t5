# dois atributos, lado e altura, possui o método área e o check se é um quadrado
class Quadrado:
    def __init__(self, lado, altura):
        if lado == altura:
            self.lado = lado
            self.altura = altura
        else:
            print("Não é um quadrado!\n")

    def area(self):
        return self.lado * self.altura


var_lado = int(input("Digite o lado do quadrado: "))
var_altura = int(input("Digite a altura do quadrado: "))

q = Quadrado(lado=var_lado, altura=var_altura)
print(q.area())