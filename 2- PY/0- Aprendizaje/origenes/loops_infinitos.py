# LOS LOOP INFINITOS NO TENEMOS UNA CONDICION DE SALIDA POR LO QUE SE EJECUTARIA PARA SIEMPRE

# EN ESTE CASO LE DECIMOS A WHILE A TRUE DECIMOS QUE SIEMPRE ES VERDADERO LA CONDICION POR LO QUE SIEMPRE SE EJECUTARA ES UN EJEMPLO DE BUCLE O LOOP WHILE.

# comando = ""

# while True:
#     comando = input("$ "):
#     print(comando)
# print(" ")

# CLARO ESE SIEMPRE SE EJECUTARA Y SOLO S EDETENDRA SI DETENEMOS LA EJECUCION MANUALMENTE AL CERRAR EN ESTE CASO TERMINAL

# UNA FORMA DE HACER UN CIERRE ES CON UN SI O IF SI CUMPLA UNA CONDICION HAGA UN BREAK ROMPIENDO EL WHILE Y PARANDO EL BUCLE PERO EL PROBLEMA ES QUE CUANDO SE CONSUMA LA MEMORIA SUFICIENTE O LIMITADA VA A MATR NUESTRA APLICACION ASI QUE EL LOOP SIEMPRE CONSUMIRA MUCHA MEMORIA ASI QUE SIEPRE DEBEMOS ASEGURANOS DE PONER UNA OPCION PARA DETENER EL LOOP EN ESTE CASO ES CON IF Y CLARO SIENDO QUE DETALLAMOS COMANDO = INPUT YA SE DECLARA LA VARIABLE ASI QUE NO NECESITAMOS DECLARARLA ANTES
while True:
    comando= input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
print(" ")