#include "Estudante.hpp"

Estudante::calcularRSG(float notas[]){
    int i;
    float soma = 0.0;
    float rsg[5];
    float rsg_total;
     
    for(i=0; i < 5; i++){
        // Maior ou igual a 90 -> 5
        if(this->notas[i] >= 90.0){
            rsg[i] = 5.0;
        }
        // Maior ou igual a 80 -> 4
        else if(this->notas[i] >= 80.0){
            rsg[i] = 4.0;
        }
        // Maior ou igual a 70 -> 3
        else if(this->notas[i] >= 70.0){
            rsg[i] = 3.0;
        }
        // Maior ou igual a 60 -> 2
        else if(this->notas[i] >= 60.0){
            rsg[i] = 2.0;
        }
        // Entre 40 e 59 -> 1
        else if(this->notas[i] >= 40.0 && this->notas[i] < 60.0){
            rsg[i] = 1.0;
        }
        // Menor do que 40
        else {
            rsg[i] = 0.0;
        }
             
    }  
    
    for(i=0; i < 5; i++){
        soma = soma + rsg[i];
    }
    
    rsg_total = soma/5;
    return rsg_total;