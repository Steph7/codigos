#include <iostream>
#include <queue>

using namespace std;

class Pessoa{
private:
    string _nome;
    int _idade;
public:
    Pessoa(string nome, int idade);
    ~Pessoa();
    string getNome();
    int getIdade();
};

Pessoa::Pessoa(string nome, int idade){
    this->_nome = nome;
    this->_idade = idade;
}

Pessoa::~Pessoa(){
}

string Pessoa::getNome(){
    return _nome;
}

int Pessoa::getIdade(){
    return _idade;
}

struct CompIdade{
    bool operator() (Pessoa &p1, Pessoa &p2){
        return p1.getIdade() < p2.getIdade();
    }
};


int main(){

    priority_queue<Pessoa, vector<Pessoa>, CompIdade> pq;

    Pessoa p1("João", 40);
    Pessoa p2("Maria", 55);
    Pessoa p3("Pedro", 22);
    

    pq.push(p1);
    pq.push(p2);
    pq.push(p3);

    Pessoa pessoa = pq.top();
    
    cout << "Nome: " << pessoa.getNome() << endl;
    cout << "Idade: " << pessoa.getIdade() << endl;

    return 0;
}