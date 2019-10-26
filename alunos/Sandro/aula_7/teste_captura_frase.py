from captura_frase_internet import speak


def test_speak():
    assert len(speak()) > 10, 'A frase precisa ser menor que 10 caracteres'


if __name__ == '__main__':
    test_speak()


