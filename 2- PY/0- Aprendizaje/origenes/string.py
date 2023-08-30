nombre_del_dueño = "DuskStar"
# STRING
informacion_del_dueño = """
Nombre real: Speencer Pulido Romero,
Permiso: Owner,
Edad: 19 años.
"""

print(nombre_del_dueño, informacion_del_dueño)

# Funcion len nos permite saber la longitud de un string o de cualquier otra funcion
# LEN ES FUNCION
# LO DEL PARENTECIS ES ARGUMENTO
print(len(nombre_del_dueño))
print(len(informacion_del_dueño))
# COMO INICIALIZAR UN CARACTER DE UN TEXTO
# SE EMPIEZA EL PRIMER CARACTER O PRIMER INDICE SERIA IGUAL A 0
# Al decirle que me de indice 0 nos dara de la palabra d ela variable el indice cero que es d
print(nombre_del_dueño[0])

# Como cortar un string
# Al decirle con dos putnos es que va cortar la palabra en la impresion, el primer valor es desde donde va empezar a imprimir y el segundo valor es donde termina el corte este su indice no es desde cero es desde 1.
print(nombre_del_dueño[0:4])
# Cuando no se asigna un segundo valor se corta hasya el ultimo caracter este 1 y aparte cuenta 1 extra a la derecha
print(nombre_del_dueño[4:])
# Lo mismo que antes pero con el segundo valor, aqui empieza tambien desde 1 hacia la izquierda y cuenta tambien 1 mas.
print(nombre_del_dueño[0:4])
# Cuando no ponemos valores python elije por ddefecto o que el considere.
print(nombre_del_dueño[:])
