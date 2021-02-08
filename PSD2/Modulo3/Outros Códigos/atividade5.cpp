#include <iostream>
#include <string.h>

using namespace std;

int main(){

    // A = alunos e M = monitores
    int A;
    int M;
    int soma;
    string resultado;

    cin >> A;
    cin >> M;

    soma = A + M;

    if(soma <= 50){
        resultado = "S";
    }
    else{
        resultado = "N";
    }
    
    cout << resultado << endl;

}