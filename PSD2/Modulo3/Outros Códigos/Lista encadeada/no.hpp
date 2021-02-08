#ifndef _NO_H_
#define _NO_H_

#include <iostream>

using namespace std;

template<class T> 

// Classe NÓ
class No{
    private:
        T v;
        No* prox;

    public:
        No(T v);

        T obterValor();

        No* obterProx();

        void setProx(No* p);
};

#endif