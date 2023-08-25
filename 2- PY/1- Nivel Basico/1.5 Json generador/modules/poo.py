"""Titulo: |Modulos de generacion de json|"""

#####################################################################################
# Descripción: <En este modulo esta la POO par generar un diccionario para un json>
# Autor: <DuskStar>
# Fecha de creación: <20/08/2023>
#####################################################################################

# ────────────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <Importar el modulo llamando las funciones a ocupar.>
# ────────────────────────────────────────────────────────────────────────────────────

# ────────────────────────────────────────────────────────────────────────────────────
# Notas:
#   <Uso libre.>
# ────────────────────────────────────────────────────────────────────────────────────

#LIBRERIAS Y MODULOS
import json
import os

class InputData:
    """Almacen"""
    def __init__(self):
        self.data = {}
    def get_user_input(self,count):
        """ENTRADA"""
        for i in range(count):
            nombre_apartado = input(f"Nombre apartado {i+1}: ")
            contenido = input("Contenido: ")
            self.data[nombre_apartado] = contenido
    def save_to_json(self,new):
        """GENERADOR"""
        filename = os.path.join(os.getcwd(), new + ".json")
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)


def generator_json(section_number,nombre_json):
    """GENERADOR CON POO"""
    count = section_number
    data_entry = InputData()
    data_entry.get_user_input(count)
    nombre_archivo = nombre_json
    data_entry.save_to_json(nombre_archivo)
    print("\nDatos guardados en", nombre_archivo , ".json")
