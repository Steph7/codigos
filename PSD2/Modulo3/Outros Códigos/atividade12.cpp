#include <iostream>
#include <math.h>

using namespace std;

int main(){
    
   // a e b são lâmpadas
   // I1 e I2 são interruptores

   // No início as lâmpadas estão apagadas
   int a = 0;
   int b = 0;

    // N = número de vezes que o amigo apertará os interuptores
    int n;
    cin >> n;

    int max = pow(10, 5);

    if((n <= 2) || (n >= max)){
        cin >> n;
    }

    int *valor = new int[n];

    int x = 0;
    while(x < n){
        cin >> valor[x];
        x++;
    }


    for(int y = 0; y < n; y++){
        if(valor[y] == 1){
            a = !a;
        }
        else if(valor[y] == 2){
            a = !a;
            b = !b;
        }   
    }

    cout << a << endl;
    cout << b << endl;

}