//Fonte do Código: https://www.youtube.com/watch?v=1XDBMy3rgi4&list=PL8eBmR3QtPL13Dkn5eEfmG9TmzPpTp0cV&index=49
// Aprendendo sobre Listas Encadeadas

#ifndef _LISTA_H_
#define _LISTA_H_

#include <iostream>
#include "no.hpp"

using namespace std;

//Classe LISTA

class Lista{
    private:
        No* cabeca;
        No* cauda;
    
    public:
        Lista();

        Lista(int v);

        ~Lista();

        void mostrar();

        bool vazia();

        void inserir_inicio(int v);

        void inserir_final(int v);

        int tamanho();

        bool existe(int v);

        void remover();

};

#endif