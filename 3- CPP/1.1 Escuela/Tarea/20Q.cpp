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
    // Variables
    string menu;
    // Despliegue de menu
    do
    {
        cout << "\t\t\t\tBienvenido a 20Q" << endl;
        cout << "\nElija una opcion mentalmente d ela siguiente lista y intentare adivinar a traves de una serie de maximo 20 preguntas que opcion has elegido.\n"
             << endl;
        cout << "\n\tFrutas:\n\tTecojote\tMango\t\tCoco" << endl;
        cout << "\n\tAnimales:\n\tPajaro\t\tCanguro\t\tLeon" << endl;
        cout << "\n\tObjetos:\n\tCanica\t\tEscoba\t\tCubeta\n\n"
             << endl;
        // Pregunta para repetir o finalizar juego juego
        cout << "¿Quieres jugar de nuevo? (S/N): ";
        cin >> menu;
        // Validacion de respuesta del usuario
        if (menu == "S" or menu == "s")
        {
            cout << "¡Okay hagamoslo de nuevo!" << endl;
        }
        else if (menu == "N" or menu == "n")
        {
            continue;
        }
        else
        {
            do
            {
                cout << "Opcion no valida" << endl;
                cout << "¿Quieres jugar de nuevo? (S/N): ";
                cin >> menu;
            } while (menu != "S" and menu != "s" and menu != "N" and menu != "n");
        }
    } while (menu != "N" and menu != "n");
    // Mensaje de finalizacion del juego
    cout << "Gracias por jugar" << endl;
    // Fin del Programa
    return 0;
}