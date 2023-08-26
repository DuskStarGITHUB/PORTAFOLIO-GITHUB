/*====================================================================
----------------------------Funcion clear()---------------------------
====================================================================

-------------------
Autor: Speencer Pulido Romero
Alias: DuskStar
Fecha: 17/08/2023

-------------------
Descripción del Programa:
[Se logra viazulizar el codigo y aplicacion de la funcion clear(),Depsues el usuario en terminal ingresa su string, se le pide al usuario que confirme el string si pulsa si se imprime y si no se borra y se pide ingresar un nuevo valor. ]

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
    // DELCARACION DE VARIABLES
    string cadena = "";
    int op = 1;
    cout << "Ingresa tu palabra: ";
    cin >> cadena;
    cout << endl;
    do
    {
        cout << "Tu palabra es: " << cadena << endl;
        cout << endl;
        cout << "Es correcto?\n";
        cout << "Teclea 1 para confirmar" << endl;
        cout << "Teclea 2 para volver a registrar una palabra" << endl;
        cout << "--> ";
        cin >> op;
        cout << endl;
        switch (op)
        {
        case 1:
            break;
        case 2:
            cadena.clear();
            cout << "Registro vaciado" << cadena << endl;
            cout << "Ingresa tu nueva palabra: ";
            cin >> cadena;
            cout << endl;
            break;
        default:
            cout << "Entrada no valida" << endl;
            cout << "Porfavor teclea 1 o 2" << endl;
            cout << "--> ";
            cin >> op;
            cout << endl;
            break;
        }
    } while (op != 1);

    cout << "Palabra resgitrada: " << cadena << endl;

    // PROGRAMA FINALIZADO
    getch();
    return 0;
}
