from operaciones import sumar, resta, multiplicar, dividir

def test_sumar():
    assert sumar(8, 2) ==10
    
def test_resta():
    assert resta(12, 2) ==10
    
def test_multiplicar():
    assert multiplicar(5, 2) ==10
    
def test_dividir():
    assert dividir(numero2=0,numero=20) == 0