// Librerias
#include <iostream>
using namespace std;

// Programa
main()
{

	// Declaracion de variables
	int op, numCalificaciones, calificacion, suma, promedio;
	double totalPonderacion;
	double calificaciones[numCalificaciones];
	double ponderaciones[numCalificaciones];

	// Interfaz inicial
	cout << "Que operacion quieres hacer.";
	cout << endl;
	cout << "Ponderacion: es seleccionando con numero 1.";
	cout << endl;
	cout << "Promedio: es seleccionando con el numero 2.";
	cout << endl;
	cout << "Finalizar programa: es seleccionando con el numero 3.";
	cout << endl;
	cout << endl;
	cout << "Inserta el numero 1 o 2 para seleccionar una opcion o 3 para finalizar: ";
	cin >> op;
	cout << endl;

	// Switch de opciones
	switch (op)
	{

		// Programa de ponderacion
	case 1:
		cout << "Seleccionaste sacar operacion de ponderacion.";
		cout << endl;
		cout << endl;
		cout << "Ingrese el numero de calificaciones: ";
		cin >> numCalificaciones;
		for (int i = 0; i < numCalificaciones; i++)
		{
			cout << "Ingrese la calificacion " << i + 1 << ": ";
			cin >> calificaciones[i];
			cout << "Ingrese la ponderacion para la calificacion " << i + 1 << ": ";
			cin >> ponderaciones[i];
			totalPonderacion += (calificaciones[i] * ponderaciones[i]) / 100.0;
		}
		if (totalPonderacion == 100.0)
		{
			cout << endl;
			cout << "El balance de ponderacion se cumple detro del 100%." << endl;
			cout << "La ponderacion es de: " << totalPonderacion << "%." << endl;
			break;
		}
		else
		{
			cout << endl;
			cout << "Las ponderaciones son erroneas. El total de ponderacion es " << totalPonderacion << "%." << endl;
			cout << "Debe ser del 100%";
			cout << endl;
			cout << endl;
			break;
		}

		// Programa de promedio
	case 2:
		cout << "Seleccionaste sacar promedio.";
		cout << endl;
		cout << endl;
		cout << "Ingrese el numero de calificaciones a capturar: ";
		cin >> numCalificaciones;
		for (int i = 0; i < numCalificaciones; i++)
		{
			cout << "Ingrese la calificacion " << i + 1 << ": ";
			cin >> calificacion;
			suma += calificacion;
		}
		promedio = suma / numCalificaciones;
		cout << "El promedio es: " << promedio;
		cout << endl;
		cout << endl;
		break;

		// Programa para finalizar programa :)
	case 3:
		cout << "Programa finalizado.";
		cout << endl;
		cout << endl;
		break;

	default:
		cout << "La opcion no corresponde a la lista";
		cout << "El promedio es: " << promedio << endl;
		break;
	}
}