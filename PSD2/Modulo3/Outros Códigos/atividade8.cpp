#include <iostream>
#include <string.h>

using namespace std;

int main(){

    int Bino;
    int Cino;
    int totalDedos;
    string vencedor;

    cin >> Bino;
    cin >> Cino;

    totalDedos = Bino + Cino;

    if(totalDedos % 2 == 0){
        vencedor = "Bino";
    }
    else{
        vencedor = "Cino";
    }

    cout << vencedor << endl;
    
}