nombre_owner = "DuskStar"
nombre_real = "Speencer Pulido Romero"
nombre_ia = "Asu"
nombre_completo_ia = "ASUNA LIFESTAR"
# CONCATENACION
# Significa unir varias variables o string o objetos, en este caso unimos dos variables y un texto con el simbolo plus.c
iconos_del_programa = nombre_owner + " y " + nombre_ia

print(iconos_del_programa)

# EL OPERADOR DE FORMATEO DE STRINGS
# Como usar el simbolo plus es muy anticuado y largo podemos usar el operador dicho, se us f"{}{}{}...""
iconos_de_esta_interfaz = f"{nombre_owner} y {nombre_ia} {1+1}"
print(iconos_de_esta_interfaz)