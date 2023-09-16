// Speencer Pulido Romero DEVELOPER
// Instrucciones de uso del programa:
// El programa pide dos numeros y despliega el resultado d euna suma, tiene un bucle de interfaz para pedir al suuario si queire seguir realizando una operacion o si quiere finalizar programa

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <windows.h>
#include <conio.h>

// ALCANCE DE FUNCIONES DECLARADAS EN STD
using namespace std;

// LLAMADA INCIAL DEL PROGRAMA
int main()
{
    // Declaracion de varibales
    int num1 = 0, num2 = 0, res = 0;
    char op;
    // Interfaz de operaciones
    cout << "Calculadora para sumar dos numeros" << endl;
    do
    {
    	if(op==1){
        cout << "Escribe el primer numero: ";
        cin >> num1;
        cout << "Escribe el segundo numero: ";
        cin >> num2;
        // Operacion para el resultado de una suma de dos numeros
        res = num1 + num2;
        cout << "La suma de los dos numeros es: " << res << endl;
		}
        // Interfaz para realizar mas operaciones o terminar programa
    	else if(op!=1){
        cout << endl;
        cout << "Quieres realizar otra suma?" << endl;
        cout << "Escribe 1 para realizar otra suma." << endl;
        cout << "Escribe 2 para finalizar programa." << endl;
        cout << "Opcion a elegir: ";
		}
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
    } while (op == 1 || op != 1 and op != 2);
    system("pause");
    return 0;
}