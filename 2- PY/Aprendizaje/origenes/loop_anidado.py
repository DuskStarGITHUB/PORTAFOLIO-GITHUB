# UN LOOP AINADO ES TENER LOOPS DENTRO DE LOOPS

# EN ESTE CASO SE LEE DE ARRIBA HACIA ABAJO ENTONCES SIENDO EL PRIMERO FOR DETECTADO DE J LE ASIGNA A J EMPEZANDO DE CERO ASI QUE J=0 LUEGO LEE QUE EL SIGUIENTE FOR DE K D ELA MISMA MANERA K=0 ENTONCES QUEDA COMO: J=0, K=0,DESPUES VA LINEA 3 QUE ES IMPRIMIR Y IMPRIME 0,0 POR LO VALORES DE J Y K QUE DIJIMOS...

# POR ULTIMO YA SE HIZO LECTURA DE ARRIBA AHCIA ABAJO SEGUN PYTHON Y AHROA AL TERMIANR EL PROCESO ANTERIOR ESTABLECIDO PASAMOS DE NUEVO A EL SEGUNDO FOR PUES YA NO ES AL PRIMERO, UBICANDONOS AL SEGUNDO FOR SIENDO QUE AHORA K=1 PERO EL PRIMER FOR SEUIRA SIENDO J=0 PUES NO HACE CAMBIO PORQUE ESTAMOS CUMPLIENDO EL SEGUNDO FOR ANTES QUE EL PRIMERO PERO J SIGUE SIENDO EL PRIMERO.

# PARA EXPLICAR MEJOR ESTO DECIMOS PRIMER FOR, SEGUNDO FOR, PRINT EN EL PRIMER PROCESO, SEGUNDO FOR HASTA TERMINAR DE ITERAR PUES PUSIMOS LIMITE 2 Y PRINT , DEPSUES VAMSO AL PRIMER FOR I ITERAMOS HASTA COMPLETAR

# EL PRIMER FOR S ELLAMA COMO OUTER FOR O LOOP Y EL FOR SIGUIENTE ES INNER FOR O LOOP
for j in range(10):
    for k in range(7):
        print(f"{j},{k}")

# PARA MAS DETALLES DE COMPRENSION IR AL RECURSO 1