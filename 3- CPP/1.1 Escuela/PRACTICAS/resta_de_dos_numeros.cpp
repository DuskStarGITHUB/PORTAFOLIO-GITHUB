// Speencer Pulido Romero
// Instrucciones de uso:
// Este programa pide dos numeros a un usuario y los resta despues imprime el resultado, de igual manera no terminara hasta que el usuario indique.

// DECLARACION DE LIBRERIAS
#include <iostream>
#include <windows.h>

// ALCANCE DE FUNCIONES DECLARADAS EN STD
using namespace std;

// LLAMADA INCIAL DEL PROGRAMA
int main()
{
    // Declaracion de varibales
    int num1 = 0, num2 = 0;
	char op;
	float res = 0;
    cout << "Calculadora para restar dos numeros" << endl;
    // Interfaz de operaciones
    do
    {
        cout << "Escribe el primer numero: ";
        cin >> num1;
        cout << "Escribe el segundo numero: ";
        cin >> num2;
        // Operacion para el resultado de una resta de dos numeros
        if(num1 <=0 and num2<=0){
        	res= num1 + num2;
		}
		else{
        res = num1 - num2;	
		}
        cout << "El resultado de restas ambos numeros es:  "<< res << endl;
        system("pause");
        
        // Interfaz para realizar mas operaciones o terminar programa
        cout << endl;
        cout << "Quieres realizar otra resta?" << endl;
        cout << "Escribe 1 para realizar otra resta." << endl;
        cout << "Escribe 2 para finalizar programa." << endl;
        cout << "Opcion a elegir: ";
        cin >> op;
        cout<<endl;
        if (op == 2)
        {
            cout << "Finalizando Programa..." << endl;
            break;
        }
        else if (op == 1)
        {
            continue;
        }
        while(op !=1)
        {
            cout << endl;
            cout << "Opcion inconrrecta..." << endl;
            cout << "Porfavor ingresa una opcion de la lista anterior." << endl;
            cout << endl;
            cout<<"Opcion a elegir: ";
            cin>>op;
            if (op==2){
            	cout<<"Finalizando programa..."<<endl;
            	break;
			}
			else{
				cout << endl;
            	cout << "Opcion inconrrecta..." << endl;
            	cout << "Porfavor ingresa una opcion de la lista anterior." << endl;
            	cout << endl;
            	cout<<"Opcion a elegir: ";
            	cin>>op;
			}
			cout << endl;
        }
    } while (op == 1);
    system("pause");
    return 0;
}