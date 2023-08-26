# Si te das cuenta hay dos funciones definidas con las misma variable pero aqui es el elacance d euna funcion y es quecuando se realiza un proceso o se declara una variable esta solo existe dentro del bloque de la funcion, en si solo puedes usarla dentro de la funcion no fuera osea puedes repetir variables en distintas declaraciones de funcione spues para cada una es una nueva variable pues solo para esa funcion puede ser usada ya fuera no.

print(" ")
saludo = "ÑAM NYA"  # A ESTO SE LE LLAMA CONTEXTO GLOBAL


def saludar():
    saludo = "HOLA DUSKSTAR"
    print(saludo)


def saludousuario():
    saludo = "HOLA USUARIO"


def saludos():
    global saludo  # Aqui le decimos a python que saludo e suna variable global
    print(saludo)  # Aqui usamos una llamada a la variable global


saludar()  # LLAMDA DE UNA FUNCION
print(" ")
saludos()  # LLAMADA DE OTRA FUNCION
print(" ")

# Usar variables globlaes se considera mala practiva porque a largo plazo en un mismo codigo es malo tiene muchos errores de analissi te olvidas que interfieren en codigo futuro y demas cosas que puede suceder ocn una variable global
