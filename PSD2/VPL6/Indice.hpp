#ifndef INDICE_H
#define INDICE_H

/* DESCRIÇÃO: 
// (1) Contar nº total de palavras no texto
// (2) Contar quantas vezes cada palavra aparece no texto -> nº aparições da palavra
// (3) Calcular % de aparição de cada palavra -> nº aparições da palavra / nº total de palavras
// (4) Colocar lista das palavras em ordem alfabética
// (5) Verificar quais palavras têm mais do que 3 caracteres
// (6) Imprimir as palavras (com mais de 3 caracteres) + nº de vezes que a palavra apareceu + % de aparição no texto
*/

#include <iostream>

struct salvaPalavra{
    std::string _palavra;
    int _quantidade;
    float _aparicao; 
};


#endif