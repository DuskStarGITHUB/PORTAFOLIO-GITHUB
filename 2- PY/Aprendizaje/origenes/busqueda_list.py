print(" ")
# Si queremos busca un elemnto d euna lista podemos usar el metodo index

mascotas = ["perro", "gato", "cuervo", "caballo", "ciervo"]

print(mascotas.index("cuervo"))
print(" ")
# Con ese metodo al final encontramos su indice contando desde cero.

# Pero si e n una lsta un elemento esta repetido se cuenta el prime relemento encontrado y para saber ambos datos realmente hay otra fomra


mascotas = ["ciervo", "perro", "gato", "cuervo", "caballo", "ciervo"]

print(mascotas.index("ciervo"))
print(" ")
# La otra forma es saber cuantas veces se encuentra un elemento de una lista con el metodo count

mascotas = ["perro", "gato", "cuervo", "caballo", "ciervo","gato"]

print(mascotas.count("gato"))#contara cuantsa veces esta
print(mascotas.index("gato")) #Aqui dice el indice del primer elemento que encuentra