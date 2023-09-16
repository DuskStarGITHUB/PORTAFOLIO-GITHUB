#include <iostream>
using namespace std;

main()
{

	// Valores
	int n1, n2;

	n1 = 0, n2 = 0;

	cout << "Introduce el primer valor:"; // Texto que saltara para introducir dato
	cin >> n1;

	cout << "Introduce el segundo valor:"; // Texto que saltara para introducir dato
	cin >> n2;
	cout << "" << endl;
	// Operacion de comparacion
	if (n1 == n2)
	{
		cout << "Los valores son iguales";
	}

	else
	{
		cout << "El segundo valor es mayor " << n2; // Texto que saltara para introducir dato
	}
	return 0;
}
