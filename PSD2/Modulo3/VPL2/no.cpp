#include "no.hpp"

No::No(int prioridade, int dado){
    this->_dado = dado;
    this->_proximo = NULL;
    this->_prioridade = prioridade;
}

//ok
void No::setProximo(No *next){
    this->_proximo = next;
}

//ok
No* No::getProximo(){
    return _proximo;
}

//ok
int No::getDado(){
    return _dado;
}

//ok
void No::setDado(int dado){
    this->_dado = dado;
}

//ok
int No::getPrioridade(){
    return _prioridade;
}

//ok
void No::setPrioridade(int prioridade){
    this->_prioridade = prioridade;
}