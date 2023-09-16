"""Titulo: |MODULO DE FUNCIONES DE CALCULOS|"""

#####################################################################################
# Descripción: <FUNCIONES DE LA CLACULADORA BASICA>
# Autor: <DuskStar>
# Fecha de creación: <15/08/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <IMPORTAR COMO MODULO PARA HACER USO DE ESTAS FUNCIONES>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <N/A>
# ──────────────────────────────────────────────────────────────────────────────

# LIBRERIAS
import time
import math
from .actions import clean_terminal, clean_text, text_process #SI MARCA EROR ES PROBLEMA DE MALA EJECUCION

def suma():
    """FUNCION PARA SUMAR NUMEROS"""
    clean_terminal()
    # BUCLE DE CANTIDAD DE NUMEROS
    while True:
        print("¿Cuántos números quieres sumar?")
        try:
            cantidad_numeros = int(input("\t--> "))
            if cantidad_numeros < 2:
                clean_text()
                clean_text()
                print("Debes sumar al menos 2 numeros")
                time.sleep(2)
                clean_text()
            else:
                print("Sumaremos entonces " + str(cantidad_numeros) + " números")
                clean_terminal()
                break
        except ValueError:
            clean_text()
            clean_text()
            print("¡!Vaya, esa entrada no es válida!!")
            time.sleep(2)
            clean_text()
    # VARIABLES
    numeros = []
    i = 1
    suma_total = 0
    # PROCESOS
    while i <= cantidad_numeros: #registro de numeros
        try:
            numeros.append(float(input("Ingresa el valor del número " + str(i) + ": ")))
            i += 1
        except ValueError:
            clean_text()
            print("Has ingresado un valor errorneo")
            time.sleep(2)
            clean_text()
    for numero in numeros: #suma de los numeros
        suma_total += numero
    print()
    print("La suma total de los números es "+ str(suma_total))
    print()
    time.sleep(6)
    clean_terminal()

def resta():
    """FUNCION PAR RESTAR NUMEROS"""
    clean_terminal()
    #  BLUCE DE CANTIDAD DE NUMEROS
    while True:
        print("¿Cuántos números quieres restar?")
        try:
            cantidad_numeros = int(input("\t--> "))
            if cantidad_numeros < 2:
                clean_text()
                clean_text()
                print("Debes restar al menos 2 numeros")
                time.sleep(2)
                clean_text()
            else:
                print("Restaremos entonces " + str(cantidad_numeros) + " números")
                clean_terminal()
                break
        except ValueError:
            clean_text()
            clean_text()
            print("¡!Vaya, esa entrada no es válida!!")
            time.sleep(2)
            clean_text()
    # VARIABLES
    numeros = []
    i = 1
    # PROCESOS
    while i <= cantidad_numeros: #registro de numeros
        try:
            numeros.append(float(input("Ingresa el valor del número " + str(i) + ": ")))
            i += 1
        except ValueError:
            clean_text()
            print("Has ingresado un valor errorneo")
            time.sleep(2)
            clean_text()
    #VARIABLE TOTAL
    resta_total = numeros[0] # resta toma el valor de el numero con indice 0 d eel array
    # RESTAR NUMEROS
    for numero in numeros[1:]:  # Empezar desde el segundo número en adelante
        if resta_total < 0:  # Si resta_total es negativo, sumar en lugar de restar
            resta_total = resta_total + numero
        else:
            resta_total = resta_total - numero
    print()
    print("La resta de los números da un resultado de "+ str(resta_total))
    time.sleep(4)
    clean_terminal()

def multiplcacion():
    """FUNCION PAR MULTIPLICAR NUMEROS"""
    clean_terminal()
    #  BLUCE DE CANTIDAD DE NUMEROS
    while True:
        print("¿Cuántos números quieres multiplicar?")
        try:
            cantidad_numeros = int(input("\t--> "))
            if cantidad_numeros < 2:
                clean_text()
                clean_text()
                print("Debes multiplicar al menos 2 numeros")
                time.sleep(2)
                clean_text()
            else:
                print("Multiplicaremos entonces " + str(cantidad_numeros) + " números")
                clean_terminal()
                break
        except ValueError:
            clean_text()
            clean_text()
            print("¡!Vaya, esa entrada no es válida!!")
            time.sleep(2)
            clean_text()
    # VARIABLES
    numeros = []
    i = 1
    # PROCESOS
    while i <= cantidad_numeros: #registro de numeros
        try:
            numeros.append(float(input("Ingresa el valor del número " + str(i) + ": ")))
            i += 1
        except ValueError:
            clean_text()
            print("Has ingresado un valor errorneo")
            time.sleep(2)
            clean_text()
    #VARIABLE TOTAL
    multiplcacion_total = numeros[0]
    # RESTAR NUMEROS
    for numero in numeros[1:]:  # Empezar desde el segundo número en adelante
        multiplcacion_total *= numero
    print()
    print("El resultado de la multiplicacion de los numeros es de "+ str(multiplcacion_total))
    time.sleep(4)
    clean_terminal()

