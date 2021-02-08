#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    
   // a e b são números
    float a, b;
	float divisao;

    cin >> a;
    cin >> b;
    divisao = (a/b);
	

    cout << setprecision(3) << divisao << endl;

}