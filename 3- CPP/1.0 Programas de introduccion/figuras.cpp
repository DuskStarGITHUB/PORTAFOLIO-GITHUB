// Sintaxis
#include <iostream>
using namespace std;

// Inicio del menu
int main()
{

    // Tipo de datos y Datos
    float x, h, b, pi, a, r, d, r2;
    int n;
    // Valores de los datos
    x = 0, h = 0, b = 0, pi = 3.14, a = 0, r = 0, d = 0, r2 = 0, n = 0;

    // Interfaz inicial
    cout << "Lista de figuras del 1 a 4 para sacar el area de una figura" << endl; // endl sirve para terminar la linea y hacer un salto a la siguiente
    cout << "Porfavor selecciona un numero que corresponde a su figura:" << endl;
    cout << endl;
    cout << "1-Cuadrado" << endl;
    cout << "2-Triangulo" << endl;
    cout << "3-Circulo" << endl;
    cout << "4-Rectangulo" << endl;
    cout << endl;
    cout << "Teclea la opcion a elegir: ";
    cin >> n;
    cout << endl;
    // Incio del switch
    switch (n)
    {

        //--------------------------------------------------------------------------------------------------------------------------------------------------------
        // Casos
    case 1:
        // Interfaz
        cout << "Seleccionaste sacar el area de un cuadrado" << endl; // Texto que saltara para el caso seleccionado
        cout << "Inserta el valor del lado o llamado (x): ";
        cin >> x;
        // Operacion/es
        a = x * x;
        // Interfaz final
        cout << "\nEl area del cuadrado: " << a;
        break;

    //------------------------------------------------------------------------------------------------------------------------------------------------------
    case 2:
        cout << "Seleccionaste sacar el area de un Triangulo" << endl; // Texto que saltara para el caso
        cout << "Inserta el valor de la base (b): ";
        cin >> b;
        cout << "Inserta el valor de la altura (a): ";
        cin >> a;
        // Operacion/es
        a = b * a / 2;
        // Interfaz final
        cout << "El area del triangulo es: " << a;
        break;
        //------------------------------------------------------------------------------------------------------------------------------------------------------
    case 3:
        cout << "Seleccionaste sacar el area de un circulo" << endl; // Texto que saltara para el caso
        cout << "Inserta el valor del diametro (d): ";
        cin >> d;
        // Operacion/es
        r = d / 2;
        r2 = r * r;
        a = pi * r2;
        // Interfaz final
        cout << "El area del circulo es: " << a;
        break;
        //------------------------------------------------------------------------------------------------------------------------------------------------------
    case 4:
        cout << " Seleccionaste sacar el area de un Rectangulo" << endl; // Texto que saltara para el caso
        cout << "Inserta el valor de la altura (h): ";
        cin >> h;
        cout << "Inserta el valor de la base (b): ";
        cin >> b;
        // Operacion/es
        a = h * b;
        // Interfaz final
        cout << "El area del rectangulo es: " << a;
        break;

        //------------------------------------------------------------------------------------------------------------------------------------------------------
        // Default para excluir errores
    default:
        cout << "No seleccionaste una opcion incluida" << endl;
        cout << "Porfavor usa un numero del 1 al 4 para elegir una figura" << endl;
        cout << "Revisa la lista anterior" << endl;
        break;
    }
    return 0;
}
