"""Titulo: |Encriptador|"""

#####################################################################################
# Descripción: <Encriptador de archivos>
# Autor: <DuskStar>
# Fecha de creación: <27/08/2023>
#####################################################################################

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

def encrypt_file(file_path1):
    """ENCRIPTADOR"""
    with open(file_path1, 'rb') as file:
        original = file.read()
    encrypted = f.encrypt(original)
    with open (file_path1, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path2):
    """DESENCRIPTADOR"""
    with open(file_path2, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = f.decrypt(encrypted)
    with open(file_path2, 'wb') as dec_file:
        dec_file.write(decrypted)

if __name__ == "__main__":
    while True:
        choice = input("Que deseas hacer? (e)ncrypt/(d)ecrypt: ")
        if choice == 'e':
            file_path = input("Introduce la ruta del archivo a encriptar: ")
            encrypt_file(file_path)
            print("Archivo encriptado")
        elif choice == 'd':
            file_path = input("Introduce la ruta del archivo a desencriptar: ")
            decrypt_file(file_path)
            print("Archivo desencriptado")
        else:
            print("Opción inválida")
            break
