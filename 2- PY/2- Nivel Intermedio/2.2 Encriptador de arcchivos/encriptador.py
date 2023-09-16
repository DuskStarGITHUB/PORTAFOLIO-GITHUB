"""Titulo: |Encriptador de archvos|"""

#####################################################################################
# Descripción: <Programa que permite encriptar un archivo>
# Autor: <DuskStar>
# Fecha de creación: <18/08/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <Este programa encripta el archivo de la ruta que le des en terminal>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <Clave para desecriptar el archivo prueba.txt: Win-9+VnPWrp[)EvJ<B>>
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

            def encriptador(texto, llave):
                """ENCRPTADOR DE ARCHIVOS"""
                claver = llave.encode()  # Convertir la clave en una secuencia de bytes
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

            def desencriptador(texto_encriptado, clave_desencriptador):
                """DESENCRPTADOR DE ARCHIVOS"""
                claver = (
                    clave_desencriptador.encode()
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
# ENCRIPTACION
            if operacion == "e":
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Okay elegiste encriptar.")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                clave = generar_clave()
                # CLAVE
                print("Clave generada: ( " + clave + " ) Recuerda guardarla")
                print(" ")
                # RUTA
                ruta = input("Dime la ruta del archivo a encriptar: ")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Procesando...")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                # ABRIR ARCHIVO Y MNAEJARLO
                archivo = open(ruta, "r", encoding="utf-8")
                contenido = archivo.read()
                archivo.close()
                resultado = encriptador(contenido, clave)
                archivo = open(ruta, "wb")
                archivo.write(resultado)
                archivo.close()
                # SALIDA 1
                print("Texto original:")
                print(contenido)
                print(" ")
                # SALIDA 2
                print("Resultado de la encriptación dentro de tu archivo:")
                print(resultado.decode())
# OPERACION DESENCRIPTAR
            elif operacion == "d":
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Okay elegiste desencriptar.")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                # RUTA
                ruta = input("Dime la ruta del archivo a desencriptar: ")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                # CLAVE
                clave_desencriptar = input("Ingresa la clave de desencriptación: ")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Procesando...")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                archivo = open(ruta, "rb")
                # LECTURA
                contenido_encriptado = archivo.read()
                archivo.close()
                # PROCESAMIENTO
                resultado = desencriptador(contenido_encriptado, clave_desencriptar)
                archivo = open(ruta, "w", encoding="utf-8")
                archivo.write(resultado)
                archivo.close()
                # SALIDA 1
                print("Texto encriptado:")
                print(contenido_encriptado.decode())
                print(" ")
                # SALIDA 2
                print("Resultado de la desencriptación:")
                print(resultado)
                print(" ")
# ENTRADA NO VALIDA
            else:
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Vaya no te comprendo...")
                time.sleep(2)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
# PROGRAMA FINALIZADO
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
# ENTRADA NO VALIDA
        else:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("No comprendo la respuesta")
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
# MANEJO DE ERRORES
    except ValueError:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        print("Digitalizacion de repuesta erronea")
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
print(" ")
