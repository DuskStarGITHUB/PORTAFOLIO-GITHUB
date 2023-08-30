print(" ")
mascotas = ["dragon", "perro", "gato", "cuervo", "caballo", "ciervo", "dragon"]
print(mascotas)
print(" ")
print(" ")


# Para agregar espacio y añadir un elemeno en un indice seria con insert

mascotas.insert(1, "Pez")  # indicamos indice y elemento a añadair
# En este caso indicamos 1 entonces entre 0 y 1 va añadir el nuevo elemento
print(mascotas)
print(" ")
print(" ")

# Si queremos agregar un elemento al final de la lista podriamos poner insert(-1, elemento) pero hay otra mejor manera

mascotas.append("dinosaurio")
print(mascotas)
print(" ")
print(" ")

# Ahora para eliminar elementos es con el metodo remove y elemento que queremos eliminar pero solo se ilimina la
# primea ocurrencia que encuentre
mascotas.remove("caballo")
print(mascotas)
print(" ")
print(" ")
print(" ")

# Otra maera de eliminar el ultimo elemento d ela lista

mascotas.pop()
print(mascotas)
print(" ")
print(" ")
print(" ")

# Y tambien con el metodo pop podemos borrar un elemento conforme su indice

mascotas.pop(0)
print(mascotas)

# El metodo correcto para elimminar un indice es on del

del mascotas[4]
print(mascotas)
print(" ")
print(" ")
print(" ")

# Por ultimo si queremos limmpiar por completo un arreglo es con el metodo clear

mascotas.clear()
print(mascotas)
print(" ")
