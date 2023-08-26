animmal = "Gato"
animal = " perro"
animals = "perro Gato"
espaciado = "    HOLA   MUNDO"
espaciados = " H O L A   M U N D O"
print(animmal)
# Upper es metodos algo como una funcion, metodo en si es una funcion que se encuentra dentro de un objeto, este metodo lo que realiza es hacer un string de minusculas a mayusculas
print(animmal.upper())
# La contraparte de upper es lower y se encarga de pone rlos caracteres en minusculas.
print(animmal.lower())
# Otro metodo de los string es capitalize que hace el primer caracter en mayuscula y strip evita hacer mayuscula un espaciado vacio, y con ello podemos encatenar metodos.
print(" ")
print(animal.strip().capitalize())
# Otro metodo es title, toma la primera letra de cada palabra y la hace mayscula
print(animals.title())
# STRIP es un metodo que hagarra los espacios y lo borra de  el comienzo y final de un string.
print(" ")
print(espaciados)
print(espaciados.strip())
# Tambien podemos por separado llamar los espacios de cada lado de un strng de el principio o del final con l de left o r de rifght.
print(espaciado.lstrip())
print(espaciado.rstrip())
# COMO OBTENER EL INDICE DE UN CARACTER DE UNA CADENA DE CARACTERES DIVIDIENDO EN PARTES LA MSIMA CADENA Y SI DA -1 ES QUE LA DACENA QUE BUSCAMSO NO EXISTE ENE L STRING
print(" ")
print(animmal.find("to"))
print(animmal.find("ñam"))
# Para remplazar una cadena de caracteres de un string es con replace indicando primeor la cadena a cambiar y el valor novedoso par el string y i no lo encuentra no hara nada.
print(" ")
print(animals)
print(animals.replace("Gato", "Pez"))
# Busqueda de caracteres, la diferencia con find es que find te da el indice, la busqueda  te dice si se encuentra con un valor booleano en la variable la cadena de un string.
print("MUNDO" in espaciado)
# La anterior es para saber si se encuentra peor tambien podemos preguntar si no se encuentra, en este caso dice si porque no se encuentra pero si se encontraria deria false pues si se encuentra.
print("ÑAM" not in espaciado)
