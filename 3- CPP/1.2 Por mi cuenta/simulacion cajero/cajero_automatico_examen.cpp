/*
Programa: Simulacion de Cajero Automatico
Autor: Speencer Pulido Romero
Fecha: 29/07/2023
Descripcion del programa: El programa simula una interfaz nasica de un cajero automatico para realizar operaciones bancarias como consultar saldo, hacer depositos 
y retiros; El saldo inicial sera de $2500.00; Despues de realizar algun deposito o retiro por medio de consola se debe mostrar en pantalla la actualizacion del 
saldo, El programa debera reoetir la interfaz hasta que el usuario seleccione la opcion de terminar programa.
*/

//Declaracion de variables
#include <iostream>
#include <conio.h>

// Declaracion de metodo estandar
using namespace std;

//Inicio del cuerpo de programa
int main (){
//Declaracion de variables
int saldo=2500, op, opcion, num_depositos, deposito, depositar=0, num_retiros, retiro, retirar=0;

do{
	//Interfaz Inicial
	cout<<endl;
	cout<<"Cajero Automatico"<<endl;
	cout<<"Quieres realizar alguna operacion?"<<endl;
	cout<<"1- Si"<<endl;
	cout<<"2- No"<<endl;
	cout<<"Teclea un numero del 1 al 2: ";
	cin>>op;
	cout<<endl;
	//Condicionales de la interfaz
	if(op == 1){
		//MENU DEPUS DE LA INTERFAZ INIIAL
		cout<<"|MENU|"<<endl;
		cout<<"1- Consultar Saldo"<<endl;
		cout<<"2- Hacer Depositos"<<endl;
		cout<<"3- Hacer Retiros"<<endl;
		cout<<"4- Salir"<<endl;
		cout<<"Que operacion de la lista deseas realizar?: ";
		cin>>opcion;
		cout<<endl;
		//OPCION 1
		if(opcion == 1){
			cout<<"Tu saldo es de  $"<<saldo<<endl;
			cout<<endl;
		}
		//OPCION 2
		else if(opcion==2){
			cout<<"Cuantos depositos quieres realizar? ";
			cin>>num_depositos;
			cout<<endl;
			for (int i=1; i <= num_depositos; i++){
				cout<<" Ingresa el monto "<<i<<" a depositar: ";
				cin>>deposito;
				depositar = depositar + deposito;
			}
			cout<<"Total a depositar: "<<depositar<<"$"<<endl;
			cout<<"Depositando..."<<endl;
			saldo += depositar;
			cout<<"Listo."<<endl;
			cout<<"Tu nuevo saldo es de $"<<saldo<<endl;
			cout<<endl;
		}
		//OPCION 3
		else if (opcion == 3){
			cout<<"Cuantos retiros quieres realizar? ";
			cin>>num_retiros;
			cout<<endl;
			for (int i=1; i <= num_retiros; i++){
				cout<<"Ingresa el monto "<<i<<" a retirar: ";
				cin>>retiro;
				retirar = retirar + retiro;
			}
			cout<<"Total a retirar: "<<retirar<<"$"<<endl;
			cout<<"Retirando..."<<endl;
			if(retirar > saldo){
				cout<<"Saldo Insuficiente"<<endl;
				cout<<endl;
				continue;
			}
			else{
			saldo -= retirar;
			cout<<"Listo."<<endl;
			cout<<"Tu nuevo saldo es de $"<<saldo<<endl;
			cout<<endl;
			}
		}
		//OPCION 4
		else if (opcion== 4){
			cout<<"Saliendo..."<<endl;
			cout<<endl;
			continue;
		}
		else{
			cout<<"Opcion incorrecta";
			cout<<endl;
		}
		continue;}
	else if(op==2){
		cout<<endl;
		cout<<"Okay, Terminando programa..."<<endl;
		cout<<endl;
		break;
	}
	else if (op != 2 and op!=1){
	cout<<"Caracter no valido, Escribe el numero que corrsponda a la lista."<<endl;
	cout<<endl;
	continue;
	}
	}while(op!=2);
	
	//Fin de programa
	return 0;
}