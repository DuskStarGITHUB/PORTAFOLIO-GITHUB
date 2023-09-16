# XARGS es una funcion que te permite poner todos los argumentos que quieras


# Parametro en plural (osea varios) y un asterisco inicial
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


# Aqui en argumentos en esta ocasion seria interables y como todo iterable se le puede aplicar un for
suma(2, 3, 9)
suma(9, 8, 7)
suma(0, 3, 23, 4)
suma(1, 2)
print(" ")


# En WARGS KER ARGUMENS aqui debe ser dos astericos


def get_product(**datos):
    print(datos)


# Cadda que se usa XARG debemos poner un nombre a nustro argumento
get_product(
    id="id", name="Iphone", dec="Esto e sun telefono"
)  # ESTO SE LE CONOCE COMO DICCIONARIO

# En WARGS i queremos argumentos decididos a nuestro criterio
print(" ")


def get_productos(**datos):
    print(datos["id"], datos["name"])


# Cadda que se usa XARG debemos poner un nombre a nustro argumento
get_productos(id="1", name="Iphone", dec="Esto e sun telefono")
print(" ")
