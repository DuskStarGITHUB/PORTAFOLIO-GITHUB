/* Autor: Speencer Pulido Romero
Fecha: 05/08/2023
Descripcion: Este programa pide capturar costos de 5 articulos despliega en pantalla un ticket de compra de esos articulos y el total tras sumar los articulos */


//Declaracion de librerias
#include <iostream>

//Metodo de captura estandar
using namespace std;

//Declaracion de una variable constante
const int CantidadArticulos = 6;
//Cuerpo de programa
int main(){
//Declaracion de Arreglo de precios
int ArrayCostes[CantidadArticulos]={0};

//Despliegue en pantalal de indicaciones
cout<<endl;

//Ciclo para capturar  costos
for(int i=1; i<CantidadArticulos;i++){
	//Despliegue en cada ciclo + captura de elementos
	cout<<"Capture el costo del articulo "<<i<<": ";
	cin>>ArrayCostes[i];
	cout<<endl;
}
//Despliegue en pantalla
cout<<endl;
cout<<"Ticket de compra"<<endl;
cout<<endl;
//Ciclo Para desplegar en pantalla cada elemento de los arrays acompañado de texto para generar en si el ticket
for(int i=1; i<CantidadArticulos;i++){
	//Despliegue en cada ciclo
	cout<<"El articulo "<<i<<" $"<<ArrayCostes[i]<<".00"<<endl;
}

//Declaracion de variables
int suma=0,total=0;
//Suma de los elementos de arreglo para scaar el total
for(int i =0 ; i < CantidadArticulos;i++){
	suma += ArrayCostes[i];
}

total= suma;
//Despliegue en pantalla de total
cout<<endl;
cout<<"El total de tu compra es: $"<<total<<".00"<<endl;
	//Fin de programa
	return 0;
}