try:
    with open("DB.txt", "r") as file:
        lines_DB = file.readlines()
except FileNotFoundError:
    lines_DB = []
    print("Não há base de dados, iniciando com valores nulos")

import json

if lines_DB:
    dict_flow = json.loads(lines_DB[0])
    dict_user = json.loads(lines_DB[1])
    dict_movie = json.loads(lines_DB[2])
else:
    dict_flow = {}
    dict_user = {}
    dict_movie = {}

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

        20) Informacoes do fluxo de locacoes

        99) Sair e salvar
        999) Sair sem salvar""")

from func_cadastrar_filmes import check_element, check_borrow

try:
    while True:
        command = int(input("\nDigite a ação desejada: "))
        if command == 1:
            name_movie = input("Digite o nome do filme: ")
            if not (check_element(dict_movie, name_movie)):
                qtd_movie = int(float(input("Digite a quantidade de filmes: ")))
                value_movie = float(input("Digite o valor da diária [R$]: "))
                year_movie = int(float(input("Digite o ano do filme: ")))
                dict_movie[name_movie] = dict(title=name_movie,
                                              qtd=qtd_movie,
                                              valor=value_movie,
                                              ano=year_movie)
            else:
                print(f"Filme {name_movie} ja cadastrado")
        elif command == 2:
            for movie in dict_movie:
                print(movie)
        elif command == 3:
            name_movie = input("Digite o filme cujas informacoes serao exibidas: ")
            check_element(dict_movie, name_movie)
        elif command == 4:
            name_movie = input("Digite o filme cujas informacoes serao atualizadas: ")

            if check_element(dict_movie, name_movie):
                print("""                    1) Quantidade
                        2) Valor da diaria [R$]
                        3) Ano do filme""")
                command_att = int(input("Digite a qual informaca voce deseja atualizar: "))
                info_att = float(input("Digite para qual valor essa informacao sera atualizada: "))
                if command_att == 1:
                    dict_movie[name_movie]['qtd'] = int(info_att)
                elif command_att == 2:
                    dict_movie[name_movie]['valor'] = info_att
                elif command_att == 3:
                    dict_movie[name_movie]['ano'] = int(info_att)
                else:
                    print("Opcao invalida")
        elif command == 5:
            name_movie = input("Digite o nome do filme a ser deletado: ")

            if check_element(dict_movie, name_movie):
                del dict_movie[name_movie]
        elif command == 6:
            name_user = input("Digite o nome do usuario que ira emprestar: ")
            name_movie = input("Digite o nome do filme a ser emprestados: ")

            if check_element(dict_user, name_user) and check_element(dict_movie, name_movie):
                if check_borrow(dict_flow, dict_user, name_user, name_movie):
                    day_borrow = int(input("Digite o dia da locacacao: "))
                    qtd_borrow = int(input("Digite a quantidade a ser emprestada: "))
                    while qtd_borrow > dict_movie[name_movie]['qtd']:
                        qtd_borrow = int(input("Quantidade insuficiente em estoque, digite outro valor: "))
                    from random import random

                    id_borrow = int(random() * 10e7)
                    dict_movie[name_movie]['qtd'] -= qtd_borrow
                    dict_user[name_user]['borrow'].append(id_borrow)
                    dict_flow[id_borrow] = dict(id=id_borrow,
                                                user=dict_user[name_user],
                                                title=name_movie,
                                                qtd=qtd_borrow,
                                                day=day_borrow)
                    print(f"Filme locado sob o ID de locacao {id_borrow}")
        elif command == 7:
            id_borrow = int(input("Digite o ID da locacao: "))
            if check_element(dict_flow, id_borrow):
                day_end = int(input("Digite o dia que o filme esta sendo devolvido: "))
                time_period = day_end - dict_flow[id_borrow]['day']
                qtd_borrow = dict_flow[id_borrow]['qtd']
                title_borrow = dict_flow[id_borrow]['title']
                user_borrow = dict_flow[id_borrow]['user']['name']
                dict_movie[title_borrow]['qtd'] += qtd_borrow
                value_return = dict_movie[title_borrow]['valor'] * qtd_borrow * time_period
                dict_user[user_borrow]['borrow'].remove(id_borrow)
                del dict_flow[id_borrow]
                print(f"Custo de devolucao: R$ {value_return:.2f}")
        elif command == 10:
            name_user = input("Digite o nome do usuario: ")
            if not (check_element(dict_user, name_user)):
                info_user = input("Digite o CPF do usuario: ")
                dict_user[name_user] = dict(name=name_user,
                                            info=info_user,
                                            borrow=[])
            else:
                print(f"Usuario {name_user} ja cadastrado")
        elif command == 11:
            for user in dict_user:
                print(user)
        elif command == 12:
            name_user = input("Digite o usuario cujas informacoes serao exibidas: ")
            check_element(dict_user, name_user)
        elif command == 20:
            print(dict_flow)
        elif command == 99:
            break
        elif command > 990:
            raise OverflowError(f"Command maior que 999: {command}, a base de dados não será salva")
        else:
            print("Opcao invalida")
except KeyboardInterrupt:
    print("Código interrompido via teclado")
except Exception:
    print("Comando invalido")

json_flow = json.dumps(dict_flow)
json_user = json.dumps(dict_user)
json_movie = json.dumps(dict_movie)

with open("DB.txt", "w") as file:
    file.write(f"{json_flow}\n{json_user}\n{json_movie}\n")