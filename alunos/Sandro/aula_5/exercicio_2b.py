class quadrado:
    def __init__(self,lado):
        self.l = lado
q1=quadrado(10)
print(q1.__dict__)
q1.l=20
print(q1.l)
print(f'O lado do quadrado é {q1.l} e a area é {q1.l*q1.l}')