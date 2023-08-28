#include <iostream>
using namespace std;

int main()
{

    float L, H, B, pi, A, r, D, r2;
    int n;

    L = 0, H = 0, B = 0, pi = 3.14, A = 0, r = 0, D = 0, r2 = 0, n = 0;

    cout << "Lista de figuras del 1 a 4 para sacar su area de dichas figura" << endl;
    cout << "Selecciona un numero que corresponde a la figura:" << endl;
    cout << endl;
    cout << "1-Cuadrado" << endl;
    cout << "2-Triangulo" << endl;
    cout << "3-Circulo" << endl;
    cout << "4-Rectangulo" << endl;
    cout << endl;
    cout << "Selecciona la opcion a elegir: ";
    cin >> n;
    cout << endl;

    switch (n)
    {
    case 1:
        cout << "Seleccionaste sacar el area de un cuadrado" << endl;
        cout << "Inserta el valor del lado  (L): ";
        cin >> L;
        A = L * L;
        cout << "\nEl area del cuadrado: " << A;
        break;
    case 2:
        cout << "Seleccionaste sacar el area de un Triangulo" << endl;
        cout << "Inserta el valor de la base (B): ";
        cin >> B;
        cout << "Inserta el valor de la altura (H): ";
        cin >> H;
        A = B * H / 2;
        cout << "El area del triangulo es: " << A;
        break;
    case 3:
        cout << "Seleccionaste sacar el area de un circulo" << endl;
        cout << "Inserta el valor del radio(r): ";
        cin >> r;
        r2 = r * r;
        A = pi * r2;
        cout << "El area del circulo es: " << A;
        break;
    case 4:
        cout << " Seleccionaste sacar el area de un Rectangulo" << endl;
        cout << "Inserta el valor de la altura (H): ";
        cin >> H;
        cout << "Inserta el valor de la base (B): ";
        cin >> B;
        A = H * B;
        cout << "El area del rectangulo es: " << A;
        break;

    default:
        cout << "No tecleaste una opcion incluida" << endl;
        cout << "Porfavor usa un numero del 1 al 4 para elegir una figura" << endl;
        cout << "Revisa la lista anterior" << endl;
        break;
    }
    return 0;
}
