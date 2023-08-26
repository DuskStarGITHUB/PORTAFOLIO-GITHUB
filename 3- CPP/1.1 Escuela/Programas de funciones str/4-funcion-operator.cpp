/*====================================================================
----------------------------Funcion operator[]---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion operator[], Pide una entrada al usuario par ael string y despues el indice a buscar y despliega en pantalla su caracter correspondiente a ese indice.]

====================================================================*/

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <conio.h>
#include <string>

// SIMPLIFICADO DE CODIGO
using namespace std;

// CUERPO DE PROGRAMA
int main() {

    // DECLARACION DE VARIABLES
    string mensaje;

    // ENTRADA DE USUARIO
    cout << "Cual es tu palabra: ";
    cin >> mensaje;
    cout << "Tu mensaje es: " << mensaje << endl;

    // VARIABLE INDICE
    size_t indice;

    // ENTRADA DE INDICE
    cout << "Ingresa el indice del caracter que deseas ver: ";
    cin >> indice;
    cout<<endl;

    // VALIDAR INDICE
    if (indice >= 0 && indice < mensaje.length()) {
        char caracter = mensaje[indice];
        cout << "El caracter en el indice " << indice << " es: " << caracter << endl;
    } else {
        cout << "Indice fuera de rango. Ingresa un indice válido." << endl;
    }

    // FIN DE PROGRAMA
    getch();
    return 0;
}
