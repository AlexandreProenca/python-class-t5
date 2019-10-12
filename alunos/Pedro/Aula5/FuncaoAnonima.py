z = lambda x, y: x**2 + y ** 2

print(z(1, 2))

# lista de dicionarios
dict_users = [
    dict(nome="Pedro", telefone="32132331"),
    dict(nome="Sandro", telefone="31421412"),
    dict(nome="Lucas", telefone="14241412")
    ]

k = sorted(dict_users, key=lambda x: x['nome'])
print(k)


def retorna_contato(contato):
    return contato['nome']


j = sorted(dict_users, key=retorna_contato)
print(j)
