#include <iostream>
#include <string>
using namespace std;

const int numPersonas = 3; // Cambia este valor según el número de personas a ingresar

int main() {
    string nombres[numPersonas];
    int edades[numPersonas];
    string ciudades[numPersonas];

    cout << "Ingrese datos de " << numPersonas << " personas:\n";
    for (int i = 0; i < numPersonas; i++) {
        cout << "\nPersona " << i + 1 << ":\n";
        
        cout << "Nombre: ";
        cin.ignore(); // Limpiar el buffer de entrada antes de leer la cadena
        getline(cin, nombres[i]);

        cout << "Edad: ";
        cin >> edades[i];

        cout << "Ciudad: ";
        cin.ignore();
        getline(cin, ciudades[i]);
    }

    cout << "\nDatos ingresados:\n";
    for (int i = 0; i < numPersonas; i++) {
        cout << "\nPersona " << i + 1 << ":\n";
        cout << "Nombre: " << nombres[i] << endl;
        cout << "Edad: " << edades[i] << endl;
        cout << "Ciudad: " << ciudades[i] << endl;
    }

    return 0;
}
