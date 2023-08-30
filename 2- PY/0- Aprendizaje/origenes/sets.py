# Set significa grupo o conjunto

# Set en si es una coleccion de datos que no se puede repetir y tampoco esta ordenada
print(" ")
grupo = {1, 1, 2, 2, 3, 4}
print(grupo)  # si ejecutas en consola veras que los elementos no se repiten
print(" ")

# con el set s epuede trabajar similar a las listas

# Podemos agregar  y eliminar elementos

grupo.add(5)
grupo.remove(2)
print(grupo)
print(" ")
# Esto eliminara elementos  o añadira un elemeto peor de forma automatica python no interpeta lso elementos repetidos en si los elimina

# Para trasnformar una lista a un set es de la siguiente manera

primer = {1, 2, 3, 4, 5}
segundo = [6, 7, 8, 9, 10]

segundo = set(segundo)  # Aqui hacemos iterable para convertirlo a set
print(primer | segundo)
print(" ")

# Otro ejemplo de lo anterior dicho mas nueva xpresion ampersand


primer = {2, 2, 2, 4, 5}
segundo = [3, 1, 2]

segundo = set(segundo)  # Aqui hacemos iterable para convertirlo a set
print(primer | segundo)  # Devuelve la combinacion de ambas listas
print(
    primer & segundo
)  # Delvuelve solo los elementos que se encuentren repetidos en ambos sets osea el 2 del segundo set se encuentra en el prime rset son los unicos que se repiten llamado ese operador interseccion
print(primer - segundo) #Calcula la diferencia entre dos sets quitandole al primero los duplicados del segundo
print(" ")

primerizo = {2, 2, 2, 4, 5}
segundozo = [3, 1, 2]
segundozo = set(segundozo)  # Aqui hacemos iterable para convertirlo a set
print(primerizo ^ segundozo) #La diferencia simetrica nos va devolver los valores que se encuentren en el primer set y en el segundo pero que no se encuentren en ambos
print(" ")
