#include "Indice.hpp"
#include <iomanip>
#include <iostream>
#include <map>
#include <algorithm>

void separarPalavras();

int main(){
    // Função para separar o texto por palavras
    separarPalavras();
    
    return 0;
}


void separarPalavras() { 
    std::map<std::string, unsigned int> contarPalavras;
    std::string palavra;
    float soma=0;
    
    while (std::cin >> palavra)
        if (contarPalavras.find(palavra) == contarPalavras.end()) // Palavra encontrada pela primeira vez.
            contarPalavras[palavra] = 1; 
        else // Se já foi encontrada antes:
            contarPalavras[palavra]++; // Acrescenta uma (a cada vez que a palavra for encontrada de novo)

    for(auto it = contarPalavras.cbegin(); it != contarPalavras.cend(); ++it){
        soma = soma + it->second;
    }
    
    for(auto it = contarPalavras.cbegin(); it != contarPalavras.cend(); ++it){
        if(it->first.length() >= 3){
            std::cout << std::fixed;
            std::cout << std::setprecision(2);
            std::cout << it->first << " " << it->second << " " << it->second/soma <<  "\n";
        }
    } 
} 
