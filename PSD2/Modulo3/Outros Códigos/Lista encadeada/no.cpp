#include <iostream>
#include "no.hpp"

using namespace std;

No::No(int v){
    this->v = v;
    this->prox = NULL;
}

int No::obterValor(){
    return v;
}

No* No::obterProx(){
    return prox;
}

void No::setProx(No* p){
    this->prox = p;
}