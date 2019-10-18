#Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta,
# nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:
    def __init__(self, numero, nome, saldo):
        self.n = int(numero)
        self.i = nome
        self.s = float(saldo)

    def info(self):
        print(f"As informacomacoes da conta sao: {self.i} : {self.n} e {self.s}")



option = 0
banco = {}
numero_automatico = 1000
while(option != 6):
    deposito = float(0)
    print("""
            Tecle 1 - Cadastrar cliente
            Tecle 2 - inserir deposito
            Tecle 3 - registrar saque
            Tecle 4 Consultar saldo
            tecle 5 para alterar cliente
            tecle 6 para sair""")
    option = int(input("Digite sua opção"))
    if option == 1:
        nome = input("Digite o nome do cliente.")
        banco[numero_automatico] = ContaCorrente(numero=numero_automatico, nome=nome, saldo=0)
        print(f"Sua conta é o número {banco[numero_automatico].n}")
        numero_automatico += 1
    elif option == 2:
        conta = int(input("Digite a conta do cliente."))
        deposito = float(input(f"Digite o valor do deposito de {conta.i}."))
        conta.s = cc(s + deposito)
    elif option == 3:
            conta.n = input("Digite a conta do cliente.")
            deposito = float(input(f"Digite o valor do saque de {conta.i}."))
            cconta.s = cconta.s - deposito
    elif option == 4:
            cconta.i = input("Digite a conta do cliente.")
            print(f"o cliente {cconta.i} possue R$ {cconta.s} de saldo bancario.")
    banco[numero_automatico-1].info()