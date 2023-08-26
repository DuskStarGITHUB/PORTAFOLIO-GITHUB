/*Desarrollado por Speencer Pulido Romero
Instrucciones de uso:
Se solicitan al usuario dos numeros enteros para multiplicar uno es el limite y otro el numero base, esto con un contador for se hara una iteracion para hacer una tabla de multiplicar.
22/07/2023
*/

// Declaracion de librerias
#include <iostream>
#include <windows.h>

// ALCANCE DE FUNCIONES DECLARADAS EN STD
using namespace std;

// LLAMADA INCIAL DEL PROGRAMA
main(){
//	Declaracion de Variables
	int lim=0, num=0, res=0;
//	Interfaz inicial
	cout<<"Tabla de Multiplicar"<<endl;
	cout<<endl;
	cout<<"Porfavor para realizar su tabla de multiplicar proporciona 2 numeros enteros."<<endl;
	cout<<endl;
	cout<<"Teclea el primer numero a multiplicar o numero base: ";
	cin>>num;
	cout<<"Teclea el segundo numero del limite de la tabla de multiplicar: ";
	cin>>lim;
	cout<<endl;
	
//	Texto de la tabla
	cout<<"La tabla de multiplicar del "<<num<<" es:"<<endl;
	cout<<endl;
	
//	Operaciones para realizar la tabla de multiplicar.
	for(int i=1; i<=lim; i++){
		res = num * i;
//		Despliegue en pantalla de la tabla generada
		cout<<num<<" x "<< i<<"= "<<res<<endl;
	}
	
	
	
//	FIN
	cout<<endl;
	cout<<"FIN"<<endl;
	system("pause");
	return 0;
}