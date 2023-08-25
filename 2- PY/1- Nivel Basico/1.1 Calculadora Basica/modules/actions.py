"""Titulo: |MODULO DE FUNCIONES DE TERMINAL|"""

#####################################################################################
# Descripción: <FUNCIONES PARA DESPLIEGUE EN PANTALLA>
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
import os
import sys


# FUNCIONES

def clean_terminal():
    """FUNCION PARA LIMPIAR TERMINAL"""
    print()
    print("Porcesando...")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')

def text_process():
    """DESPLIEGUE DE MENSAJE Y DESPAARECE"""
    print()
    print("Procesando...")
    time.sleep(2)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

def clean_text():
    """FUNCION PARA BORRAR LINEA ANTERIOR"""
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
