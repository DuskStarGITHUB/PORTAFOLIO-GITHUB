print(" ")


def no_space(palabra):
    nueva_palabra = ""
    for char in palabra:
        if char != " ":
            nueva_palabra += char
    return nueva_palabra


def reverse(palabra):
    palabra_revertida = ""
    for char in palabra:
        palabra_revertida = char + palabra_revertida
    return palabra_revertida


def es_palindromo(palabra):
    palabra = no_space(palabra)
    palabra_revertida = reverse(palabra)
    palabra = palabra.lower() == palabra_revertida.lower()
    print(palabra)


es_palindromo(palabra=input("Escribe la palabra: "))
