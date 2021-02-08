#include <iostream>
#include "no.hpp"


No::No(T v){
    this->v = v;
    this->prox = NULL;
}

T No::obterValor(){
    return v;
}

No::obterProx(){
    return prox;
}

void No::setProx(No* p){
    this->prox = p;
}