class Bola:
    def __init__(self,cor,material):
        self.c = cor
        self.m = material
    def infor():
        return f"minha bola te a cor {self.c} e é feita de {self.m}"
b3 = Bola('azul','couro')
print(b3.c)
print(b3.m)
print(b3.__dict__)
print(infor(b3))