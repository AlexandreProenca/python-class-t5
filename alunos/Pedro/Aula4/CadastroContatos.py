dict_contato = dict()
print("""
        1) Cadastrar contato
        2) Listar contatos
        3) Mostrar um contato específico
        4) Excluir um contato
        5) Sair""")

while(True):
    comando = int(input("\nDigite a ação desejada: "))
    if comando == 1:
        nome_contato = input("Digite o nome do contato a ser inserido: ")
        info_contato = input("Digite as informacoes do contato inserido: ")
        dict_contato[nome_contato] = info_contato
    elif comando == 2:
        for contato in dict_contato:
            print(contato)
    elif comando == 3:
        nome_contato = input("Digite o contato cujas informacoes serao exibidas: ")
        print(dict_contato[nome_contato])
    elif comando == 4:
        nome_contato = input("Digite o nome do contato a ser deletado: ")
        del dict_contato[nome_contato]
    elif comando == 5:
        break