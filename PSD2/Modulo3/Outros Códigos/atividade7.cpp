#include <iostream>
#include <string.h>

using namespace std;

int main(){

    int x;
    string mensagem;

    cin >> x;

    if(x == 0){
        mensagem = "nulo";
    }
    else if(x < 0){
        mensagem = "negativo";
    }
    else{
        mensagem = "positivo";
    }
    
    cout << mensagem << endl;

}