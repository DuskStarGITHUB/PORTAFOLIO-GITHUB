"""Titulo: |Calculadora Cientifica|"""

#####################################################################################
# Descripción: <Operaciones de calculadora cientifica>
# Autor: <DuskStar>
# Fecha de creación: <27/08/2023>
#####################################################################################

import math

print("Calculadora Científica")

while True:
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("11. Salir")
    opcion = int(input("Ingrese la opción deseada: "))
    match opcion:
        case 1:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(num1, "+", num2, "=", num1 + num2)
        case 2:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(num1, "-", num2, "=", num1 - num2)
        case 3:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(num1, "*", num2, "=", num1 * num2)
        case 4:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(num1, "/", num2, "=", num1 / num2)
        case 5:
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            print(base, "^", exponente, "=", pow(base, exponente))
        case 6:
            num = float(input("Ingrese un número: "))
            print("Raíz cuadrada de", num, "=", math.sqrt(num))
        case 7:
            num = float(input("Ingrese un número: "))
            print("Seno de", num, "=", math.sin(num))
        case 8:
            num = float(input("Ingrese un número: "))
            print("Coseno de", num, "=", math.cos(num))
        case 9:
            num = float(input("Ingrese un número: "))
            print("Tangente de", num, "=", math.tan(num))
        case 10:
            num = float(input("Ingrese un número: "))
            print("Logaritmo de", num, "=", math.log(num))
        case 11:
            break
        case _:
            print("Opción inválida")

print("Fin del programa")
