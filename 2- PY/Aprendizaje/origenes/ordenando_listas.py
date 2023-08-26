print(" ")
# Tuplas
numeros = [10, 3, 6, 2, 1, 4, 7, 5, 8, 9]

# Con el metodo sort una secuencia de datos numericos se ordena de manera ascendete
numeros.sort()
print(numeros)
print(" ")

# Con la misma funcion se puede establecer lo cotrario a lo predeterminado, recordemos que predeterminadamente es ascendete mientras que  el metodo srt puede aplicar un argumento a la misma para ocnfigurar su comportamiento en el siquiente ejemplo veremos de forma descendente la lista.
print(" ")
numeros.sort(reverse=True)
print(numeros)
print(" ")

# Otro metodo para ordenar los elementos d euna lista es con sorted
numeros_2 = sorted(numeros)
print(numeros_2)
# A diferencia de sprt esa genera una nueva lista que no afectara la lista original mientras que sort si afecta la lista original
print(" ")

# Como sorted tiene un argumento aplicable
numeros_2= sorted(numeros, reverse=True)
print(numeros_2)
print(" ")

# Si queremos ordenar listas con sub listas dentro siempre debe terne el id primero o un identificador numerico
usuarios = [
    [4,"DARKRE"], [1, "DUSKSTAR"], [3,"TROM"],[5,"STREAK"], [2,"LASER"]
    ]

usuarios.sort()
print(usuarios)
print(" ")

# Otra cuestion es si aun asi queremos ordenar la lista pero un identificador esta despues y queremos ordenar la lista pues debemos decirle a python la ubicacion, con un argumento al metodo sort de una funcion con un parametor indicando el indice de el identificador y su key
usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TROM",3],["STREAK",5], ["LASER",2]
    ]
def ordena(elemento):
    return elemento[1]
usuarios.sort(key=ordena)
print(usuarios)
print(" ")

# Si queremos que sea al reves debe ser un argumento e la funcion separada con una coma
usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TROM",3],["STREAK",5], ["LASER",2]
    ]
def ordena2(elemento):
    return elemento[1]
usuarios.sort(key=ordena2, reverse=True)
print(usuarios)
print(" ")


# TUPLA MAS ELEGANTE APRA NO ESTA CREANDO FUNCIONES PUES CON SORT COMO LO HICIMOS DEBEMOS CREAR UNA FUNCION NUEVA CADA INSTANTE

# Usaremos expresiones landa con parametros y valor de retorno 

usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TROM",3],["STREAK",5], ["LASER",2]
    ]

usuarios.sort(key=lambda el:el[1])
print(usuarios)
print(" ")

