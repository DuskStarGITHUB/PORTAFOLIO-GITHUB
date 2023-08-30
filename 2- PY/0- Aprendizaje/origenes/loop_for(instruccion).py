# UN FOR PUEDE AYUDARTE EN MUCHAS COSAS PERO PRINCIPALMENTE SE USA PARA ITERAR UNA LISTA DE ELEMENTOS

# EL RANGO DE FOR COMIENZA DE 0 Y TERMINA EN ESTE CASO 4 PUES ES -1 Y ESTE ES UN ITERABLE

# AQUI ESTAMOS DICIENDO QUE PAA NUMERO TOMARA TODOS LSO VALORES DENTRO DE RANGE ENTONCES QUEDARIA QUE NUMEOR VALE 0 CADA VES QUE PASE POR RANGO VA VALER 1,2,3,4 CUANDO SEA CINCO TERMINO PUES VALE -1 ENTONCES EL ULTIMO NUMERO PLASMADO ES 4 OSEA 0 ES EL QUINTO NUMERO OSEA SON 5 NUMEROS OSEA 0,1,2,3,4,5
for numero in range(5):
    print(numero)
print(" ")

# OTRO USA ES MULTIPLICAR POR CADA PROCESO EN BUCLE DE FOR

for numero in range(5):
    print(numero, numero * "hola mundo ")
print(" ")


# AHORA VEREMOS FOR ELSE EN UN EJEMPLO DE DETENERSE CUANDO SE ENCUENTRA UN NUMERO
buscar = 3

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
print(" ")

# Supongamos que no encontramos el elemento
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("NO ENCONTRE EL NUMERO BUSCADO")
print(" ")

# EJEMPLO DE UNA IMPRESION DE PALABRA

for char in "DuskStar":
    print(char)
print(" ")

# Impresion normal de array o arreglo por su traduuccion

arreglo = ["ñam1", "ñam2", "ñam3", "ñam4", "ñam5"]

for elemento in arreglo:
    print(elemento)
