#ifndef _NO_H_
#define _NO_H_

#include <iostream>
#include "no.hpp"

using namespace std;

// Classe NÓ
class No{
    private:
        int v;
        No* prox;

    public:
        No(int v);

        int obterValor();

        No* obterProx();

        void setProx(No* p);
};

#endif