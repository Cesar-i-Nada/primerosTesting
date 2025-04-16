def es_palindromo(palabra):
    return palabra == palabra[::-1]

def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if letra() in "aeiouAEIOU":
            contador += 1
    return contador