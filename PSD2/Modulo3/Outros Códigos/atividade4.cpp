#include <iostream>
#include <math.h>

using namespace std;

int main(){

    int P, R;

    string porta;

    cin >> P;
    cin >> R;

    if(P == 0){
        porta = "C";
    }
    else if((P == 1) && (R == 0)){
        porta = "B";
    }
    else{
        porta = "A";
    }

    cout << porta << endl;

}