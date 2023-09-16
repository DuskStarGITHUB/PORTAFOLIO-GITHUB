// Speencer Pulido Romero
// Instrucciones de uso:
// El programa pide dos numeros y despliega el resultado d euna suma, tiene un bucle de interfaz para pedir al suuario si queire seguir realizando una operacion o si quiere finalizar programa

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <windows.h>

// ALCANCE DE FUNCIONES DECLARADAS EN STD
using namespace std;

// LLAMADA INCIAL DEL PROGRAMA
int main()
{
    // Declaracion de varibales
    int num1 = 0, num2 = 0, res = 0, op = 0;
    cout << "Calculadora para sumar dos numeros" << endl;
    // Interfaz de operaciones
    do
    {
        cout << "Escribe el primer numero: ";
        cin >> num1;
        cout << "Escribe el segundo numero: ";
        cin >> num2;
        // Operacion para el resultado de una suma de dos numeros
        res = num1 + num2;
        cout << "La suma de los dos numeros es: " << res << endl;
        // Interfaz para realizar mas operaciones o terminar programa
        cout << endl;
        cout << "Quieres realizar otra suma?" << endl;
        cout << "Escribe 1 para realizar otra suma." << endl;
        cout << "Escribe 2 para finalizar programa." << endl;
        cout << "Opcion a elegir: ";
        cin >> op;
        if (op == 2)
        {
            cout << "Finalizando Programa..." << endl;
            break;
        }
        else if (op == 1)
        {
            continue;
        }
        else
        {
            cout << endl;
            cout << "Opcion inconrrecta..." << endl;
            cout << "Porfavor ingresa una opcion de la lista." << endl;
            cout << endl;
        }
    } while (op == 1);
    system("pause");
    return 0;
}