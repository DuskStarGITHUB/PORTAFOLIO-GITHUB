"""Titulo: |GENERADOR DE CONTRASEÑAS|"""

#####################################################################################
# Descripción: <Este orograma es capaz de generar contraseñas de manera dinamica>
# Autor: <DuskStar>
# Fecha de creación: <18/08/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
# <Este programa se ejecuta por medio de linea de comandos>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────

# LIBRERIAS
import random

# INICIO DE PROGRAMA
print("|GENERADOR DE CONTRASEÑAS|\n")

def main():
    """INTERFAZ INCIAL"""
    print("\nLista de caracteristicas\n")
    # LISTA DE OPCIONES
    characteristics = [
    ("1", "Numeros"),
    ("2", "Letras"),
    ("3", "Caracteres")
    ]
    # ITERACION DE LISTA
    max_length = max(len(i) for i, _ in characteristics)
    for i, characteristic in characteristics:
        print(f"\t{i:<{max_length}} - {characteristic}")
    print("\nPresiona del 1 al 3 la carcateristica que deseas para tu contraseña")

def capture():
    """CARACTERISTICAS DE LAS CONTRASEÑAS"""
    while True:
        try:
            main()
            options = set()
            options.add(int(input("--> ")))
            min_set=min(options)
            max_set=max(options)
            if min_set < 1 or max_set > 3:
                print("\nTU ENTRADA NO CORRESPONDE A UNA OPCION DE LA LISTA.\n")
            else:
                while True:
                    print("\n¿Quieres agregar otra caracteristica?")
                    print("\t|Si\n\t|No")
                    operator= str.lower(input("--> "))
                    if operator != "si" and operator != "no":
                        print("\nENTRADA NO VALIDA.\n")
                        main()
                    elif operator == "si":
                        longitud = len(options)
                        if longitud <= 3:
                            while True:
                                main()
                                options.add(int(input("--> ")))
                                min_set=min(options)
                                max_set=max(options)
                                if min_set < 1 or max_set > 3:
                                    print("\nENTRADA NO VALIDA.\n")
                                    if min_set < 1:
                                        list_pass = list(options)
                                        del list_pass[0]
                                        options= set(list_pass)
                                    elif max_set > 3:
                                        list_pass = list(options)
                                        del list_pass[-1]
                                        options= set(list_pass)
                                else:
                                    break
                        else:
                            print("Opciones completadas")
                            break
                    else:
                        break
            break
        except ValueError:
            print("\nENTRADA NO VALIDA.\n")
    lista_options=list(options)
    return lista_options

def propieties(lista):
    """ITERAR SET EN LISTA DE OPCIONES"""
    print("\nCaracteristicas de tu contraseña:")
    for manner in lista:
        if manner == 1:
            print("| Numeros")
        elif manner == 2:
            print("| Letras")
        elif manner== 3:
            print("| Caracteres")




# VARIABLE GLOBAL DE EL RETORNO DE LA FUNCION
lista_final = capture()


# PROCESO Y SALIDA

def generator(listado):
    """GENERADOR DE CONTRASEÑAS"""
    lista = []
    i=0
    while i < 7:
        for manner in listado:
            if manner == 1:
                part = str(random.randint(1, 9))
            if manner == 2:
                with open(r"PROYECTOS\1- Nivel Basico\1.2 Generador de Contraseñas\assets\letters.txt", "r", encoding="utf-8") as archive1:
                    contenido = archive1.read()
                lista_letras = list(contenido)
                part = random.choice(lista_letras)
            if manner == 3:
                with open(r"PROYECTOS\1- Nivel Basico\1.2 Generador de Contraseñas\assets\chars.txt", "r", encoding="utf-8") as archive2:
                    contenido = archive2.read()
                lista_caracteres = list(contenido)
                part = random.choice(lista_caracteres)
            lista.extend(part)
        for _ in range(21):
            random.shuffle(lista)
        i = i + 1
    password = ''.join(lista)
    return password

# LLAMADA DE FUCIONES
propieties(lista_final)
FINAL_PASSWORD = generator(lista_final)
print("\nLa contraseña generada es: "+ FINAL_PASSWORD)