def dividir():
    """FUNCION PARA DIVIDIR NUMEROS"""
    clean_terminal()
    #  BLUCE DE CANTIDAD DE NUMEROS
    while True:
        print("¿Cuántos números quieres dividir?")
        try:
            cantidad_numeros = int(input("\t--> "))
            if cantidad_numeros < 2:
                clean_text()
                clean_text()
                print("Debes dividir al menos 2 numeros")
                time.sleep(2)
                clean_text()
            else:
                print("Dividiremos entonces " + str(cantidad_numeros) + " números")
                clean_terminal()
                break
        except ValueError:
            clean_text()
            clean_text()
            print("¡!Vaya, esa entrada no es válida!!")
            time.sleep(2)
            clean_text()
    # VARIABLES
    numeros = []
    i = 1
    # PROCESOS
    while i <= cantidad_numeros: #registro de numeros
        try:
            numeros.append(float(input("Ingresa el valor del número " + str(i) + ": ")))
            i += 1
        except ValueError:
            clean_text()
            print("Has ingresado un valor errorneo")
            time.sleep(2)
            clean_text()
    #VARIABLE TOTAL
    division_total = numeros[0]
    # RESTAR NUMEROS
    for numero in numeros[1:]:  # Empezar desde el segundo número en adelante
        division_total /= numero
    print()
    print("El resultado de la division de los numeros es de "+ str(division_total))
    time.sleep(4)
    clean_terminal()

def potencia():
    """Funcion para potenciar un numero"""
    clean_terminal()
    while True:
        try:
            num1 = float(input("¿Cuál es el número base? "))
            while True:
                try:
                    num2 = float(input("¿A qué potencia deseas elevarlo? "))
                    break
                except ValueError:
                    clean_text()
                    print("Entrada no Valida.")
                    time.sleep(2)
                    clean_text()
            resultado = num1 ** num2
            text_process()
            print(f"{num1} elevado a la potencia {num2} es igual a {resultado}")
            time.sleep(5)
            clean_terminal()
            break
        except ValueError:
            clean_text()
            print("Entrada no Valida.")
            time.sleep(2)
            clean_text()

def raiz_cuadrada():
    """FUNCION DE RAIZ CUADRADA"""
    clean_terminal()
    while True:
        try:
            print("¿Cual es el numero que quieres sacar su raiz cuadrada?")
            numero = float(input("\t--> "))
            text_process()
            break
        except ValueError:
            clean_text()
            print("Entrada no valida")
            time.sleep(2)
            clean_text()
    resultado = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}")
    time.sleep(4)
    clean_terminal()

def porcentaje():
    """FUNCION PARA SACAR PORCENTAJE DE UN NUMERO"""
    clean_terminal()
    while True:
        try:
            print("¿Cual es el valor total?")
            numero = float(input("\t--> "))
            while True:
                try:
                    print("¿Que porcentaje quieres sacar?")
                    valor_porcentaje = float(input("\t--> "))
                    break
                except ValueError:
                    clean_text()
                    clean_text()
                    print("Entrada no valida")
                    time.sleep(2)
                    clean_text()
            break
        except ValueError:
            clean_text()
            clean_text()
            print("Entrada no valida")
            time.sleep(2)
            clean_text()
    text_process()
    resultado = numero * valor_porcentaje
    resultado /= 100
    print(f"El {valor_porcentaje}% de {numero} = {resultado}")
    time.sleep(4)
    clean_terminal()

def valor_absoluto():
    """VALOR ABSOLUTO DE NUMEROS"""
    clean_terminal()
    numeros = []
    while True:
        try:
            print("¿Cuantos numeros hay que sacarles su valor absoluto?")
            cantidad_numeros = int(input("\t--> "))
            if cantidad_numeros < 1:
                clean_text()
                clean_text()
                print("No se permiten números negativos.")
                time.sleep(2)
                clean_text()
            else:
                time.sleep(2)
                clean_text()
                clean_text()
                text_process()
                break
        except ValueError:
            clean_text()
            clean_text()
            print("Entrada no valida")
            time.sleep(2)
            clean_text()
    i = 1
    while True:
        while i <= cantidad_numeros:
            try:
                numeros.append(float(input("Numero " + str(i) + ": ")))
                i += 1
            except ValueError:
                clean_text()
                print("Entrada no valida")
                time.sleep(2)
                clean_text()
        break
    print()
    text_process()
    clean_text()
    print("\n-------Valores Absolutos------\n\n")
    for i, numero in enumerate(numeros, start=1):
        total_valor_absoluto = abs(numero)
        print(f"Valor absoluto del numero {i}: {total_valor_absoluto}")
    time.sleep(6)
    clean_terminal()


def resto():
    """RESIUDO DE UNA DIVISION"""
    clean_terminal()
    while True:
        try:
            print("¿Cual es el dividendo?")
            num1 = float(input("\t--> "))
            while True:
                try:
                    print("¿Cual es divisor?")
                    num2 = float(input("\t--> "))
                    text_process()
                    break
                except ValueError:
                    clean_text()
                    clean_text()
                    print("Entrada no valida")
                    time.sleep(2)
                    clean_text()
            break
        except ValueError:
            clean_text()
            clean_text()
            print("Entrada no valida")
            time.sleep(2)
            clean_text()
    residuo = num1 % num2
    print(f"{num1} / {num2} = {residuo}")
    time.sleep(8)
    clean_terminal()
