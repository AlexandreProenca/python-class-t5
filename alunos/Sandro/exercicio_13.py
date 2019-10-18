class retangulo:
    def __init__(self, lado1,lado2):
        self.l1 = lado1
        self.l2 = lado2
q1=retangulo(10,20)
q2=retangulo
print(q1.__dict__)
print(q1.l1,q1.l2)
q2.l1=int(input("Qual o tamanho da lateral?"))
q2.l2=int(input("Qual o tamanho da profundidade?"))
piso=float(input("qual o tamanho da peça de porcelanato?"))
print(f'O tamanho do rodape {2*q2.l1+2*q2.l2} e será usado {(q2.l1*q2.l2)/piso} porcelanatos.')