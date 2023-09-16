# Si uno quiere retomar valores de una funcin y darselas a otraes posible con return


# En este caso definimos una funcion llamada suma le asignamos dos parametros su operacion es una suma y se le asigna a una variable llamado resultao despues hacemos un return de resultado para asignarlo a una varibale que queremos
def suma(a, b):
    resultado = a + b
    return resultado


# Cuando indicamos c= decimos que es variable es igual al return de la funcion llamada osea c=resultado en este caso, decimos 1+2=3=resultado=c, c=3, c=3+2=resultado=d, d=5
c = suma(1, 2)
d = suma(c, 2)

# En si estamso imprimiendo d érp es en verad un return de resultado final.
print(d)

# Al hacer un return en una funcion detienem como un break la ejecucion de la funcion en la que se encuentre y toma el valor y se lo asigna a la variable dicha
