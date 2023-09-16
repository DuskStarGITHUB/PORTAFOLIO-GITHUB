/*====================================================================
----------------------------Funcion append()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion replace(), se declara un string con la paalbra hola y s ele pide al usuario su nombre, despues se suman los strings para formar un mensaje.]

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
    // DECLARACION DE VARIABLES TIPO STRINGS
    string saludo = "Hola ";
    string nombre;

    cout << "Ingresa tu nombre: ";
    cin >> nombre;
    // Agregar el nombre al saludo utilizando append()
    saludo.append(nombre);

    cout << saludo << endl;
    // Fin de programa
    getch();
    return 0;
}
