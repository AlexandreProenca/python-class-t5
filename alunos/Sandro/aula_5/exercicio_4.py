class pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.n = nome
        self.i = idade
        self.p = peso
        self.h = altura
p1=pessoa
p1.n=input("Qual o nome da pessoa?")
p1.i=int(input("Qual a idade da pessoa?"))
p1.p=float(input("Qual o peso da pessoa?"))
p1.h=float(input("Qual a altura da pessoa(metros)?"))
anos=int(input("quantos anos se passaram?"))
if p1.i+anos <21:
    p1.i=p1.i+anos
    p1.h=p1.h+(anos*0.005)
else:
    p1.i = p1.i + anos

print(f'O {p1.n} tem {p1.i} anos de idade, pesa {p1.p} e tem {p1.h} m de altura.')