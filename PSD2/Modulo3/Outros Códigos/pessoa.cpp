#include <iostream>
using namespace std;

class Pessoa{
    private:
        int idade;
        float peso;
    public:
        Pessoa(int i, float p);

        int getIdade();
        void imprimirIdade();
};

Pessoa::Pessoa(int i, float p){
    idade = i;
    peso = p;
}
int Pessoa::getIdade(){
    return idade;
}

void Pessoa::imprimirIdade(){
    cout << "Idade: " << getIdade() << endl;
}


int main(){
    Pessoa p(29, 80);

    p.imprimirIdade();
    return 0;
}