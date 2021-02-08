#include "FilaPrioridade.hpp"

FilaPrioridade::FilaPrioridade(){
    cabeca = NULL;
    cauda = NULL;
}

void FilaPrioridade::inserir(int prioridade, int dado){
    cabeca = new No(prioridade, dado)
    cauda = cabeca;
}

int FilaPrioridade::remover(){
    delete cabeca;
    return cabeca->getPrioridade();
}

bool FilaPrioridade::estaVazio(){
    return (cabeca == NULL);
}

