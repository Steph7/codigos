#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

int main(){
    
    // p1 e p2 = são os pesos das crianças 
    // c1 e c2 = são os comprimentos de cada lado da gangorra

    int p1, p2, c1, c2;
    int lado1, lado2;

    cin >> p1 >> c1 >> p2 >> c2;

    lado1 = p1*c1;
    lado2 = p2*c2; 

    if(lado1 == lado2){
        // Equilíbrio
        cout << 0 << endl;
    }
    else if(lado1 > lado2){
        // Desequilíbrio criança esquerda na parte de baixo
        cout << -1 << endl;
    }
    else{
        cout << 1 << endl;
    }

    
}