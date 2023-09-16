"""Titulo: |Calculadora Basica|"""

#####################################################################################
# Descripción: <Programa que permite realizar operaciones basicas de una calculadora>
# Autor: <DuskStar>
# Fecha de creación: <14/08/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <Este programa se ejecuta por medio de linea de comandos>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <N/A>
# ──────────────────────────────────────────────────────────────────────────────

# LIBRERIAS Y MODULOS
import time
from modules.actions import clean_terminal, clean_text
from modules.process import suma, resta, multiplcacion, dividir
from modules.process import potencia, raiz_cuadrada, porcentaje, valor_absoluto, resto

# VARIABLES INICIALES
operations = [
    ("Suma", "+"),
    ("Resta", "-"),
    ("Multipicacion", "*"),
    ("Division", "/"),
    ("Potencia", "**"),
    ("Raiz Cuadrada", "//"),
    ("Porcentaje", "%"),
    ("Valor Absoulto", "|x|"),
    ("Resto", "..."),
    ("Salir", "</>")
]

# FUNCION PRINCIPAL

def main():
    """MENU PRINCIPAL"""
    print("|Calculadora Basica|")
    print()
    print("Operaciones de la calculadora:")
    print()
    # ITERACION DE LISTA Y AGREGANDO EL CARACTER (|)
    max_length = max(len(name) for name, _ in operations)
    for name, symbol in operations:
        print(f"\t{name:<{max_length}} | {symbol}")
    print()

def entrada_interfaz_usuario():
    """ENTRADA DE LA OPCION DE USUARIO"""
    while True:
        try:
            print("¿Qué operación quieres realizar?")
            operador = str(input("\t--> "))
            if operador == "":
                while operador == "":
                    clean_text()
                    clean_text()
                    print("¿Qué operación quieres realizar?")
                    operador = str(input("\t--> "))
            return operador.title()
        except ValueError:
            print("Hubo un error")

def navegacion(operador):
    """Navegacion en el programa"""
    while True:
        # OPERACION SUMA
        if operador == "Suma" or operador == "+" or operador == "Sum" or operador == "1":
            terminando = "no"
            suma()
            return terminando
        # OPERACION RESTA
        elif operador == "Resta" or operador == "-" or operador == "Res" or operador == "Minus" or operador == "2":
            terminando = "no"
            resta()
            return terminando
        # PÉRACION MULTIPLICACION
        elif operador == "Multiplicacion" or operador == "Mul" or operador == "Multi" or operador == "Multiplicar" or operador == "*" or operador == "Multiply" or operador == "3":
            terminando = "no"
            multiplcacion()
            return terminando
        # OPERACION DIVISION
        elif operador == "Division" or operador == "Dividir" or operador == "Divide" or operador == "/" or operador == "4":
            terminando = "no"
            dividir()
            return terminando
        # OPERACION POTENCIA
        elif operador == "Potencia" or operador == "Pot" or operador == "**" or operador == "Power" or operador == "5":
            terminando = "no"
            potencia()
            return terminando
        # OPERACION RAIZ CUADRADA
        elif operador == "Raiz Cuadrada" or operador == "Raiz" or operador == "Rc" or operador == "//" or operador == "Cuadrada" or operador == "6":
            terminando = "no"
            raiz_cuadrada()
            return terminando
        # OPERACION PORCENTAJE
        elif operador == "Porcentaje" or operador == "Percentage" or operador == "%" or operador == "7":
            terminando = "no"
            porcentaje()
            return terminando
        # OPERACION VALOR ABSOLUTO
        elif operador == "Valor Absoluto" or operador == "Valor" or operador == "Absoluto" or operador == "|x|" or operador == "Va" or operador == "8" or operador == "x" or operador == "|x|" or operador == "IxI":
            terminando = "no"
            valor_absoluto()
            return terminando
        # OPERACION RESTO
        elif operador == "Resto" or operador == "Residuo" or operador == "Sobrante" or operador == "..." or operador == "9":
            terminando = "no"
            resto()
            return terminando
        # OPERACION SALIR
        elif operador == "Salir" or operador == "Exit" or operador == "Terminar" or operador == "Finalizar" or operador == "Cerrar" or operador == "Finish" or operador == "Close" or operador == "10" or operador == "s":
            terminando = "si"
            return terminando
        # MANEJO DE ENTARDA ERRONEA
        else:
            print("Opcion no Valida.")
            print("Porfavor escribe correctamente el nombre o simbolo de la operacion")
            terminando = "no"
            time.sleep(3)
            clean_terminal()
            return terminando

# CARGA DEL PROGRAMA
if __name__ == "__main__":
    while True:
        # MENU
        main()
        # ENTRADA DE OPCION A ELEGIR
        operador_elegido = entrada_interfaz_usuario()
        programa = navegacion(operador_elegido)
        if programa == "no":
            continue
        else:
            print("Terminando Programa...")
            time.sleep(2)
            clean_text()
            clean_terminal()
            break
