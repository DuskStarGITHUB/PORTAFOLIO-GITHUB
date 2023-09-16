/*====================================================================
----------------------------Funcion resize()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion resize(),Depsues el usuario en terminal ingresa su string, si la palabra tiene un tamaño menor a 20 se completa con guiones medio si lo cubre entonces no hace falta hacer anda mas. ]

====================================================================*/

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <conio.h>
#include <string>

// SIMPLIFICADO DE CODIGO
using namespace std;

// CUEPRO DE PROGRAMA
int main()
{
    // DECLARACION DE VARIABLE
    string cadena[50] = "---------------------------------------------------------------------------------";

    // ENTRADA DE USUARIO
    cout << "Escirbe tu texto: ";
    cin >> cadena;

    // CALCULO RESIZE
    cadena.resize(20, '-');

    // SALIDA
    cout << "Cadena redimensionada: " << cadena << endl;

    // PROGRAMA FINALIZADO
    getch();
    return 0;
}
