/*
Autor: Speencer Pulido Romero
Fecha: 19/08/2023
Programa: Capturador de Calificaciones
Descripción: Este programa captura nombre y calificaciones, calcula promedio y pemrite volver a modificar alguna calificacion, 
si es el caso recalcula promeid, cada proceso tiene su despliegue de pantalla
*/


// Declaracion de librerias
#include <iostream>
#include <conio.h>
#include <string>

// Mejora de c++
using namespace std;

// Cuerpo de programa
main(){
	//Declaracion de variables
	string nombre;
	int num_calificaciones = 10;
	float calificaciones[num_calificaciones];
	char op;
	float suma=0, promedio=0;
	
	//Despliegue en pantalla
	cout<<"Nombre del alumno: ";
	getline(cin,nombre);
	cout<<endl;
	cout<<"Hola "<<nombre<<endl;
	cout<<endl;
	
	//Captura de calificaicones
	for(int i = 0; i < num_calificaciones; i++){
		cout<<"Calif materia "<<i+1<<": ";
		cin>>calificaciones[i];
		cout<<endl;
	}
	
//	Despliegue de calificaiones en pantalla
	cout<<"Los datos capturados son: "<<endl;
		
	for(int i = 0; i< num_calificaciones; i++){
		cout<<"Calificacion "<<i+1<<": "<<calificaciones[i]<<endl;
	}
	
//	Calculos de promedio
	for(int i =0 ; i < num_calificaciones;i++){
	suma += calificaciones[i]; 
	}
	
	promedio = suma/num_calificaciones;
	cout<<"nPromedio: "<<promedio<<endl;
	
//	Prgeuntar si modificara alguna calificacion
	cout<<"\nDesea modificar alguna calificacion? (s/n): ";
	cin>>op;
	
//	Evaluacion de la respuesta
	if(op == 's' || op == 'S'){
		int indice;
		int nuevoValor;
//		Captura de la nueva calificacion
		cout<<"Ingrese el numero de la calificacion: ";
		cin>>indice;
		indice --;
		cout<<endl;
//		Entrada de calificacion nueva
		if (indice >= 0 && indice <= num_calificaciones) {
			cout<<"Ingrese el nuevo valor: ";
	 		cin>>nuevoValor;
	 		calificaciones[indice] = nuevoValor;
//	 		Despliegue de nuevas calificaciones
	 		cout<<"\nCalificaciones actualizadas: \n";
	 		for(int i = 0; i< num_calificaciones; i++){
			 cout<<"Calificacion "<<i+1<<": "<<calificaciones[i]<<endl;
			}
//			Calcular nuevo promedio
			suma=0;
			for(int i =0 ; i < num_calificaciones;i++){
			suma += calificaciones[i]; 
			}
			promedio = suma/num_calificaciones;
//			Desplegar promedio
			cout<<"Promedio: "<<promedio<<endl;
	 	}
//	 	Manejo de indice erroneo
		else{
		cout<<"Seleccion erronea. La seleccion es del numero 1 a 4"<<endl;
		}
	}
	
	//Fin de programa.
	getch();
	return 0;
}