"""Titulo: |Modulos de generacion de json|"""

#####################################################################################
# Descripción: <En este modulo esta las funnciones de terminal>
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

# LIBRERIAS

import time
import sys

# FUNCIONES

def clean_text(retraso):
    """LIMPIAR TEXTO"""
    time.sleep(retraso)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
