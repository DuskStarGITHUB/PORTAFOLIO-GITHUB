/*====================================================================
----------------------------Funcion replace()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion replace(), se declara un string y se inicializa despues se remplaza la parte que queremos del string al final se depsliega el resultado.]

====================================================================*/

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <conio.h>
#include <string>

// SIMPLIFICADO DE CODIGO
using namespace std;

// CUERPO DE PROGRAMA
int main()
{
    // DECLARACCION DE STRING
    string mensaje = "Hola, mundo!";
    cout << "El mensaje es: " << mensaje << endl;
    // Reemplazar "mundo" con "amigos" utilizando replace()
    mensaje.replace(6, 5, "amigos");
    cout << "Mensaje modificado: " << mensaje << endl;
    // fin de programa
    getch();
    return 0;
}
