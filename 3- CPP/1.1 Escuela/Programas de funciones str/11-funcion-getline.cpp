/*====================================================================
----------------------------Funcion getline()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion getline(),Se obtiene la linea ingresada por el usuario y se reitera al usuario cual fue la liena capturada .]

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
    // DECLARACION D EVARIABLE TIPO STRING
    string linea;
    // ENTRADA
    cout << "Ingresa una linea de texto: ";
    // Leer una línea completa desde la entrada estándar utilizando getline()
    getline(cin, linea);
    cout << endl;
    // SALIDA
    cout << "Linea capturada: " << linea << endl;
    // FIN D EPROOGRAMA
    getch();
    return 0;
}