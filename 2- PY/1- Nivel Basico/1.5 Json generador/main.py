"""Titulo: |Generador de JSON|"""

#####################################################################################
# Descripción: <Programa que genera un json estructurado como el usuario indique>
# Autor: <DuskStar>
# Fecha de creación: <20/08/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <ingresar en terminal los identificadores del contenido y su contenido.>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <Este programa funciona solo ejecutandose por terminal.>
# ──────────────────────────────────────────────────────────────────────────────

# IMPORTACIONES

from modules.terminal import clean_text
from modules.poo import generator_json

# FUNCIONES

def main():
    """Encabezado"""
    print("\t\t|Generador de Json|")
    print("\tVersión: 2.0\tDeveloper: DuskStar\n")

def menu():
    """Interfaz"""
    main()
    with open(
        r"PROYECTOS\1- Nivel Basico\1.5 Json generador\assets\documents\instructions.txt",
        "r",encoding="utf-8") as instructions:
        content_instructions = instructions.read()
        print(content_instructions + "\n")

def inputs():
    """Entradas de usuario"""
    print("Cantidad de apartados?")
    while True:
        try:
            paragraphs = int(input("--> "))
            # CANTIDAD DE APARTADOS APRA JSON
            if paragraphs < 1:
                print("Debes tener al menos 1 apartado para tu json.")
                clean_text(3)
            elif paragraphs > 12:
                print("Cuando queires almacenar mas de 12 claves deberias considerar usar una BD")
                clean_text(5)
            # LOGICA DE REGISTRO
            else:
                break
        # MANEJO DE ERROR DE EXEPCION
        except ValueError:
            print(f"Entrda no valida {ValueError}")
            clean_text(2)
    return paragraphs

if __name__ == "__main__":
    menu()
    sections = inputs()
    while True:
        try:
            NOMBRE = str(input("\nNombre del archivo: "))
            print()
            break
        except ValueError:
            print("Campo Vacio")
            clean_text(3)
    generator_json(sections,NOMBRE)
