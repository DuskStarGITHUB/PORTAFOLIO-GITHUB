# Los diccionarios son de los datos mas usados en python en conjunto con las listas.

# Estructura basica y forma de llamar un elemento.
print(" ")

punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])
print(" ")

# Forma de añadir un valor
punto["z"] = 45
print(punto)
print(" ")

# Metodo para buscar un elemento por si existe o no existe
# Si existe se ejecuta i no existe no se ejecuta
if "lala" in punto:
    print("encontre lala", punto["lala"])

# Manera correcta y elegante de llamar un elemento
print(punto.get("x"))
print(
    punto.get("wazaa")
)  # AQUI SI LLAMAMOS UN ELEMENTO INEXISTENTE CERA NONE PERO PODEMOS PONERLE UN VALOR POR DEFECTO SI ES EL CASO
print(punto.get("wazaaa", 100))
print(" ")

# Para eliminar un elemento

del punto["x"]  # Podemos eleminar in dato
del punto["y"]  # podemos tambien eliminar una llave
print(punto)
print(" ")

punto["x"] = 25

# Si quiero iterar todas las llaves de un diccionario es con for y solo devuelve las llaves dle diccionario

for valor in punto:
    print(valor)
print(" ")

# Si queremos iterar los valores de las llaves de un diccionario es asi:

for valor in punto:
    print(valor, punto[valor])
print(" ")

# Otra manera mas conveniente es con el metodo items peor nos evuelve tuplas

for valor in punto.items():
    print(valor)
print(" ")

# Como recordamos podemos desempaquetar las tuplas
for llave, valor in punto.items():
    print(valor)
# Hay diversas maneras
for llave, valor in punto.items():
    print(llave, valor)
print(" ")


# UNA VISTA MAS REAL DE LOS DICCIONARIOS ES ASI:

usuarios = [
    {"id": 1, "nombre": "DuskStar"},
    {"id": 2, "nombre": "ASUNA"},
    {"id": 3, "nombre": "TRON"},
    {"id": 4, "nombre": "MELCRON"},
]

for usuario in usuarios:
    print(usuario["nombre"])
