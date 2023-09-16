print(" ")
# Tipos de listas
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["hola", "nyaa"]
palabrasFelices = ["asuna", "vida", "ia", "programar"]
booleans = [True, False, True, False, True]
matriz = [[0, 1], [1, 0]]
ceros = [0] * 10
pseudoceros = [0, 1] * 10
alfanumerico = numeros + letras
rango = list(range(10))
rage = list(range(1, 10))
chars = list("Hola Mundo")

# Manipulacion de listas

mascotas = ["Star", "RE", "Perro", "Gato"]
print(mascotas[3])
print(" ")

mascotas[2] = "Pez"
print(mascotas[2])
print(" ")

mascotas = ["Star", "RE", "Perro", "Gato"]
print(mascotas[0:3])  # El primer valor es indice del arreglo y el segundo el limite
print(mascotas[:2])
print(mascotas[2:])
print(" ")

print(mascotas[-1])  # Ire hacia el final de la lista
print(" ")

print(
    mascotas[::2]
)  # Aqui decimos oma u elemento despues salta y toma el siguiente elemento y asi sucesivamente
print(mascotas[1::2])  # AQUI HACEMOS QUEE EMPIEZE DE INDICE 1 Y SALTE EN PAR
print(" ")

numericos = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(
    (numericos[1:6:2])
)  # Decimos que empieze de uno salte de dos en dos hasta 6 como limite.
numericos = list(range(40))
print(numericos[9:39:3])
print(" ")


# Desenpaquetar listas

ide = [1, 2, 3]
# Manera fea:
# primero = ide[0]
# segundo = ide[1]
# tercero = [2]
primero, segundo, tercero = ide
print(primero, segundo, tercero)
print(" ")

# Otra manera de desempaqeutar un solo numero es asi:

ide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primero, *otros = ide  # estamos empaquetasndo menos primero en otros
print(primero)
print(primero, otros)
print(" ")

# Otra manera de elegir
ides = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeros, segundos, *otross = ides
print(primeros, segundos, otross)
print("  ")

# Otra manera
identificables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
uno, *otras, ultimo = identificables
print(uno, ultimo, otras)
print(" ")

# Tambien es posible

numeral = [1, 2, 3, 4, 5]
uno, dos, *otros, ultimo = numeral
print(uno,dos,ultimo)
print("  ")
