// Librerias
#include <iostream>
// Cuerpo
using namespace std;
int main()
{
	// Datos
	int i, p, f;
	i = 0, p = 0, f = 0;
	// Interfaz inicial

	cout << "Contador de numeros de desincremento." << endl;
	cout << "" << endl;
	cout << "" << endl;
	cout << "Inserta el valor incia para tu contador: ";
	cin >> i;
	cout << "" << endl;
	cout << "Inserta el valor de salto entre cada numero: ";
	cin >> p;
	cout << "" << endl;
	cout << "" << endl;
	cout << "Tus valores son--> " << f << " Hasta " << i << " Cada: " << p << "." << endl;
	cout << "" << endl;
	cout << "--------------------INICIO--------------------" << endl;

	// Ciclo
	for (int i = i; i > 0; i--)
	{
		cout << "|-" << i << endl;
	}
	cout << "--------------------FIN--------------------" << endl;
	return 0;
}
