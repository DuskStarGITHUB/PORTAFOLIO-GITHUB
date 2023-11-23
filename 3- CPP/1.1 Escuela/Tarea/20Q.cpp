/*
Nombre de archivo: 20Q
Autor: Speencer Pulido Romero
Descripcion: Este programa muestra un menu de opciones en el cual involucra 3 frutas, 3 animales y 3 cosas e indica que el usuario debe elegir uno en su mente, al inciar el programa se despliega en pantalla una serie de preguntas para intentar adivinar la opcion elegida por el usuario.
*/

// Importacion de Librerias
#include <iostream>
// Mejora STD
using namespace std;

// Funcion principal
int main()
{
    // Despliegue de menu
    cout << "\t\t\tBienvenido a 20Q" << endl;
    cout << "\nElija una opcion mentalmente y intentare adivinarlo:\n"<< endl;
    cout << "\n\tFrutas:\n\tTecojote\tMango\tCoco" << endl;
    cout << "\n\tAnimales:\n\tPajaro\tCanguro\tLeon" << endl;
    cout << "\n\tObjetos:\n\tCanica\tEscoba\tCubeta\n\n" << endl;
    return 0;
}