"""Titulo: |Tu pass WIFI|"""
#####################################################################################
# Descripción: <Script,te muestra las contraseñas de tu wifi ocultas en tu maquina>
# Autor: <DuskStar>
# Fecha de creación: <29/08/2023>
# Notas: <Solo funciona en WINDOWS>
#####################################################################################

import subprocess

# Función para obtener contraseñas de redes Wi-Fi
def get_wifi_passwords():
    """Funcionde procesos"""
    # Obtener los nombres de las redes Wi-Fi almacenadas en el sistema
    output_profiles = subprocess.run(
        ["netsh", "wlan", "show", "profiles"],
        capture_output=True, text=True, shell=True, check=False)
    # Extraer los nombres de los perfiles de redes
    profile_names = [
        line.split(":")[1].strip()
        for line in output_profiles.stdout.splitlines() if "Perfil de todos los usuarios" in line]
    # Inicializar lista para almacenar nombres de red y contraseñas
    wifi_passwords = []
    # Iterar a través de los perfiles de redes
    for profile_name in profile_names:
        print(f"Obteniendo información de perfil: {profile_name}")
        # Construir y ejecutar el comando para obtener detalles del perfil Wi-Fi
        cmd = f"netsh wlan show profile name=\"{profile_name}\" key=clear"
        output = subprocess.run(cmd, capture_output=True, text=True, shell=True, check=False)
        lines = output.stdout.splitlines()
        # Buscar y almacenar la contraseña si está presente en la salida
        for line in lines:
            if "Contenido de la clave" in line:
                password = line.split(":")[1].strip()
                wifi_passwords.append((profile_name, password))
    # Devolver la lista de nombres de red y contraseñas
    return wifi_passwords

def main():
    """Funcion de despiegue en pantalla"""
    # Obtener contraseñas de redes Wi-Fi utilizando la función get_wifi_passwords()
    wifi_passwords = get_wifi_passwords()
    # Verificar si se encontraron contraseñas
    if len(wifi_passwords) == 0:
        print("\nNo se encontraron contraseñas de redes Wi-Fi.")
    else:
        print("\nContraseñas de redes Wi-Fi encontradas:\n")
        # Mostrar nombres de red y contraseñas en la consola
        for network, password in wifi_passwords:
            print(f"Red: {network}")
            print(f"Contraseña: {password}\n")

# Verificar si el script está siendo ejecutado directamente
if __name__ == "__main__":
    # Llamar a la función principal 'main()' para iniciar el programa
    main()
