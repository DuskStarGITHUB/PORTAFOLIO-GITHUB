/*====================================================================
----------------------------Funcion back()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion back(), Pide una entrada al usuario para el string y despues despliega en pantalla el ultimo caracter.]

====================================================================*/

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <conio.h>
#include <string>

// SIMPLIFICADO DE CODIGO
using namespace std;

// CUERPO DE PROGRAMA
int main() {

    // Declaración de variables
    string mensaje;

    // Entrada de usuario
    cout << "Ingresa tu mensaje: ";
    cin >> mensaje;

    // Acceso al último carácter utilizando back()
    char ultimoCaracter = mensaje.back();

    // Mostrar el último carácter
    cout << "El ultimo caracter es: " << ultimoCaracter << endl;

    // Fin de programar
    getch();
    return 0;
}
