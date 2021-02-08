// Exercício do site https://www.ic.unicamp.br/~cmrubira/aacesta/cpp/cpp15.html
#include <iostream>

using namespace std;

struct contador {
    int num;

    void incrementa(void){
        num = num + 1;
    }
    void comeca(void){
        num = 0;
    }
};

int main(){
    contador umcontador;

    umcontador.comeca();
    cout << umcontador.num << endl;

    umcontador.incrementa();
    cout << umcontador.num << endl;
}