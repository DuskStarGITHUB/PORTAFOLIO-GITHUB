/*====================================================================
----------------------------Funcion front()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion front(), Pide una entrada al usuario para el string y despues despliega en pantalla el primer caracter.]

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

    // Acceso al primer carácter utilizando front()
    char primerCaracter = mensaje.front();

    // Mostrar el primer carácter
    cout << "El primer carácter es: " << primerCaracter << endl;

    // Fin de programa
    getch();
    return 0;
}
