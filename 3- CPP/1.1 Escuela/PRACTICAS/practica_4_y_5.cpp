//SPEENCER PULIDO ROMERO
// ESTE PROGRAMA ES PARA VER COMO ACTUAN LAS DOS FUNCIONES DE WHLE Y DO WHILE

// DECLARACION DE LIBRERIA
#include <iostream>

// RANGO DE STD 
using namespace std;

// CUERPO DE PROGRAMA
main(){
	
	//DECLARACION DE VARIABLE
	int i=0;
	
//	PROGRAMA DE LA FUNCION DO WHILE
	do{
		cout<< i <<" ";
		i++;
	}while (i<=5);
	
	cout<<endl;
	cout<<endl;
	
// CAMBIO DE VALOR PARA INICIAR EL WHILE DESDE CERO
	i=0;
	
//	PROGRAMA DE LA FUNCION WHILE
	while(i<=5){
		cout<<i<<" ";
		i++;
	}
}