// Exercício do site https://www.ic.unicamp.br/~cmrubira/aacesta/cpp/cpp15.html
#include <iostream>

using namespace std;

struct circulo{
    float raio;
    float x;
    float y;
    
};

int main(){
    circulo ac;
    ac.raio = 10.0;
    ac.x = 1.0;
    ac.y = 1.0;

    cout << "Raio: " << ac.raio << endl;
    cout << "X: " << ac.x << endl;
    cout << "Y: " << ac.y << endl;
    
}



