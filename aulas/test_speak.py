from mensagem_dia import speak


def test_speak():
    assert len(speak()) > 10, 'A frase precisa ser menor que 10'
