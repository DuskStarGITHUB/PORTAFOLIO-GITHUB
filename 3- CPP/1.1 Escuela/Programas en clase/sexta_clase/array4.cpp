/* Autor: Speencer Pulido Romero
Fecha: 05/08/2023
Descripcion: Este programa despliega en pantalla un ticket de compra de 12 articulos comprados */


//Declaracion d elibrerias
#include <iostream>

//Metodo de captura estandar
using namespace std;

//Declaracion de una variable constante
const int CantidadArticulos = 13;
//Cuerpo de programa
int main(){
//Declaracion de Arreglo de precios
int ArrayCostes[CantidadArticulos]={0};

//Despliegue en pantalal de indicaciones
cout<<"Porfavor capture el costo de los articulos para generar un ticket: "<<endl;
cout<<endl;

//Ciclo para capturar  costos
for(int i=1; i<CantidadArticulos;i++){
	//Despliegue en cada ciclo + captura de elementos
	cout<<"Capture el costo del articulo "<<i<<": ";
	cin>>ArrayCostes[i];
	cout<<endl;
}

//Despliegue en pantalla
cout<<"Ticket de compra"<<endl;
cout<<endl;
//Ciclo Para desplegar en pantalla cada elemento de los arrays acompañado de texto para generar en si el ticket
for(int i=1; i<CantidadArticulos;i++){
	//Despliegue en cada ciclo
	cout<<"El articulo "<<i<<" Costo: "<<ArrayCostes[i]<<"$"<<endl;
}
	//Fin de programa
	return 0;
}