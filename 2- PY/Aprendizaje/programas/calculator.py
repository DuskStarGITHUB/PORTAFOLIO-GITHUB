"""Titulo: |Calculadora Intemedia|"""

################################################################################
# Descripción: <Una calculadroa de uso en consola y con  funciones intermedia>
# Autor: <DuskStar>
# Fecha de creación: <24/07/2023>
################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
# <La calculadora funciona por medio de consola,
# tiene diversas interfazces repetitivas para estar
# haciendo operaciones y el programa solo se detendra cuando el suuario a traves de consola lo diga
# , mientars siga en funconamiento el programa podra clacular diversas operaciones matematicas>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <Version 1>
# ──────────────────────────────────────────────────────────────────────────────

# Importacion de librerias
import time
import sys

# NONE

# Interfaz inicial

nombre = input("Hola " + "Para comenzar dime tu nombre: ")
NOMBRE = str(nombre)
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")

if nombre == "":
    while nombre == "":
        nombre = input("Hola " + "Enserio dime tu nombre: ")
        NOMBRE = str(nombre)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def mostrar_procesando():
    """Un mensaje temporal en consola"""
    print("Procesando...", end="", flush=True)
    time.sleep(2)
    print("\r", end="", flush=True)


def interfaz():
    """Funcion de la interfaz de operaciones"""
    print("Hola!!! " + NOMBRE)
    print(" ")
    print("1- Suma")
    print("2- Resta")
    print("3- Division")
    print("4- Multiplicacion")
    print("5- Elevacion por exponente")
    print("6- Raiz Cuardrada")
    print("7- Resto de una division")
    print("8- Comparacion de Numeros")
    print("9- Generar un Numero Aleatorio")
    print("10- Cerrar Programa")
    print(" ")


def switch_case():
    """Operaciones de la calculadora"""
    if case == 1:
        print("Hora de hacer una Suma " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        while True:
            try:
                cantidad_numeros = int(input("¿Cuántos números hay que sumar?: "))
                numeros = []

                if cantidad_numeros > 1 and cantidad_numeros != "":
                    mostrar_procesando()
                    break
                else:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    print("Vaya " + NOMBRE + " Al menos debo sumar 2 numeros")
                    time.sleep(2)
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")

            except ValueError:
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print(
                    "No pude entender cuantos numeros debo sumar intentalo de nuevo "
                    + NOMBRE
                )
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")

        for i in range(cantidad_numeros):
            while True:
                try:
                    numero = float(input(f"Ingrese el número {i + 1}: "))
                    numeros.append(numero)
                    break
                except ValueError:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    print("No puedo entender ese número. Por favor, ingrese un número válido.")
                    time.sleep(1.5)
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")

        suma = sum(numeros)
        print("La suma de tus números " + NOMBRE + " es: ", suma)
        print(" ")

    elif case == 2:
        print("Hora de hacer una Resta "+ NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 3:
        print("Hora de hacer una Division " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 4:
        print("Hora de hacer una multiplicacion " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 5:
        print("Hora de hacer una Elevacion por Exponente " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 6:
        print("Hora de hacer una Raiz Cuadrada " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 7:
        print("Hora de hacer un calculo para sacar Resto de una division " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 8:
        print("Hora de hacer una comparacion de numeros " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 9:
        print("Hora de hacer una comparacion de numeros " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    elif case == 10:
        print("Okay Hasta luego " + NOMBRE)
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


mostrar_procesando()

interfaz()

while True:
    while True:
        try:
            operador = int(
                input("Dime el número de opción de la accion que debo realizar: ")
            )
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

            if operador >= 1 and operador <= 10:
                mostrar_procesando()
                break
            else:
                print("Vaya esa opcion no esta inlcuida " + NOMBRE)
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")

        except ValueError:
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("¡Error! Debes ingresar un número entero " + NOMBRE)
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

    case = operador
    print("¡Entendido!")
    time.sleep(1)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    switch_case()
    if case == 10:
        sys.exit()
    print("Tarea terminada...")
    time.sleep(2)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    mostrar_procesando()
    interfaz()
