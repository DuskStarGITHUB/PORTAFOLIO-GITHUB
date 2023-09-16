"""Titulo: |Traductor EN-ES, ES-EN|"""
#####################################################################################
# Descripción: <Script,te muestra una traduccion de en a es o de es a en en tu terminal>
# Autor: <DuskStar>
# Fecha de creación: <29/08/2023>
# Nota: <Favor de descragar: pip install googletrans==4.0.0-rc1>
# Nota: <Afeca temporalmente el contenido, pero despues regresa a su idioma base>
#####################################################################################

# LIBRERIAS
import time
from googletrans import Translator

def translate_text(text, target_language):
    """Funcion de traduccion"""
    translator = Translator() # Traduce el texto al idioma especificado.
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    """Funcion Principal"""
    # Solicitar al usuario la ruta del archivo.
    input_file_path = input("Ingrese la ruta del archivo: ")
    target_language = "en"  # Idioma destino predeterminado (inglés).
    # Leer el contenido del archivo original.
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        original_text = input_file.read()
    # Mostrar el contenido original en la terminal.
    print("\nContenido del archivo:")
    print(original_text)
    # Intentar detectar el idioma del contenido original.
    try:
        detected_language = Translator().detect(original_text).lang
    except AttributeError:
        # En caso de que la detección de idioma falle, usar el idioma destino predeterminado.
        detected_language = target_language
    # Determinar el idioma destino basado en el idioma detectado.
    if detected_language == "es":
        target_language = "en"  # Si es español, traducir al inglés.
    elif detected_language == "en":
        target_language = "es"  # Si es inglés, traducir al español.
    # Traducir el contenido original al idioma destino.
    translated_text = translate_text(original_text, target_language)
    # Mostrar el contenido traducido en la terminal.
    print("\nContenido traducido:")
    print(translated_text)
    # Esperar 5 segundos antes de mostrar la traducción inversa.
    time.sleep(5)
    # Traducir nuevamente al idioma original y mostrar en la terminal.
    print("\nRetornando contenido base:")
    print(translate_text(translated_text, detected_language))

# LLAMADA CUANDO SE EJECUTA EL SCRIPT
if __name__ == "__main__":
    main()
