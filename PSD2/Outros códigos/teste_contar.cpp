#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

void separarPalavras(std::string str);

int main(){
    std::cout << "Digite um texto: " << std::endl;
    std::string palavras;
    std::vector<std::string> guardaPalavra;
    std::string s;

    // Receber palavra inserida pelo usuário (teclado)
    std::getline (std::cin,s);
    // Função para separar o texto por palavras
    separarPalavras(s);
    
    for (std::string e : palavras)
        guardaPalavra.push_back(e);

    sort(guardaPalavra.begin(), guardaPalavra.end());

    int tamanhoVetor = guardaPalavra.size();

    if(tamanhoVetor == 0){
        std::cout << "Nenhuma palavra! =( " << std::endl;
        return 1;
    }

    int contadorPalavras=1;
    palavras = guardaPalavra[0];

    for(int i=1; i < tamanhoVetor; i++){
        if(palavras != guardaPalavra[i]){
            std::cout << palavras << "apareceu " << contadorPalavras << "vezes " << std::endl;
            contadorPalavras=0;
            palavras = guardaPalavra[i];
        }
        contadorPalavras++;
    }

    std::cout << palavras << "apareceu " << contadorPalavras << "vezes " << std::endl; 

    return 0;
    
}

void separarPalavras(std::string str) { 
    std::set<std::string>set;
    std::string palavra; 
    std::stringstream iss(str);
    
    while (iss >> palavra)
        set.insert(palavra);
        for (std::string e : set)
            std::cout << e << std::endl; 
} 