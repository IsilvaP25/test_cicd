from src.calculadora import sumar

def test_sumar_correcto():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-1, -1) == -2