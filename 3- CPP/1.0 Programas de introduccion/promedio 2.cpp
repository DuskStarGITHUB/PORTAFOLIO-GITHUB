// Librerias
#include <iostream>
using namespace std;

// Inicio del main
int main()
{

	// Tipos de datos y datos
	float a, b, c, d, f1, f2, f3;

	a = 0, b = 0, c = 0, d = 0, f1 = 10, f2 = 7, f3 = 5;

	// Textos principales
	cout << "Captura de calificaciones" << endl;
	cout << "Este programa sacara el promedio" << endl;
	cout << "" << endl;
	cout << "Capture la primera calificacion: ";
	cin >> a;
	cout << "Capture la segunda calificacion: ";
	cin >> b;
	cout << "Capture la tercera calificacion: ";
	cin >> c;
	cout << "" << endl;
	// Proceso
	d = a + b + c / 3;

	if (d >= f3)
	{
		cout << "El promedio es: " << d;
		cout << " Exelente sigue asi";
	}
	else
	{
		cout << "El promedio es: " << d << " Exelente sigue asi";
		cin >> d >> f2;
	}

	return 0;
}
