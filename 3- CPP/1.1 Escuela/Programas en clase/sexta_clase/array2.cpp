/* Autor: Speencer Pulido Romero
Fecha: 05/08/2023
Descripcion: El programa define un tamaño de array a traves de una variable constante y a este mismo array se le asigna multiples elementos, se utiliza un for para
desplegar en consola cada elemento del array tras modificar los elementos de manera manual */

//Declaracion de variables
#include <iostream>

//Metodo estandar
using namespace std;
//Variable constante para el tamaño del array
const int tamano = 5;

//Cuerpo de programa
int main(){
	//Declaracion de el array y sus elementos
	int DefArray[tamano] = {1, 2, 3, 4, 5};

//Despliegue en consola de un texto con una tabulacion y salto de linea
cout<<"Índice\tContenido\n";

//Contador for donde se despliega cada indice y elemnto dek array
for (int i = 0; i < tamano; i++) {
    cout<<i<<"\t"<<DefArray[i]<<endl;
}

//Fin de programa
return 0;
}