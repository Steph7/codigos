#include "FilaPrioridade.hpp"

FilaPrioridade::FilaPrioridade(){
    this->cabeca = NULL;
    this->cauda = NULL;
}

void FilaPrioridade::inserir(int prioridade, int dado){
    this->cabeca = new No(prioridade, dado);
    this->cauda = cabeca;  //só tem um elemento
}

int FilaPrioridade::remover(){
    cabeca = cabeca->getPrioridade();
}

bool FilaPrioridade::estaVazio(){
    return (cabeca == NULL);
}

unsigned FilaPrioridade::getTamanho(){
     if(estaVazio()){
        return 0;
    }

    No* c = cabeca;
    int tam = 0;
    do{
        c = c->getProximo();
        tam++;
    }while(c);
    return tamanho = tam;
}

int FilaPrioridade::getMeio(){
    return No[n];
}

int FilaPrioridade::getUltimo(){
    No* c = cauda;
    while(c){
        if(c->getProximo() == NULL){
            cout << c->getDado() << ' ';
            c = c->getProximo();
        }
    }
    return false;
}

void FilaPrioridade::furaFila(int dado){
    No* novo_no = new No(1, dado);

    novo_no->setProximo(cabeca);
    cabeca = novo_no;
}

void FilaPrioridade::print(){
    cout << "Imprimindo todos os elementos: \n";
    No* c = cabeca;
    if(estaVazio()){
        cout << "A lista não possui elementos \n";
    }
    else{
        while(c){
            cout << c->getDado() << endl;
            c = c->getProximo();
        }
        cout << endl;
    }
}