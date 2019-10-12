locadora = {}
locacao = {}
while True:
    alteracao, position = "", ""
    print("""
          Cadastrar filme dig 1
            listar filmes dig 2
          atualizar filme dig 3
            excluir filme dig 4
          emprestar filme dig 5
           devolver filme dig 6
                     Sair dig 7
          """)
    option = int(input("Digite sua opção"))

    if option == 1:
        title = input("Digite o titulo:")
        coast = float(input("Digite o custo da locação:"))
        year = int(input("Digite o ano:"))
        quantity = int(input("Digite quantidade de copias:"))
        info = {"titulo": title, "valor": coast, "ano": year, "quantidade": quantity}
        locadora[title] = info

    if option == 2:
        print(locadora)  # imprimir com for

    if option == 3:
        title = input("Digite o nome do filme a atualizar na lista:")
        opt_title = int(input("digite para atualizar: 1 - Custo\n 2 - Ano\n 3 - Quantidade\n"))
        if opt_title == 1:
            position = "valor"
            alteracao = float(input("Novo valor:"))
        elif opt_title == 2:
            position = "ano"
            alteracao = int(input("Novo valor:"))
        elif opt_title == 3:
            position = "quantidade"
            alteracao = int(input("Novo valor:"))
        else:
            print ("Opção inválida")
        if alteracao != "" and position != "":
            locadora[title][position] = alteracao

    if option == 4:
        title = str(input("Digite o nome do filme a excluir da lista:"))
        del locadora[title]

    if option == 5:
        usuario = input("Digite o nome do cliente:")
        title = input("Digite o nome do filme a emprestar:")
        dia = int(input("Qual o dia da locação:"))
        if locadora[title]['quantidade'] > 0:
            locadora[title]['quantidade'] -= 1
            info = {"usuario": usuario, "filme": title, "data": dia}
            locacao[usuario] = info
        else:
            print("Não há esse filme ou não há cópias disponiveis")

    if option == 6:
        usuario = input("Digite o nome do cliente:")
        title = input("Digite o nome do filme a devolver:")
        devolucao = int(input("Digite a data de devolução:"))
        print(locacao)
        valor = (devolucao - locacao[usuario]["data"]) * locadora[title]['valor']
        print("O valor da locação foi de R$ {:.2f}".format(valor))
        if locadora[title]['titulo'] == title:
            locadora[title]['quantidade'] += 1
        else:
            print("Não há esse filme emprestado")


print ("Encerrado acesso a Lista")