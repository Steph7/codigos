//Fonte do Código: https://www.youtube.com/watch?v=1XDBMy3rgi4&list=PL8eBmR3QtPL13Dkn5eEfmG9TmzPpTp0cV&index=49
// Aprendendo sobre Listas Encadeadas

#ifndef _LISTA_H_
#define _LISTA_H_

#include <iostream>
#include "no.hpp"

using namespace std;

//Classe LISTA
template<class T>

class Lista{
    private:
        No<T>* cabeca;
        No<T>* cauda;
    
    public:
        Lista();

        Lista(T v);

        virtual ~Lista();

        void mostrar();

        bool vazia();

        void inserir_inicio(T v);

        void inserir_final(T v);

        int tamanho();

        bool existe(T v);

        void remover();

};

#endif