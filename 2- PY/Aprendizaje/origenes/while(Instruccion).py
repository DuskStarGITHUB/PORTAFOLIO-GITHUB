# IMAGIINEMOS QUE QUEREMOS QUE SE DUPLIQUE EL NUMERO HASTA QUE ESTE CUMPLA UNA CONIDICON
print(" ")
numero = 1

while numero < 100:
    print(numero)
    numero *=2
print(" ")

comando = ""

# TAMBIEN WHILE PUEDE IMPRIMIR COMANDOS DADOS EN TERMINAL O CONSOLA CON UN INPUT Y SIMBOLO DE DOALR Y ESTARA IMPRIMIENDO LOS COMANDO SESRITOS HSTA QUE SE ESCRIBA SALIR SOLO AHI LA CONDICION SE DEJA DE CUMPLIR Y TERMINA PROGRAMA
while comando != "salir":
    comando = input ("$ ")
    print(comando)
print(" ")

# AHO TAMBIEN, HAY MANERAS DE SCRIBIR SALIR PUES UN STRING CUENTA LSO CARACTERES COMO SON SI NO LO ESCRIBES IDENTICAMENTE PUES NO LO DETECTA COMO IGUAL AL STRING ASI QUE PODEMOS USAR LOWER O UN METODO SRING PARA ASEGURARNOS DE QUE SE ESTABLESCA UN ASIGNACION A NUETSRA VARIABLE INDEPENDIENTE DE LO QUE SE ESCRIBA OSEA SI ESCRIBIMOS SALIR CON MAYUSCULAS SERA DISTINTO A salir CON MINUSCULAS ASI QUE CON LOWER NO IMPORTA COMO LO ESCRIBA EL USUARIO PUES SE TOMARA LOS VALORES COMO MINUSCULAS PARA MAS DETALLES IR A METODOS STRINGS
comando = ""
while comando.lower() != "salir":
    comando = input ("$ ")
    print(comando)
print(" ")