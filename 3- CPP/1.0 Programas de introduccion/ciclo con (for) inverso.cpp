/*Los ciclos for son lo que se conoce como estructuras de control de flujo c�clicas o simplemente estructuras c�clicas,
estos ciclos, como su nombre lo sugiere, nos permiten ejecutar una o varias l�neas de c�digo de forma iterativa,
conociendo un valor especifico inicial y otro valor final, adem�s nos permiten determinar el tama�o del paso entre cada "giro" o iteraci�n del ciclo.
En resumen, un ciclo for es una estructura de control iterativa, que nos permite ejecutar de manera repetitiva un bloque de instrucciones,
conociendo previamente un valor de inicio, un tama�o de paso y un valor final para el ciclo*/

#include <iostream>

using namespace std;
int main()
{
	// Ciclo inverso
	for (int i = 10; i > 0; i--)
	{
		cout << i << endl;
	}
	return 0;
}
