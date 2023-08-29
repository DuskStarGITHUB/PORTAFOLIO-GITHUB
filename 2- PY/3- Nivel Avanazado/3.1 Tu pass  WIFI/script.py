"""Titulo: |Tu pass WIFI|"""

#####################################################################################
# Descripción: <Script,te muestra las contraseñas de tu wifi ocultas en tu maquina>
# Autor: <DuskStar>
# Fecha de creación: <29/08/2023>
#####################################################################################

import subprocess

def get_wifi_passwords():
    """Procesos"""
    # Obtener los nombres de las redes
    output_profiles = subprocess.run(
        ["netsh", "wlan", "show", "profiles"],
        capture_output=True, text=True, shell=True, check=False)
    profile_names = [
        line.split(":")[1].strip()
        for line in output_profiles.stdout.splitlines() if "Perfil de todos los usuarios" in line]
    wifi_passwords = []
    for profile_name in profile_names:
        cmd = f"netsh wlan show profile name=\"{profile_name}\" key=clear"
        output = subprocess.run(cmd, capture_output=True, text=True, shell=True, check=False)
        lines = output.stdout.splitlines()
        for line in lines:
            if "Contenido de la clave" in line:
                password = line.split(":")[1].strip()
                wifi_passwords.append((profile_name, password))
    return wifi_passwords

def main():
    """Funcion Principal"""
    wifi_passwords = get_wifi_passwords()
    if len(wifi_passwords) == 0:
        print("No se encontraron contraseñas de redes Wi-Fi.")
    else:
        print("Contraseñas de redes Wi-Fi encontradas:\n")
        for network, password in wifi_passwords:
            print(f"Red: {network}")
            print(f"Contraseña: {password}\n")

if __name__ == "__main__":
    main()
