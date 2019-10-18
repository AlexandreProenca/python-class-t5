class Bola:
    def __init__(self,cor,circunferencia,material):
        self.c = cor
        self.d = circunferencia
        self.m = material
b3 = Bola('azul',20,'couro')
print(b3.c)
print(b3.d)
print(b3.m)
print(b3.__dict__)
b3.c="vermelha"
print(b3.c)
print(b3.__dict__)
