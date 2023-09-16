"""Titulo: |ENCRIPTADOR BASICO|"""

################################################################################
# Descripción: <Este programa encripta archivos>
# Autor: <DUSKSTAR>
# Fecha de creación: <25/07/2023>
################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <En consola se indica la ruta del
# archivo con texto a encriptar y se encriptara
# tambien puedes indicar si quieres encriptar o desencriptar>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <NA>
# ──────────────────────────────────────────────────────────────────────────────

import time
import sys
import random
import string

print(" ")
while True:
    try:
        print(" ")
        pregunta = str(input("¿Hola quieres abrir el programa? (si/no): ").lower())

        def generar_clave():
            """GENERADOR DE CLAVE"""
            longitud = 20  # Longitud de la clave generada
            caracteres = string.ascii_letters + string.digits + string.punctuation
            clave_generada = "".join(random.choice(caracteres) for _ in range(longitud))
            return clave_generada

        if pregunta == "si":
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("Procesando...")
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

            operacion = input(
                "Presiona E para encriptar o D para desencriptar: "
            ).lower()

            def encriptador(texto, clave):
                """ENCRPTADOR DE ARCHIVOS"""
                claver = clave.encode()  # Convertir la clave en una secuencia de bytes
                texto_encriptado = b""
                for caracter in texto.encode():
                    caracter_encriptado = bytes(
                        [
                            caracter ^ claver[i % len(claver)]
                            for i, caracter in enumerate(caracter.to_bytes(1, "big"))
                        ]
                    )
                    texto_encriptado += caracter_encriptado
                return texto_encriptado

            def desencriptador(texto_encriptado, clave_desencriptar):
                """DESENCRPTADOR DE ARCHIVOS"""
                claver = (
                    clave_desencriptar.encode()
                )  # Convertir la clave en una secuencia de bytes
                texto_desencriptado = ""
                for i, caracter in enumerate(texto_encriptado):
                    caracter_desencriptado = bytes(
                        [
                            caracter ^ claver[i % len(claver)]
                            for i, caracter in enumerate(caracter.to_bytes(1, "big"))
                        ]
                    )
                    texto_desencriptado += caracter_desencriptado.decode()
                return texto_desencriptado

            if operacion == "e":
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Okay elegiste encriptar.")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                clave = generar_clave()
                print("Clave generada: ( " + clave + " ) Recuerda guardarla")
                print(" ")
                ruta = input("Dime la ruta del archivo a encriptar: ")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Procesando...")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                archivo = open(ruta, "r", encoding="utf-8")
                contenido = archivo.read()
                archivo.close()
                resultado = encriptador(contenido, clave)
                archivo = open(ruta, "wb")
                archivo.write(resultado)
                archivo.close()
                print("Texto original:")
                print(contenido)
                print(" ")
                print("Resultado de la encriptación dentro de tu archivo:")
                print(resultado.decode())

            elif operacion == "d":
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Okay elegiste desencriptar.")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                ruta = input("Dime la ruta del archivo a desencriptar: ")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                clave_desencriptar = input("Ingresa la clave de desencriptación: ")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Procesando...")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                archivo = open(ruta, "rb")
                contenido_encriptado = archivo.read()
                archivo.close()
                resultado = desencriptador(contenido_encriptado, clave_desencriptar)
                archivo = open(ruta, "w", encoding="utf-8")
                archivo.write(resultado)
                archivo.close()
                print("Texto encriptado:")
                print(contenido_encriptado.decode())
                print(" ")
                print("Resultado de la desencriptación:")
                print(resultado)
                print(" ")

            else:
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Vaya no te comprendo...")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")

        elif pregunta == "no":
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("Entendido")
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("Finalizando Programa...")
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            break

        else:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("No comprendo la respuesta")
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

    except ValueError:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        print("Digitalizacion de repuesta erronea")
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
print(" ")