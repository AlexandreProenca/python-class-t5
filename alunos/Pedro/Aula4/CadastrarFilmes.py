dict_filme = dict()
print("""
        1) Cadastrar novo filme
        2) Listar filmes
        3) Atualizar as informacoes de um filme
        4) Atualizar as informacoes de um filme
        5) Excluir um filme
        6) Emprestar um filme
        7) Devolver um filme
        8) Sair""")

while True:
    comando = int(input("\nDigite a ação desejada: "))
    if comando == 1:
        nome_filme = input("Digite o nome do filme: ")
        qtd_filme = int(float(input("Digite a quantidade de filmes: ")))
        valor_filme = float(input("Digite o valor da diária [R$]: "))
        ano_filme = int(float(input("Digite o ano do filme: ")))
        dict_filme[nome_filme] = dict(title=nome_filme,
                                      qtd=qtd_filme,
                                      valor=valor_filme,
                                      ano=ano_filme)
    elif comando == 2:
        for filme in dict_filme:
            print(filme)
    elif comando == 3:
        nome_filme = input("Digite o filme cujas informacoes serao exibidas: ")
        print(dict_filme[nome_filme])
    elif comando == 4:
        nome_filme = input("Digite o filme cujas informacoes serao atualizadas: ")
        print("""                1) Quantidade
                2) Valor da diaria [R$]
                3) Ano do filme""")
        atualizar = int(input("Digite a qual informaca voce deseja atualizar: "))
        info_atualizada = float(input("Digite para qual valor essa informacao sera atualizada: "))
        if atualizar == 1:
            dict_filme[nome_filme]["qtd"] = int(info_atualizada)
        elif atualizar == 2:
            dict_filme[nome_filme]["valor"] = info_atualizada
        elif atualizar == 3:
            dict_filme[nome_filme]["ano"] = int(info_atualizada)
        else:
            print("Opcao invalida")
    elif comando == 5:
        nome_filme = input("Digite o nome do filme a ser deletado: ")

        flag = 0
        for filme in dict_filme:
            if nome_filme == filme:
                flag = 1

        if flag:
            del dict_filme[nome_filme]
        else:
            print("Filme nao cadastrado.")
    elif comando == 6:
        nome_filme = input("Digite o nome do filme a ser emprestados: ")

        flag = 0
        for filme in dict_filme:
            if nome_filme == filme:
                flag = 1

        if flag:
            qtd_emprestimo = int(input("Digite a quantidade a ser emprestada: "))
            while qtd_emprestimo > dict_filme[nome_filme]["qtd"]:
                qtd_emprestimo = int(input("Quantidade insuficiente em estoque, digite outro valor: "))
            dict_filme[nome_filme]["qtd"] -= qtd_emprestimo
        else:
            print("Filme nao cadastrado, favor cadastrar o filme primeiro")
    elif comando == 7:
        nome_filme = input("Digite o nome do filme a ser devolvido: ")

        flag = 0
        for filme in dict_filme:
            if nome_filme == filme:
                flag = 1

        if flag:
            qtd_devolucao = int(input("Digite a quantidade de filmes a serem devolvidos: "))
            numero_dias = int(input("Digite a quantidade de dias que o filme ficou alugado: "))
            dict_filme[nome_filme]["qtd"] += qtd_devolucao
            valor_devolucao = dict_filme[nome_filme]["valor"] * numero_dias * qtd_devolucao
            print(f"Custo de devolucao: R${valor_devolucao}")
        else:
            print("Filme nao cadastrado, favor cadastrar o filme primeiro")
    elif comando == 8:
        break
    else:
        print("Opcao invalida")