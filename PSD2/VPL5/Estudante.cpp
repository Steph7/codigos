#include "Estudante.hpp"


float Estudante::calcularRSG(){
    int i;
    float soma = 0.0;
    float media = 0.0;

    for(i=0; i < 5; i++){
        soma = soma + this->notas[i];
    }
    media = soma/5.0;
    return media;
}

