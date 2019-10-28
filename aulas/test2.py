from calculadora import somar, dividir, subtrair

def test_somar():
    assert somar(1,1) == 2, 'Erro'

def test_dividir():
    assert dividir(2,1) == 2, 'Erro'

def test_subtrair():
    assert subtrair(2,1) == 1, 'Error'


