# la funcion print imprime en consola o en terminal.

print(" ")
print("HOLA MUNO")

# la reservacion def es para crear nuestra propia funcion seguido del nombre que queremos darle y dos puntos para declarar instrucciones.


def nombre():
    print(" ")
    print("DUSKSTAR")
    print("QUE BUENA FUNCION")
    print(" ")


# PARA USAR LA FUNCION ESTABLECIDA DEBEMOS LLAMAR DE LA SIGUIENTE MANERA SOLO CON EL NOMBRE

nombre()

# Lo bueno es que podemos llamarla las veces que queramos:

nombre()
nombre()
nombre()

# Crear una funcion permite por ejemplo imprimir un mismo formato con distinto contenido un ejemplo es usa rargumentos y parametros de una funcion

# Dentro de los paretensis va una variable que puede ser utilizada para el contexto de dicha funcion establecida


# Cuando se declara las variables deben ser obligatoria usarlas o dicha funcion no se ejecutara
def hola(nombre_variable):
    print("Hola")
    # AQUI CUANDO SE DEFINIO LA VARIABE Y SE USO EN EL CONTEXTO SE LLAMA PARAMETRO
    print(f"Bienvenid@ {nombre_variable}")


# AQUI CUANDO SE APLICA DICHA FUNCION ENE LE CONTEXTO AL USAR UNA FUNCION SE LLAMA  ARGUMENTO
hola("DuskStar")
hola("ASU")
print(" ")

# Quieres pasarle mas parametros? separalos por coma en parametros y tambien en argumentos


def nya(nombre_de_ia, nombre_usuario, mensaje_de_ia):
    print(f"{nombre_de_ia}: {mensaje_de_ia} {nombre_usuario}")


# SE APLICAN LOSA RGUMENTOS EN ORDEN
nya("Asu", "Bienvenido", "DuskStar")
print(" ")

# ARGUMENTOS OPCIONEALES SE HACEN DE LA SIGUIENTE MANERA


def whatsapp(apodo, numero=1):
    print(f"{apodo}: {numero}")


whatsapp(
    "DuskStar"
)  # Aqui por ejemplo le decimos solo un argummento pero al antes poner por defecto un vlor al parametro de numero simmplemente se pondra el valor antes pre-establecido
print(" ")

# Luego tenemos los argumentos nombrados te dejan poner en dsitinto orden los argumentos

def nota(vector, nota):
    print(f"{vector}: {nota}")

nota(nota="TRAER LECHE",vector="1") #Cuando se ctiva un nombrado todos los argumentos debe tener su nombrado
print(" ")