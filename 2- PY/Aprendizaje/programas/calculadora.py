# INTERFAZ INICIAL
n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa un segundo numero: ")
print("Tus numero son: ", n1, " y ", n2)
print(" ")

# CONVERCION MANUAL DE LOS INPUT QUE SON STRING INCILMENTE A VALOR ENTERO
n1 = int(n1)
n2 = int(n2)

# OPERACIONES DE CALCULADORA
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}.
El reultado de una la suma es: {suma}.
El resultado de una resta es: {resta}.
El resultado de una multipliacion es: {multiplicacion}.
El resultado de una division es: {division}.
"""

print(mensaje)