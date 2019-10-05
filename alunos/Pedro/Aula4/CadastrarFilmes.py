dict_movie = dict()
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
    command = int(input("\nDigite a ação desejada: "))
    if command == 1:
        name_movie = input("Digite o nome do filme: ")
        qtd_movie = int(float(input("Digite a quantidade de filmes: ")))
        value_movie = float(input("Digite o valor da diária [R$]: "))
        year_movie = int(float(input("Digite o ano do filme: ")))
        dict_movie[name_movie] = dict(title=name_movie,
                                      qtd=qtd_movie,
                                      valor=value_movie,
                                      ano=year_movie)
    elif command == 2:
        for movie in dict_movie:
            print(movie)
    elif command == 3:
        name_movie = input("Digite o filme cujas informacoes serao exibidas: ")
        print(dict_movie[name_movie])
    elif command == 4:
        name_movie = input("Digite o filme cujas informacoes serao atualizadas: ")
        print("""                1) Quantidade
                2) Valor da diaria [R$]
                3) Ano do filme""")
        command_att = int(input("Digite a qual informaca voce deseja atualizar: "))
        info_att = float(input("Digite para qual valor essa informacao sera atualizada: "))
        if command_att == 1:
            dict_movie[name_movie]["qtd"] = int(info_att)
        elif command_att == 2:
            dict_movie[name_movie]["valor"] = info_att
        elif command_att == 3:
            dict_movie[name_movie]["ano"] = int(info_att)
        else:
            print("Opcao invalida")
    elif command == 5:
        name_movie = input("Digite o nome do filme a ser deletado: ")

        flag = 0
        for movie in dict_movie:
            if name_movie == movie:
                flag = 1

        if flag:
            del dict_movie[name_movie]
        else:
            print("Filme nao cadastrado.")
    elif command == 6:
        name_movie = input("Digite o nome do filme a ser emprestados: ")

        flag = 0
        for movie in dict_movie:
            if name_movie == movie:
                flag = 1

        if flag:
            qtd_borrow = int(input("Digite a quantidade a ser emprestada: "))
            while qtd_borrow > dict_movie[name_movie]["qtd"]:
                qtd_borrow = int(input("Quantidade insuficiente em estoque, digite outro valor: "))
            dict_movie[name_movie]["qtd"] -= qtd_borrow
        else:
            print("Filme nao cadastrado, favor cadastrar o filme primeiro")
    elif command == 7:
        name_movie = input("Digite o nome do filme a ser devolvido: ")

        flag = 0
        for movie in dict_movie:
            if name_movie == movie:
                flag = 1

        if flag:
            qtd_return = int(input("Digite a quantidade de filmes a serem devolvidos: "))
            num_days = int(input("Digite a quantidade de dias que o filme ficou alugado: "))
            dict_movie[name_movie]["qtd"] += qtd_return
            value_return = dict_movie[name_movie]["valor"] * num_days * qtd_return
            print(f"Custo de devolucao: R${value_return}")
        else:
            print("Filme nao cadastrado, favor cadastrar o filme primeiro")
    elif command == 8:
        break
    else:
        print("Opcao invalida")