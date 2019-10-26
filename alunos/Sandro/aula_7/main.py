import json
from modulo import ContaCorrente


numero_automatico = 1000
option = 0
banco = {}

while(option != 6):
    deposito = float(0)
    print("""
            Tecle 1 - Cadastrar cliente
            Tecle 2 - inserir deposito
            Tecle 3 - registrar saque
            Tecle 4 - Consultar saldo
            tecle 5 - para alterar cliente
            tecle 6 - para sair""")
    try:
        option = int(input("Digite sua opção"))
    except ValueError:
        print("Esta opção não é valida.")
    if option == 1:
        nome = input("Digite o nome do cliente.")
        banco[numero_automatico] = ContaCorrente(numero=numero_automatico, nome=nome, saldo=0)
        print(f"Sua conta é o número {banco[numero_automatico].numero}")
        conta = numero_automatico
        numero_automatico += 1
    elif option == 2:
        while True:
            try:
                conta = int(input("Digite a conta do cliente."))
                banco[conta]
            except ValueError:
                print('Esta conta não é valida')
            except KeyError:
                print('Esta conta não esta cadastrada')
            else:
                break


        deposito = float(input(f"Digite o valor do deposito de {banco[conta].nome}."))
        banco[conta].saldo += deposito
    elif option == 3:
        conta = int(input("Digite a conta do cliente."))
        deposito = float(input(f"Digite o valor de saque de {banco[conta].nome}."))
        banco[conta].s -= deposito
    elif option == 4:
            conta = int(input("Digite a conta do cliente."))

            banco[conta].info()
    elif option == 5:
            conta = int(input("Digite a conta do cliente."))
            nome_alt = (input("Digite o nome correto do cliente."))

            for cc in banco:
                if banco[cc].nome == nome_alt:
                    print(f"Esse cliente ja possui cadastro na conta {cc}")
                    break
            else:
                banco[conta].nome = nome_alt

    elif option > 7:
        print('opção inválida, tente de novo')
        print (banco)

for i in banco.keys():
    with open("C:/Users/RS5891/PycharmProjects/python-t5/alunos/Sandro/aula_6/banco.txt", 'a') as reader:
        reader.write(json.dumps(banco[i].__dict__))

with open("C:/Users/RS5891/PycharmProjects/python-t5/alunos/Sandro/aula_6/banco.txt", 'r') as reader:

    base_dados = reader.readlines()
    for b in base_dados:
        d = json.loads(b)
        c = ContaCorrente(**d)
        banco[c.numero] = c
        numero_automatico = c.numero+1
