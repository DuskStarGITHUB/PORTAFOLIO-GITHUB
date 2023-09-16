#include <iostream>
#include <conio.h>
using namespace std;

const int tamano = 5;

int main() {
    int ModificarArray[tamano];

    cout << "Ingrese " << tamano << " numeros enteros:\n";
    for (int i = 0; i < tamano; i++) {
        cout << "Ingrese el valor para el indice " << i << ": ";
        cin >> ModificarArray[i];
    }

    cout << "\nIndice\tContenido\n";
    for (int i = 0; i < tamano; i++) {
        cout << i << "\t" << ModificarArray[i] << endl;
    }

    char opcion;
    cout << "\nDesea modificar algun dato? Teclee s para modificar datos o cualquier otra tecla para terminar el programa: ";
    cin >> opcion;

    if (opcion == 's' || opcion == 'S') {
        int indice;
        int nuevoValor;

        cout << "Ingrese el numero de indice a modificar (0-" << tamano - 1 << "): ";
        cin >> indice;

        if (indice >= 0 && indice < tamano) {
            cout << "Ingrese el nuevo valor: ";
            cin >> nuevoValor;

            ModificarArray[indice] = nuevoValor;

            cout << "\nContenido actualizado del array:\n";
            for (int i = 0; i < tamano; i++) {
                cout << i << "\t" << ModificarArray[i] << endl;
            }
        } else {
            cout << "Indice invalido. El indice debe estar entre 0 y " << tamano - 1 << ".\n";
        }
    }
getch();
    return 0;
}
