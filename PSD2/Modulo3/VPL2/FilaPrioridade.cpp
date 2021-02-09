#include "FilaPrioridade.hpp"

FilaPrioridade::FilaPrioridade(){
    this->cabeca = NULL;
    this->cauda = NULL;
}

void FilaPrioridade::inserir(int prioridade, int dado){
    No* novo_no = new No(prioridade, dado);

    // Se só tem 1 elemento
    if(estaVazio()){
        novo_no->setProximo(cabeca);
        cabeca = novo_no;
    }
    
    // Se tem apenas 2 elementos
    else if(novo_no->getPrioridade() < cabeca->getPrioridade()){
        novo_no->setProximo(cabeca);
        cabeca = novo_no;
    }
    
    else{
        cabeca->setProximo(novo_no);
    }
    
}

/*
void FilaPrioridade::inserir(int prioridade, int dado){
    No* novo_no = new No(prioridade, dado);

    novo_no->setProximo(cabeca);
    cabeca = novo_no; 

    for(No* novo_no = cabeca; novo_no->getProximo() != NULL; novo_no = novo_no->getProximo()){
        No* menor = novo_no;
        for(No* j = novo_no->getProximo(); j != NULL; j = j->getProximo()){
            if(j->getPrioridade() <= menor->getPrioridade()){
                menor = j;
            }
        }
        No* aux = novo_no;
        novo_no = menor;
        menor = aux;
    }
}
*/


int FilaPrioridade::remover(){
    No* temp = cabeca;
    cabeca = cabeca->getProximo();

    return temp->getDado();
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
    this->tamanho = tam;
    return tamanho;
}

int FilaPrioridade::getMeio(){
    No* c = cabeca;
    int i = 0;
    // Se só tiver 1 elemento
    if(c->getProximo() == NULL){
        return c->getDado();
    }
    // Se tiver apenas 2 elementos
    else if(c->getProximo()->getProximo() == NULL){
        c = c->getProximo();
        return c->getDado();
    }
    // Se tiver mais de 2 elementos
    else{
        int meio = (tamanho/2) - 1;
        while(i <= meio){
            c = c->getProximo();
            i++;
        }
        return c->getDado();
    }
}

int FilaPrioridade::getUltimo(){
    No* c = cabeca;
    while(c->getProximo() != NULL){
        c = c->getProximo();
    }
    return c->getDado();
}


void FilaPrioridade::furaFila(int dado){
    No* novo_no = new No(1, dado);

    novo_no->setProximo(cabeca);
    cabeca = novo_no;
}

void FilaPrioridade::print(){
    No* c = cabeca;
    if(estaVazio()){
        cout << "A lista não possui elementos \n";
    }
    else{
        while(c){
            cout << c->getDado() << ' ';
            c = c->getProximo();
        }
        cout << endl;
    }
}
