# Esto es un if general
edad = 15

if edad > 17:
    print("Es mayor")
    print(" ")
else:
    print("Es menor")
    print(" ")

# Esto es un if ternario

num_personas = 10

if num_personas > 10:
    mensaje = "Son muchas personas"

else:
    mensaje = "Vaya son pocas personas"

print(mensaje)
print(" ")

# Su verdadero poder es reducir codigo:
num_personas_2 = 10

mensaje_2 = "CANTIDAD GRANDE" if num_personas_2 > 20 else "CANTIDAD PEQUEÑA"

print(mensaje_2)
print(" ")
