#include <iostream>
#include <conio.h>

using namespace std;

const int numPersonas=3;
int main(){
	string nombre[numPersonas];
	int edades[numPersonas];
	string ciudades[numPersonas];
	
	cout<<"Ingrese datos de "<<numPersonas<<"perosnas:\n";
	for (int i=0; i<numPersonas;i++){
		cout<<"\nPersona"<<i+1<<":/n";
		
		cout<<"Nombre";
		cin.ignore();
		getline(cin,nombre[i]);
		
		cout<<"Edad: ";
		cin>>edades[i];
		
		cout<<"Ciudad: ";
		cin.ignore();
		getline(cin,ciudades[i]);
	}
	return 0;
}