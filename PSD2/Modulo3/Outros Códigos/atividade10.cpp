#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

int main(){
    // n = número de dias
    // a = número de acessos por dia
    int n;
    int max_dias = pow(10, 3);
    int max_acessos = pow(10, 6);

    cin >> n;
    
    if((n < 1) || (n > max_dias)){
        //pedir novamente o valor de n
        cin >> n;
    }
    
    int *a = new int[n];
    int x = 0;
    int y = 1;
    int soma = 0;

    for(x = 0; x < n; x++){
        cin >> a[x];
        if((a[x] < 1) || (a[x] > max_acessos)){
            //pedir novamente o valor de n
            cin >> a[x];
        }
    }   

    for(x = 0; x < n; x++){
        soma = soma + a[x];
        //cout << soma << endl;
        if(soma < max_acessos){
            y++;
        }
        else{
            cout << y << endl;
            break;
        }

    }

    
}