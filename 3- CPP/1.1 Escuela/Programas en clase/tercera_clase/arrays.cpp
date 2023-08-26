/*Desarrollador por Speencer Pulido Romero
Instrucciones de uso:

*/

// Declaracion de librerias
#include <iostream>
#include <windows.h>

// ALCANCE DE FUNCIONES DECLARADAS EN STD
using namespace std;

// LLAMADA INCIAL DEL PROGRAMA
main(){
//	Declaracion de arrays
	int numeros[] = {1,2,3,4,5};
	int tamano = sizeof(numeros) / sizeof(numeros[0]);
	
	for(int i=0; i<tamano; i++){
		cout<<numeros[i]<<endl;
	}
	
	system("pause");
	return 0;
}