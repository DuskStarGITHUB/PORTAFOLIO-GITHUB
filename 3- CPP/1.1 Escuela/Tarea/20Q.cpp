/*
Nombre de archivo: Adivinador
Autor: Speencer Pulido Romero
Descripcion: Este programa muestra un menu de opciones en el cual involucra 3 frutas, 3 animales y 3 cosas e indica que el usuario debe elegir uno en su mente, al inciar el programa se despliega en pantalla una serie de preguntas para intentar adivinar la opcion elegida por el usuario, eto parecido al juego tan conocido como 20Q.
*/

// Importacion de Librerias
#include <iostream>
// Mejora STD
using namespace std;

// Funcion principal
int main()
{
    // Variables
    string menu, respuesta;
    int error = 1;
    // Despliegue de menu
    do
    {
        cout << "\t\t\t\tBienvenido a 20Q" << endl;
        cout << "\nSelecciona una opcion mentalmente de la siguiente lista y intentare adivinar a traves de una serie de preguntas que opcion has elegido.\n"
             << endl;
        cout << "\n\tFrutas:\n\tTecojote\tMango\t\tCoco" << endl;
        cout << "\n\tAnimales:\n\tPajaro\t\tCanguro\t\tLeon" << endl;
        cout << "\n\tObjetos:\n\tCanica\t\tEscoba\t\tCubeta\n\n"
             << endl;
        // Preguntas para adivinar opcion
        do
        {
            // Primera Pregunta
            cout << "¿Es una fruta? (S/N): ";
            cin >> respuesta;
            cout << endl;
            if (respuesta == "S" or respuesta == "s")
            {
                error = 1;
                // Segunda Pregunta
                do
                {
                    cout << "¿Puede ser de color amarillo? (S/N): ";
                    cin >> respuesta;
                    cout << endl;
                    if (respuesta == "S" or respuesta == "s")
                    {
                        error = 1;
                        // Tercera Pregunta
                        do
                        {
                            cout << "¿Su cascara se come? (S/N): ";
                            cin >> respuesta;
                            if (respuesta == "S" or respuesta == "s")
                            {
                                error = 1;
                                cout << "\n¡Es un tecojote!" << endl;
                            }
                            else if (respuesta == "N" or respuesta == "n")
                            {
                                error = 1;
                                cout << "\n¡Es un mango!" << endl;
                            }
                            // Manejo de error
                            else
                            {
                                error = 2;
                                cout << "\nRespuesta no valida, porfavor responde con 'S' para si o 'N' para no.\n"
                                     << endl;
                            }
                        } while (error == 2);
                    }
                    else if (respuesta == "N" or respuesta == "n")
                    {
                        error = 1;
                        cout << "\n¡Es un coco!" << endl;
                    }
                    // Manejo de error
                    else
                    {
                        cout << "\nRespuesta no valida, porfavor responde con 'S' para si o 'N' para no.\n"
                             << endl;
                        error = 2;
                    }
                } while (error == 2);
            }
            else if (respuesta == "N" or respuesta == "n")
            {
                error = 1;
                // Segunda Pregunta
                do
                {
                    cout << "¿Es un animal? (S/N): ";
                    cin >> respuesta;
                    cout << endl;
                    if (respuesta == "S" or respuesta == "s")
                    {
                        error = 1;
                        // Tercera Pregunta
                        do
                        {
                            cout << "¿Tiene pelaje? (S/N): ";
                            cin >> respuesta;
                            cout << endl;
                            if (respuesta == "S" or respuesta == "s")
                            {
                                error = 1;
                                // Cuarta Pregunta
                                do
                                {
                                    cout << "¿Es herviboro? (S/N): ";
                                    cin >> respuesta;
                                    cout << endl;
                                    if (respuesta == "S" or respuesta == "s")
                                    {
                                        error = 1;
                                        cout << "\n¡Es un canguro!" << endl;
                                    }
                                    else if (respuesta == "N" or respuesta == "n")
                                    {
                                        error = 1;
                                        cout << "\n¡Es un leon!" << endl;
                                    }
                                    // Manejo de error
                                    else
                                    {
                                        cout << "Respuesta no valida, porfavor responde con 'S' para si o 'N' para no" << endl;
                                        error = 2;
                                    }
                                } while (error == 2);
                            }
                            else if (respuesta == "N" or respuesta == "n")
                            {
                                error == 1;
                                cout << "\n¡Es un pajaro!" << endl;
                            }
                            // Manejo de error
                            else
                            {
                                cout << "Respuesta no valida, porfavor responde con 'S' para si o 'N' para no" << endl;
                                error = 2;
                            }
                        } while (error == 2);
                    }
                    else if (respuesta == "N" or respuesta == "n")
                    {
                        error = 1;
                        // Tercera Pregunta
                        do
                        {
                            cout << "¿Puede ser de plastico? (S/N): ";
                            cin >> respuesta;
                            cout << endl;
                            if (respuesta == "S" or respuesta == "s")
                            {
                                error = 1;
                                // Cuarta Pregunta
                                do
                                {
                                    cout << "¿Puede retener liquido? (S/N): ";
                                    cin >> respuesta;
                                    cout << endl;
                                    if (respuesta == "S" or respuesta == "s")
                                    {
                                        error = 1;
                                        cout << "\n¡Es un cubeta!" << endl;
                                    }
                                    else if (respuesta == "N" or respuesta == "n")
                                    {
                                        error = 1;
                                        cout << "\n¡Es un escoba!" << endl;
                                    }
                                    // Manejo de error
                                    else
                                    {
                                        cout << "Respuesta no valida, porfavor responde con 'S' para si o 'N' para no" << endl;
                                        error = 2;
                                    }
                                } while (error == 2);
                            }
                            else if (respuesta == "N" or respuesta == "n")
                            {
                                error = 1;
                                cout << "\n¡Es un canica!" << endl;
                            }
                            // Manejo de error
                            else
                            {
                                cout << "Respuesta no valida, porfavor responde con 'S' para si o 'N' para no" << endl;
                                error = 2;
                            }
                        } while (error == 2);
                    }
                    // Manejo de error
                    else
                    {
                        cout << "Respuesta no valida, porfavor responde con 'S' para si o 'N' para no" << endl;
                        error = 2;
                    }
                } while (error == 2);
            }
            // Manejo de error
            else
            {
                cout << "\nRespuesta no valida, porfavor responde con 'S' para si o 'N' para no\n"
                     << endl;
                error = 2;
            }
        } while (error == 2);
        // Pregunta para repetir o finalizar juego juego
        cout << "\n\n¿Quieres jugar de nuevo? (S/N): ";
        cin >> menu;
        // Validacion de respuesta del usuario
        if (menu == "S" or menu == "s")
        {
            cout << "\n¡Okay hagamoslo de nuevo!" << endl;
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
                cout << "\n\n¿Quieres jugar de nuevo? (S/N): ";
                cin >> menu;
            } while (menu != "S" and menu != "s" and menu != "N" and menu != "n");
        }
    } while (menu != "N" and menu != "n");
    // Mensaje de finalizacion del juego
    cout << "\nGracias por jugar..." << endl;
    // Fin del Programa
    return 0;
}