/* Autor: Speencer Pulido Romero
Fecha: 05/08/2023
Descripcion: El programa define un tamaño de array a traves de una variable constante y a este mismo array se le asigna multiples elementos,se utiliza un for
para capturar por consola cada elemento, se utiliza otro for para desplegar en consola cada elemento del array capturado */

//Declaracion d elibrerias
#include <iostream>

//Metodo de captura estandar
using namespace std;

//Declaracion de variable constante
const int tamano = 8;

//Cuerpo de programa
int main(){
	//Declaracion de array tipo entero con el tamaño d ela varaible tamaño
	int CapturaArray[tamano];
	
	//Despliegue en pantalla de texto indicando cuantos numeros se deben capturar
	cout<<"Ingrese "<<tamano<<" numeros enteros:\n";
	
	//Ciclo para registrar elementos del array a traves de consola
	for(int i=0;i<tamano;i++){
		//Captura de elementos despues de un depsliegue de el texto
		cout<<"Ingrese el valor para el indice "<<i<<": ";
		cin>>CapturaArray[i];
	}
	
	//Despliegue en pantalla de un texto
	cout<<"\nIndice\tContenido\n";
	//Ciclo for para desplegar en pantalla cada elemento registrado anterior elemento de el array
	for (int i = 0; i < tamano; i++) {
		//Despliegue en pantalla de cada indice y elemento del array
    	cout<<i<<"\t"<<CapturaArray[i]<<endl;
		}

return 0;
}