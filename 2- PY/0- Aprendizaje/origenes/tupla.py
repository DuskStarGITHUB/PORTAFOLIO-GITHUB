# UN TUPLA ES COMO UNA LISTA PERO ESTA NO PODEMOS MODIFICARLA, NO SE LE PUEDE AGREGAR ELEMENTOS NI QUITAR PERO SI SE PUEDE CREAR NUEVAS TUPLAS EN BASE A TUPLAS YA EXISTENTES

# A diferencia de una lista debemos usar los parentesis redondos
print(" ")
numeros = (1, 2, 3)
print(numeros)
print(" ")

# Con los duplas se pueden encanquetar otros elementos

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)
print(" ")


# De esta manera podemos crear una tupla y como tupla puede resivir strings signifia que puede ser iterable
punto = tuple([1, 2])
print(punto)
print(" ")

# Las operaciones que podemos realizar con los duplsa son iguales que la listas a exepcion de las que modifican como añadir o eliminar un elemento

punto = tuple([1, 2])
print(punto)
# Podemos crear una nueva lista llamada menos Numeros
menosNumeros = numeros[:2]
print(menosNumeros)
# Tambien podemos desempaquutar la lista por ejemplo desempaquetamos el primero numero luego el segundo y los otros que puedan existir se crean en una nueva lista
primero, segundo, *otros = numeros
print(primero, segundo, otros)
# Como dijimos podemos iterar duplas
for n in numeros:
    print(n)
print(" ")

# En el caso que en verdad necesitemso alterar un dupla que en verdad no deberiamos podemso alterarlo de la siuiente manera

listaNumeros= list(numeros)
listaNumeros[0] = "VAYA"
print(listaNumeros)
# Si te das cuenta no alteramos el dupppla en si pues no es posible pero creaamos una nueva lista a base del dupla y esal lista la alteramos
