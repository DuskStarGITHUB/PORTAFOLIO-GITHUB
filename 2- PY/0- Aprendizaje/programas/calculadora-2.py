print(" ")
print("Bienvenido a la calculadora 2.0")
menu = """En esta calculadora tienes la capacidad de realizar las siguientes operaciones:
Sumar.
Restar.
Multiplicar.
Dividir.
"""
print(menu)
print("Escribe salir si deseas terminar.")
print(" ")

consola = ""
while True:
    if not consola:
        consola = input("Ingresa un numero : ")
        if consola.lower() == "salir":
            print("ADIOS")
            break
        consola = int(consola)
        op = input("Escribe la operacion a realizar: ")
        if op.lower() == "salir":
            print("ADIOS")
            break
        consola2 = input("Ingresa el siguiente numero: ")
        if not consola2:
            consola2 = input("Ingresa un numero : ")
        if consola2.lower() == "salir":
            break
        consola2 = int(consola)
        if op.lower() == "sumar":
            res = consola + consola2
            print("Resultado de la operacion: ", res)
        elif op.lower() == "restar":
            res = consola - consola2
            print("Resultado de la operacion: ", res)
        elif op.lower() == "multiplicar":
            res = consola * consola2
            print("Resultado de la operacion: ", res)
        elif op.lower() == "dividir":
            res = consola / consola2
            print("Resultado de la operacion: ", res)
        else:
            print("Operacion no valida")
            break
print(" ")
