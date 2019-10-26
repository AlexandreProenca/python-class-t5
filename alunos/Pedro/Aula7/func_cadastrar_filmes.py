def check_element(dict_names, verify):
    try:
        print(dict_names[verify])
    except KeyError:
        print(f"Elemento {verify} nao esta cadastrado, favor cadastrar primeiro")
        return 0
    else:
        return 1


def check_borrow(flows, users, verify_user, verify_title):
    for borrow in users[verify_user]['borrow']:
        if flows[borrow]['title'] == verify_title:
            print(f"Usuario {verify_user} ja possui o filme {verify_title} alugado no ID {borrow}")
            return 0
    else:
        return 1

