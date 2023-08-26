/*====================================================================
----------------------------Funcion find()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion find(), hya un stringstring y despues despliega en pantalla si el elemento que quieor busacr se encontro.]

====================================================================*/

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <conio.h>
#include <string>

// SIMPLIFICADO DE CODIGO
using namespace std;

// CUERPO DE PROGRAMA
int main() {
    // DECLARACION DE STRING
    string mensaje = "Hola, mundo!";

    // Buscar la posición de "mundo" en el mensaje utilizando find()
    size_t posicion = mensaje.find("mundo");
    // CONDICIONALES
    if (posicion != string::npos) {
        cout << "La subcadena 'mundo' fue encontrada en la posicion: " << posicion << endl;
    } else {
        cout << "La subcadena 'mundo' no fue encontrada." << endl;
    }
    // FIN DE PROGRAMA
    getch();
    return 0;
}
