class Retangulo:
    def __init__(self, lado, altura):
        self.l = lado
        self.h = altura
    def conta(self):
        return self.l * self.h
    def quadrado(self):
        if self.l == self.h:
            return 'quadrado'
        else:
            return 'não é quadrado'

r = Retangulo(3,2)

n = r.conta()
m = r.quadrado()

print(n,m)