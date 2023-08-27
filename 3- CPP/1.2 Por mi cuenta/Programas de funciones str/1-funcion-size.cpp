/*====================================================================
----------------------------Funcion size()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion size(),En terminal el usuario ingresa su strin, el programa maneja el string de el texto para leer la longitud de la misma]

====================================================================*/

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <conio.h>
#include <string>

// SIMPLIFICADO DE CODIGO
using namespace std;

// INICIO DEL PROGRAMA
int main()
{
    // DECLRACION DE VARIABLES
    string palabra = "---------------------------------------------------------------------------------"; // VARIABLE TIPO STRING
    size_t longitud; // VARIABLE TIPO LONG
    // ENTRADA DE USUARIO
    cout << "Cual es tu texto: ";
    cin >> palabra;
    // PROCESO DE TEXTO
    longitud = palabra.size();

    // IMPRESION EN PANTALLA
    cout << "Cadena de texto: " << palabra << endl;
    cout << "Longitud de la cadena: " << longitud << endl;

    // FIN DE PROGRAMA
    getch();
    return 0;
}
