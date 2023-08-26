# LOS OPERAODRES LOGICOS SON SON AND, OR ,NOT puede haber varios en una instruccion

print(" ")

# EN ESTE CASO NO PODEMOS UN COMPARADOR LOGICO PUES LAS VARIABLES YA TIENE SI ES TRUY O FALSY OSEA VALOR BOOLEANO

# EN OPERADOR AND AMBOS TIENE QUE SE VERDADERO SI NO NO SE EJECUTA LA INSTRUCCION
gas = True
encendido = True
if gas and encendido:
    print("Puedes avanzar")
    print(" ")

# SI AMBOS SON FALSE O UNO ES FALSE NO SE EJECUTA LA INSTRUCCION POR LO QUE NO HAY NADA EN CONSOLA EN ESTE CASO DE EJEMPLO:
gas = False
encendido = False
if gas and encendido:
    print("Puedes avanzar")
    print(" ")

# EL OPERADOR LOGICO CON QUE UNO SEA TRUY O VERDADERO O TRUE SE EJECITA LA INSTRUCCION PERO SI AMBOS SON FALSO NO SE EJECUTARA
gas = False
encendido = True
if gas or encendido:
    print("Puedes avanzar x2")
    print(" ")

# AQUI EL EJEMPLO DE QUE EN CONSOLA NO SE EJECUTA NADA CUANDO AMBOS SON FALSE EN EL OPERADOR OR
gas = False
encendido = False
if gas or encendido:
    print("Puedes avanzar x2")
    print(" ")

# EN EL COMPARADOR NOT ES NEGACION CAMBIARA A TRUE UN VALOR FALSO SI LAS VARIABLES TIENE UN VALOR BOOLEANO FALSY FALSE O FALSO
gas = False
encendido = False
if not gas or encendido:
    print("Puedes avanzar x3")
    print(" ")

# CUANDO HAY VARIOS OPERADORES LOGICOS SI SON DEL MISMO OPERADOR TODO BIEN PERO SI HAY DISTINTOS COMBINADOS EN UNA INSTRUCCION HAY QUE USAR PARENTESIS

gas = True
encendido = True
edad = 18
if gas and encendido and edad > 17:
    print("Puedes avanzar x4")

# AQUI ES NECESARIO ESPECIFICAR CON PARENTESIS EL ORDEN EN QUE PYTHN EJECUTARA LAS INTRUCCIONES PUE SPYTHON NO SABRA QUE EJECUTAR PRIMERO

# EN ESTE CASO VA EVALUAR PRIMERO LO QUE ESTA DENTRO D ELOS APRENTESIS LUEGO EL GAS
gas = True
encendido = True
edad = 15
if gas and (encendido or edad > 17):
    print("Puedes avanzar x4.2")
    print(" ")

# AHORA VAMOS USARO LOS 3 OPERADORES LOGICOS

gas = False
encendido = True
edad = 10
if not gas and (encendido or edad > 17):
    print("Puedes avanzar x5")
    print(" ")
