#include <iostream>
using namespace std;

main()
{

    int n1, n2;

    n1 = 0, n2 = 0;

    cout << "Introduce el primer valor:";
    cin >> n1;

    cout << "Introduce el segundo valor:";
    cin >> n2;

    if (n1 > n2)
    {
        cout << "El primer valor es mayor " << n1;
    }

    else
    {
        cout << "El segundo valor es mayor " << n2;
    }

    return 0;
}
