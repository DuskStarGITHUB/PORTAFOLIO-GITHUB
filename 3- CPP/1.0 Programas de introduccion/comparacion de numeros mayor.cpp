#include <iostream>
using namespace std;

main()
{

	// Datos

	int n1, n2;

	// Valores

	n1 = 0, n2 = 0;

	cout << "Introduce el primer valor:"; // Texto que saltara para introducir dato
	cin >> n1;

	cout << "Introduce el segundo valor:"; // Texto que saltara para introducir dato
	cin >> n2;

	// Operacion de comparacion

	if (n1 > n2)
	{
		cout << "El primer valor es mayor " << n1; // Texto que saltara para introducir dato
		cin >> n1 >> n2;
	}

	else
	{
		cout << "El segundo valor es mayor " << n2; // Texto que saltara para introducir dato
		cin >> n1 >> n2;
	}

	return 0;
}
