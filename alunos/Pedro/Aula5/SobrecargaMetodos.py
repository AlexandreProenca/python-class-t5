class Calc:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def soma(self, a, b):
        return a + b

    def soma(self, a, b, c):
        return a * b * c


c = Calc(n1=1, n2= 2, n3=3)
print(c.soma(1, 2))
print(c.soma(1, 2, 3))
