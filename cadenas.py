def es_palindromo(palabra):
    palabra_al_reves = palabra[::-1]
    return palabra == palabra_al_reves

def contar_vocales(palabra):
    contador = 0
    palabra = "aeiouAEIOU"
    for letra in palabra:
        if letra in palabra:
            contador += 1
    return contador

