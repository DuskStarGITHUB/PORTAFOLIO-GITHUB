"""Titulo: |Detector de numeros primos|"""

#####################################################################################
# Descripción: <Programa que analiza numeros y te dice cuales son primos>
# Autor: <DuskStar>
# Fecha de creación: <03/04/2023>
#####################################################################################

# ──────────────────────────────────────────────────────────────────────────────
# Instrucciones:
#   <Indicarle cuantos numeros son, indicarle al programa cuales son y este te
#   dira cuales son los numeros primos.>
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Notas:
#   <Este programa funciona solo ejecutandose por terminal.>
# ──────────────────────────────────────────────────────────────────────────────

# ENCAEZADO
print("\t\t|Detector de numeros primos|\n")
print("\tDEV: DuskStar\t\tVersion: 1.0\n")

# PROGRAMA
def es_primo(numero):
    """FUNCION DE DETECCION DE NUMEROS PRIMOS"""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    """FUNCION PRINCIPAL"""
    while True:
        try:
            cantidad_numeros = int(input("Ingrese la cantidad de números a registrar: "))
            if cantidad_numeros <= 0:
                print("Debes almenos comprobar un numero con este programa.")
            else:
                print()
                numeros = []
                for i in range(cantidad_numeros):
                    while True:
                        try:
                            numero = int(input(f"Ingrese el número {i + 1}: "))
                            break
                        except ValueError:
                            print(f"Entrada no valida: {ValueError}")
                    numeros.append(numero)
                primos = [num for num in numeros if es_primo(num)]
                print("\nLos números primos de la lista son:")
                for primo in primos:
                    print(primo)
                break
        except ValueError:
            print(f"Entrada no valida: {ValueError}")

if __name__ == "__main__":
    main()
