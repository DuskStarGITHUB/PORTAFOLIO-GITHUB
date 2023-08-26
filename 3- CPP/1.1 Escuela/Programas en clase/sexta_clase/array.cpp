/* Autor: Speencer Pulido Romero
Fecha: 05/08/2023
Descripcion: El programa define un tamaño de array a traves de una variable constante y a este mismo array se le asigna multiples elementos, se utiliza un for para
desplegar en consola cada elemento del array */
#include <iostream>

using namespace std;
const int tamano = 5;
int main(){
	int DefArray[tamano] = {10, 20, 30, 40, 50};

cout<<"Índice\tContenido\n";

for (int i = 0; i < tamano; i++) {
    cout<<i<<"\t"<<DefArray[i]<<endl;
}

return 0;
}