#include <iostream>
using namespace std;

main(){
	
int x,h,b,pi,r,n,area;

x=0,h=0,pi=0,r=0,n=0,area=0;
cout<<"Opciones que puedes elegir"<<endl;
cout<<"Selecciona una opcion que equivale a su figura para proceder a calcular su area;"<<endl;
cout<<"1=Cuadrado"<<endl;
cout<<"2=Triangulo"<<endl;
cout<<"3=Circulo"<<endl;
cout<<"4=Rectangulo"<<endl;
cout<<""<<endl;
cout<<"Teclea la opcion:";
cin>>n;

switch(n){
	case 1:
	cout<<"Sacaras el area del cuadrado"; //Texto que saltara para el caso
	cout<<"Inserta el valor del lado"<<endl;
    cin>>x;
    area=x*x
    
    cout>>"El area del cuadrado es:"<<area;
	break;
	
	case 2:
	cout<<"Sacaras el area del Triangulo"; //Texto que saltara para el caso
	break;
	
	case 3:
	cout<<"Sacaras el area del Circulo"; //Texto que saltara para el caso
	break;
	
	case 4:
	cout<<"Sacaras el area del Rectangulo"; //Texto que saltara para el caso
	break;
	
	default:
		cout<<"No seleccionaste una opcion incluida";
		break;
}
 return 0;
}
