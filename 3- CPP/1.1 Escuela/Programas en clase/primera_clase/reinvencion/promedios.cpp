// DECLARACION DE LIBRERIAS
#include <iostream>
#include <windows.h>
// ALCANCE DE FUNCIONES DECLARADAS EN STD
using namespace std;

// LLAMADA INCIAL DEL PROGRAMA
main()
{
    // variables
    int opciones = 0, numCalificaciones = 0, calificacion = 0, suma = 0, promedio = 0;
    // Interfaz Inicial
    while (opciones != 3)
    {
        cout << "1- "
             << "Promedio Simple" << endl;
        cout << "2- "
             << "Promedio Ponderado" << endl;
        cout << "3- "
             << "Salir" << endl;
        cout << "Inserta la opcion a elegir: ";
        cin >> opciones;
        cout << endl;
        if (opciones == 1 || opciones == 2)
        {

            // Swicth
            switch (opciones)
            {
                // PROMEDIO GENERAL
            case 1:
                cout << "ELEGISTE SACAR PROMEDIO SIMPLE" << endl;
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
                system("pause");
                break;
                // OPCION 2
            case 2:
                cout << "ELEGISTE CALCULAR PROMEDIO PONDERADO" << endl;
                // PROGRAMA PONDERADO
                double Suma = 0, suma_ponderaciones = 0, promedio_ponderado;
                int X;
                cout << "Ingrese el numero de examenes o asignaturas: ";
                cin >> X;

                for (int i = 1; i <= X; ++i)
                {
                    double valor;
                    double ponderacion;
                    cout << "Ingrese la calificacion del examen o asignatura " << i << ": ";
                    cin >> valor;

                    if (valor > 10)
                    {
                        cout << "La calificacion no puede ser mayor a 10. Ingrese nuevamente." << endl;
                        --i;
                        continue;
                    }

                    cout << "Ingrese la ponderacion del examen o asignatura " << i << ": ";
                    cin >> ponderacion;

                    if (ponderacion > 100)
                    {
                        cout << "La ponderacion no puede ser mayor a 100. Ingrese nuevamente." << endl;
                        --i;
                        continue;
                    }

                    suma += valor * ponderacion;
                    suma_ponderaciones += ponderacion;
                }

                promedio_ponderado = suma / suma_ponderaciones;

                cout << "El promedio ponderado de las calificaciones es: " << promedio_ponderado << "%" << endl;

                cout << endl;
                system("pause");
                break;
            }
        }
        else if (opciones >= 3)
        {
            cout << "Hasta la Proxima..." << endl;
            break;
        }
        else
        {
            cout << "ERROR 444";
        }
    }
    cout << "Programa finalizado" << endl;
    cout << endl
         << endl;
    return 0;
}