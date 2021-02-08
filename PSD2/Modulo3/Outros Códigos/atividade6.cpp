#include <iostream>
#include <string.h>

using namespace std;

int main(){

    // A = nota prova 1 e B = nota prova 2
    float a, b;
    float media;
    string status;

    cin >> a >> b;

    media = (a + b)/2;

    if(media >= 7){
        status = "Aprovado";
    }
    else if((media >= 4) && (media < 7)){
        status = "Recuperacao";
    }
    else{
        status = "Reprovado";
    }

    cout << status << endl;
    

}