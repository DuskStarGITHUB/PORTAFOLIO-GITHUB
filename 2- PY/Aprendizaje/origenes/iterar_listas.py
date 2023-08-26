# Lo genial de las listas es que son iterables
who = ["asuna", "duskstar", "asu", "star"]

# El metodo enuerate es un metodo que realiza una enumeracion a nuestras iteraciones y con ello sabemos que etsamos iterando con for nuestra lista llamada who que tiene strings
for name in enumerate(who):
    print(name)
print(" ")
# Dentro de este metodo te activa otro pseudo metodo llaado tupla que es hacer lamado a la columna de nuestra iteracion
for name in enumerate(who):
    print(name[0]) #Aqui definimos tupla 0
for name in enumerate(who):
    print(name[1]) #Aqui tupla 1
print(" ")
print(" ")
print(" ")

# Lo anterior es lo mismo a una empaquetacion
mascotas=["perros","gatos","pajaros","loros","lobos","cuervos"]

primero,segundo=[1,2]
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
print(" ")