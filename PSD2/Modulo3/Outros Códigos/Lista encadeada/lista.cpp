//Fonte do Código: https://www.youtube.com/watch?v=1XDBMy3rgi4&list=PL8eBmR3QtPL13Dkn5eEfmG9TmzPpTp0cV&index=49
// Aprendendo sobre Listas Encadeadas
#include <iostream>
#include "lista.hpp"

Lista::Lista(){
    this->cabeca = NULL;
    this->cauda = NULL;
}

Lista::Lista(T v){
    this->cabeca = new No<T>(v);
    this->cauda = cabeca; //só tem um elemento
}

virtual Lista::~Lista(){
    delete cabeca;
}

void Lista::mostrar(){
    template<class T>
    cout << "Imprimindo todos os elementos: \n";
    No<T>* c = cabeca;
    if(vazia()){
        cout << "A lista não possui elementos \n";
    }
    else{
        while(c){
            cout << c->obterValor() << endl;
            c = c->obterProx();
        }
        cout << endl;
    }
}

bool Lista::vazia(){
    return(cabeca == NULL);
}

void Lista::inserir_inicio(T v){
    No<T>* novo_no = new No<T>(v);

    novo_no->setProx(cabeca);
    cabeca = novo_no;
}

void Lista::inserir_final(T v){
    No<T>* novo_no = new No<T>(v);
    if(vazia()){
        cabeca = novo_no;
        cauda = novo_no;
    }
    else{
        cauda->setProx(novo_no);
        cauda = novo_no;
    }
}

int Lista::tamanho(){
    if(vazia()){
        return 0;
    }

    No<T>* c = cabeca;
    int tam = 0;
    do{
        c = c->obterProx();
        tam++;
    }while(c);
    return tam;
}

bool Lista::existe(T v){
    No<T>* c = cabeca;
    while(c){
        if(c->obterValor() == v){
            return true;
        }
        c = c->obterProx();
    }
    return false;
}

void Lista::remover(){
    if(!vazia()){
        // se tiver só um elemento
        if(cabeca->obterProx() == NULL){
            cabeca = NULL;
        }
        // 2 elementos
         else if(cabeca->obterProx()->obterProx() == NULL){
            cabeca->setProx(NULL);
        }
        // +2 elementos
        else{
            No<T>* ant_ant = cabeca;
            No<T>* ant = cabeca->obterProx();
            No<T>* corrente = cabeca->obterProx()->obterProx();

            while(corrente){
                No<T>* aux = ant;
                ant = corrente;
                ant_ant = aux;
                corrente = corrente->obterProx();
            }
            delete ant_ant->obterProx();
            ant_ant->setProx(NULL);
            cauda = ant_ant;
        }
    }
}