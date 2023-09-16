print(" ")
lista = [1, 2, 3, 4]
print(lista)
print(" ")

# Este puede desempaquetar
print(*lista)
print(" ")

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Se pueden sumar listas
combinada = [*lista1, *lista2]
print(combinada)
print(" ")

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Se pueden sumar listas
combinada = ["Lista 1", *lista1, "Lista 2", *lista2, "Fin de listas"]
print(combinada)
print(" ")


# Se pueden desempaquetar diccioarios
nombres = {1:"DUSKSTAR"}
iden = {2:"ASUNA"}

diccionario= {**nombres,**iden, 3:"TRON"}

print(diccionario)
