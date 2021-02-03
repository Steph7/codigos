#include "Estudante.hpp"
#include <iostream>
#include <cstring>
#include <iomanip>

struct EstudanteRSG{
    int matricula;
    std::string nome;
    float rsg_total;

    void melhoresAlunos();
};

int dadosAluno(Estudante *aluno){
    int matricula;
    std::string nome;
    float notas[5];
    int j;

    std::cin >> aluno->matricula;
    std::cin >> aluno->nome;
    for(j=0; j < 5; j++){
        std::cin >> aluno->notas[j];
    }
    return 0;
}

void melhoresAlunos(EstudanteRSG *aluno);

int main(){
    int size = 10;

    struct Estudante *aluno = new Estudante [size];
    struct EstudanteRSG *aluno_RSG = new EstudanteRSG [size];

    int i;

    for(i=0; i < size; i++){
        dadosAluno(aluno + i);
        (aluno_RSG + i)->matricula = (aluno + i)->matricula;
        (aluno_RSG + i)->nome = (aluno + i)->nome;
        aluno_RSG[i].rsg_total = (aluno + i)->calcularRSG();
    }
    
    melhoresAlunos(aluno_RSG);

    // Imprimir os TOP 3 melhores alunos
    for(i=0; i < 3; i++){
        std::cout << aluno_RSG[i].matricula << " ";
        std::cout << aluno_RSG[i].nome << " ";
        std::cout << std::fixed;
        std:: cout << std::setprecision(2) << aluno_RSG[i].rsg_total << std::endl;
    }  

    delete [] aluno;
    delete [] aluno_RSG;

    return 0;
}

void melhoresAlunos(EstudanteRSG *aluno) {
    for (int i = 0; i < 10; i++) {
        int iMaior = i;
        for (int iSeguinte = i+1; iSeguinte < 10; iSeguinte++) {
            // Ordenar os indexes de acordo com o RSG --> Ordem Decrescente
            if (aluno[iSeguinte].rsg_total > aluno[iMaior].rsg_total) {
                iMaior = iSeguinte;
            }
            // Caso o RSG total seja o mesmo, o desempate deverá ser feito de acordo com a menor matrícula
            if (aluno[iSeguinte].rsg_total == aluno[iMaior].rsg_total) {
                if(aluno[iSeguinte].matricula < aluno[iMaior].matricula){
                    iMaior = iSeguinte;
                }
            }
        }
        EstudanteRSG aux = aluno[i];
        aluno[i] = aluno[iMaior];
        aluno[iMaior] = aux;
    }
}