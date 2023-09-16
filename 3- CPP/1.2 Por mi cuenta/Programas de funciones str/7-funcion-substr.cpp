/*====================================================================
----------------------------Funcion subsrt()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion subsrt(), Pide una entrada al usuario para el string y despues despliega en pantalla el la sub cadena resultante.]

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
    // DECLARACION DE STRING
    string mensaje;
    // ENTRADA
    cout << "Ingresa tu mensaje: ";
    cin >> mensaje;
    // Obtener una subcadena utilizando substr()
    string subcadena = mensaje.substr(2, 5); // Obtener 5 caracteres a partir del índice 2
    cout << "La subcadena es: " << subcadena << endl;
    // Fin de programa
    getch();
    return 0;
}
