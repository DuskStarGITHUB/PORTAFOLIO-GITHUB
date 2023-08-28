#include <iostream>
using namespace std;
int main()
{

    // Datos
    char Producto_a, Producto_b, Producto_c;
    int Precio_de_Producto_1, Precio_de_Producto_2, Precio_de_Producto_3, sum;

    // Valores
    Producto_a = 0, Producto_b = 0, Producto_c = 0, Precio_de_Producto_1 = 0, Precio_de_Producto_2 = 0, Precio_de_Producto_3 = 0, sum = 0;

    // Interfaz

    // Producto 1
    cout << "\nNombre_del_producto_1:"; // Texto que saltara para introducir dato
    cin >> Producto_a;                  // Dato a la cual va tomar los valores finales
    cout << "\nPrecio del producto:";   // Texto que saltara para introducir dato
    cin >> Producto_a;                  // Dato a la cual va tomar los valores finales

    // Producto 2
    cout << "\nNombre del producto 2:"; // Texto que saltara para introducir dato
    cin >> Producto_b;                  // Dato a la cual va tomar los valores finales
    cout << "\nPrecio del producto:";   // Texto que saltara para introducir dato
    cin >> Producto_b;                  // Dato a la cual va tomar los valores finales

    // Producto 3
    cout << "\nNombre del producto 3:"; // Texto que saltara para introducir dato
    cin >> Producto_c;                  // Dato a la cual va tomar los valores finales
    cout << "\nPrecio del producto:";   // Texto que saltara para introducir dato
    cin >> Producto_c;                  // Dato a la cual va tomar los valores finales

    // Operaciones
    sum = Producto_a + Producto_b + Producto_c; // Podemos sumar,restar,dividir,multiplicar

    // Apartado de resultados

    // Interfaz de nombres
    cout << "\nProducto 1:" << Producto_a;
    cout << "\nProducto 2:" << Producto_b;
    cout << "\nProducto 3:" << Producto_c;

    // Interfaz de total
    cout << "\nTotal:" << sum;
    return 0;
}
