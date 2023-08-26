# Primeor sabemos que podemso iterar una lista con for pero hay una forma mas elegante de escribir lo siguiente
# print(" ")
# usuarios = [
#     ["DARKRE",4], ["DUSKSTAR",1], ["TRON",3],["STREAK",5], ["LASER",2]
#     ]

# nombres =[]

# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# print(" ")

# La forma elegante de tranformar para solo mostrar la comulmna d eindice cero osea los nombres sola mente de  una lista es:

usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TRON",3],["STREAK",5], ["LASER",2]
    ]

nombres= [usuario[0] for usuario in usuarios]
print(nombres)
print(" ")

# Si queremos flitrar una lista es diciendole que el numero si es mayor a dos me de solo esos datos de identificador:
usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TRON",3],["STREAK",5], ["LASER",2]
    ]
nombres=[usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)
print(" ")

# Si queremos flitrar y modificar una lista es:
usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TRON",3],["STREAK",5], ["LASER",2]
    ]
nombres=[usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
print(" ")


# FILTRAR = FILTER
# MODIFICAR = MAP

# Lo mismo que vimos antes en manera elegante de transformar y de filtrar puede ser con expresion lambda y funciones map y filter de la siguiente manera

# ESTE ES FILTER
usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TRON",3],["STREAK",5], ["LASER",2]
    ]
nombres=list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
print(" ")
# ESTES ES MAPEADO
usuarios = [
    ["DARKRE",4], ["DUSKSTAR",1], ["TRON",3],["STREAK",5], ["LASER",2]
    ]
menosUsuarios= list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
print(" ")

