from cadenas import es_palindromo, contar_vocales

def test_es_palindromo():
    assert es_palindromo("arroz") == False
    assert es_palindromo("verso") == False
    assert es_palindromo("oso") == True
    assert es_palindromo("reconocer") == True
    
def test_contar_vocales():
    assert contar_vocales("arroz") == 2
    assert contar_vocales("verso") == 2
    assert contar_vocales("oso") == 2
    assert contar_vocales("reconocer") == 4