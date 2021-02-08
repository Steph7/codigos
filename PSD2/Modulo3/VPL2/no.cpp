#include "no.hpp"

No::No(int prioridade, int dado, No* proximo){
    this->_dado = dado;
    this->_proximo = NULL;
}

void No::setProximo(No *next){
    _proximo = next;
}

No::getProximo(){
    return _proximo;
}

int No::getDado(){
    return _dado;
}

void No::setDado(){
    _dado = dado;
}

int No::getPrioridade(){
    return _prioridade;
}

void No::setPrioridade(int prioridade){
    _prioridade = prioridade;
}