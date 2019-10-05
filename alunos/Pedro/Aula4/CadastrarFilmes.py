def CheckElement(dict_names, verify):
    flag = 0
    for x in dict_names:
        if x == verify:
            flag = 1
        if flag:
            return 1
        else:
            print(f"Elemento {verify} nao esta cadastrado, favor cadastrar primeiro")

dict_movie = dict()
dict_user = dict()

print("""
        1) Cadastrar novo filme
        2) Listar filmes
        3) Exibir as informacoes de um filme
        4) Atualizar as informacoes de um filme
        5) Excluir um filme
        6) Emprestar um filme
        7) Devolver um filme
        
        10) Cadastrar novo usuario
        11) Listar usuarios
        12) Exibir as informacoes de um usuario
        
        99) Sair""")

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
        if CheckElement(dict_movie, name_movie):
            print(dict_movie[name_movie])
    elif command == 4:
        name_movie = input("Digite o filme cujas informacoes serao atualizadas: ")

        if CheckElement(dict_movie, name_movie):
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

        if CheckElement(dict_movie, name_movie):
            del dict_movie[name_movie]
    elif command == 6:
        name_user = input("Digite o nome do usuario que ira emprestar: ")
        name_movie = input("Digite o nome do filme a ser emprestados: ")

        if CheckElement(dict_user, name_user):
            if dict_user[name_user]["qtd"] > 0:
                print("Usuario ja possui filme alugado")
            else:
                if CheckElement(dict_movie, name_movie):
                    qtd_borrow = int(input("Digite a quantidade a ser emprestada: "))
                    day_borrow = int(input("Digite o dia da locao: "))
                    while qtd_borrow > dict_movie[name_movie]["qtd"]:
                        qtd_borrow = int(input("Quantidade insuficiente em estoque, digite outro valor: "))
                    dict_movie[name_movie]["qtd"] -= qtd_borrow
                    dict_user[name_user]["movie"] = name_movie
                    dict_user[name_user]["qtd"] += qtd_borrow
                    dict_user[name_user]["day_ini"] += day_borrow
    elif command == 7:
        name_user = input("Digite o nome do usuario que ira devolver: ")

        if CheckElement(dict_movie, dict_movie[name_user]["movie"]):
            day_end = int(input("Digite o dia que o filme esta sendo devolvido: "))
            dict_movie[dict_movie[name_user]["movie"]]["qtd"] += dict_user[name_user]["qtd"]
            time_period = day_end - dict_user[name_user]["day_ini"]
            value_return = dict_movie[dict_movie[name_user]["movie"]]["valor"] * dict_user[name_user]["qtd"] * time_period
            dict_user[name_user].update({"qtd": 0, "day_ini": 0})
            print(f"Custo de devolucao: R$ {value_return:.2f}")
    elif command == 10:
        name_user = input("Digite o nome do usuario: ")
        dict_user[name_user] = dict(nome=name_user,
                                    movie=None,
                                    qtd=0,
                                    day_ini=0)
    elif command == 11:
        for user in dict_user:
            print(user)
    elif command == 12:
        name_user = input("Digite o usuario cujas informacoes serao exibidas: ")
        if CheckElement(dict_user, name_user):
            print(dict_user[name_user])
    elif command == 99:
        break
    else:
        print("Opcao invalida")