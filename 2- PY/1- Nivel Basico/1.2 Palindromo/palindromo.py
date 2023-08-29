"""Titulo: |Evaluacion de Palindromo|"""

#####################################################################################
# Descripción: <Programa que permite evaluar si una palabra es un palindromo>
# Autor: <DuskStar>
# Fecha de creación: <12/06/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <Ingresa una palabra, te dira con falso o verdadero si es un palindromo>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <N/A>
# ──────────────────────────────────────────────────────────────────────────────

print(" ")

def no_space(palabra):
    """MANIPULACIONDE PALABRA"""
    nueva_palabra = ""
    for char in palabra:
        if char != " ":
            nueva_palabra += char
    return nueva_palabra

def reverse(palabra):
    """ANALISIS"""
    palabra_revertida = ""
    for char in palabra:
        palabra_revertida = char + palabra_revertida
    return palabra_revertida

def es_palindromo(palabra):
    """CONDICION"""
    palabra = no_space(palabra)
    palabra_revertida = reverse(palabra)
    palabra = palabra.lower() == palabra_revertida.lower()
    print(palabra)

# ENTRADA
es_palindromo(palabra=input("Escribe la palabra: "))
