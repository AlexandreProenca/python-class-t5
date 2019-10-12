# funcao se chama método e variável se chama atributo
class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def idade(self, hoje):
        hd, hm, ha = hoje
        nd, nm, na = self.nascimento
        _idade = ha - na
        return _idade


x = Pessoa(nome="Pedro", nascimento=[16, 3, 1995])
print(x.idade([12, 10, 2019]))
