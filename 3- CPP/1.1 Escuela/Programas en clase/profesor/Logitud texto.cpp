#include <iostream>
#include <string>
using namespace std;

int main() {
    string texto = "GABRIEL RODRIGUEZ SION";

    int inicio, longitud;
    int longitudTexto = 0;

    // Calcular la longitud del texto sin usar funciones de la biblioteca de C++
    for (int i = 0; texto[i] != '\0'; i++) {
        longitudTexto++;
    }

    cout << "ILA LONGITUD DE LA CADENA ES: " << longitudTexto;
    
    return 0;
}
