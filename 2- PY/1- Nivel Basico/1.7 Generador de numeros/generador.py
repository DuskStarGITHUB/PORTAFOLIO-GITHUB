"""Titulo: |Generador de numeros aleatorios"""

#####################################################################################
# Descripción: <Generar numeros aleatorios>
# Autor: <DuskStar>
# Fecha de creación: <04/04/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <Ejecutar el prohrama y se generara un numero aleatorio cada que lo indiques.>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <Este programa funciona solo ejecutandose por terminal.>
# ──────────────────────────────────────────────────────────────────────────────

# LIBRERIAS
import random


# ENCAEZADO
print("\t\t|Generador de Numeros|\n")
print("\tDEV: DuskStar\t\tVersion: 1.0\n")

# INTERACTIVIDAD Y GENERACION
while True:
    print("Quieres generar un numero?")
    try:
        respuesta = str.lower(input("--> "))
        match respuesta:
            case "si":
                numero = int(random.randint(0,1000000))
                print(f"Tu numero es: {numero}")
            case "no":
                print("Hasta la proxima!!!")
                break
            case _:
                print("Debe ser un si o un no.")
    except ValueError:
        print("Entrada no valida. " + ValueError)