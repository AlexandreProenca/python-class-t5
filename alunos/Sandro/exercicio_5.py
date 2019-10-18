#Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta,
# nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.
class cc:
    def __init__(self,numero,nome,saldo):
        self.n = numero
        self.i = nome
        self.s = saldo
