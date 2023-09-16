// Librerias
#include <iostream>
using namespace std;

// Inicio del cuerpo
int main()
{
   // Datos
   int c, v, d;
   double suma, valor;
   c = 0, v = 0, suma = 0.0, valor = 0, d = 0;

   // Interfaz inicial
   cout << "Contador v2" << endl;
   cout << "Este contador sumara la cantidad de numeros que quieras" << endl;
   cout << "" << endl;
   cout << "Introduzca cuantos valores quiere sumar: ";
   cin >> v;

   // Contador while v2
   while (v > c)
   {

      cout << "Inserta el numero a sumar: ";
      cin >> valor;
      cout << "" << endl;
      suma = suma + valor; // Equivalente a suma = suma + valor
      c = d + 1;           // Equivalente a contador = contador + 1
   }

   if (c > 0)
   {
      cout << "La suma de los " << v << " valores introducidos es: " << suma << endl;
   }

   else
   {
      cout << "La cantida de valores a sumar tiene que ser igual o mayor a 2";
   }

   return 0;
}
