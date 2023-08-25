"""Titulo: |Adivina el numero|"""

#####################################################################################
# Descripción: <Juego de adivinar el numero>
# Autor: <DuskStar>
# Fecha de creación: <03/04/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <Escribir el numero intentando adivinar el numero del progrma de acuerdo
#   al rango de eleccion.>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <Este programa funciona solo ejecutandose por terminal.>
# ──────────────────────────────────────────────────────────────────────────────

# LIBRERIA
import random
# DESPLIEGUE EN PANTALLA
print("\t\t|Adivina el numero|\n")
print("\tDEV: DuskStar\t\tVersion: 1.0\n")
print("\nCual es el numero maximo del que puedo pensar?")
# RANGO
while True:
    try:
        rango = int(input('--> '))
        if rango <= 0:
            print("Ya tomo en cuenta como minimo el cero")
        else:
            print(f"\nEl rango es (0 , {rango})\n")
            numero = random.randint(0,rango)
            break
    except ValueError:
        print(ValueError)

intentos = 0
# ENTRADA
while True:
    try:
        pensamiento =int(input("En que numero estoy pensando: "))
        intentos = intentos + 1
        if pensamiento < numero:
            print("\nPista: El numero esta por debajo del que estoy pensando")
        elif pensamiento > numero:
            print("\nPista: El numero esta por encima del que estoy pensando")
        else:
            print("Has acertado el numero!!!")
            print(f"Intentos: {intentos}")
            break
    except ValueError:
        print(ValueError)
