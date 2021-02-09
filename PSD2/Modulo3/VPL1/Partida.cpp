#include "Partida.hpp"
#include "Jogador.hpp"


Partida::Partida(int num_jogadores){
    this->_num_jogadores = num_jogadores;
}

Partida::~Partida(){

}

void Partida::addJogadorCarta(string nomeJogador, int numero_pontos_carta, string naipe){
    /*
    Verificar se já existe um jogador com esse nome, caso exista, devemos apenas adicionar as cartas.
    Se não existir, temos que criar um novo jogador, e com isso, temos que atualizar o nº de jogadores da partida.
    Após a criação do jogador, deve ser cadastrado o º da carta e seu naipe. Isso deve ser feito a partir de uma comunicação com a Classe Carta.
    */
   int i = getNumAtualJogadores();
   if(i == 0){
       setJogadores();
   }
    for(int i= 0; i < _num_jogadores; i++){
        this->_jogadores[i].Jogador();
            for(int j = 0; j <  ; j++){
                Carta cartaNova = Carta(numero_pontos_carta, naipe);
                this->_jogadores[i].adicionaCarta(cartaNova);
            }
    
    }

    
}
	
int Partida::getNumJogadores(){
    /*(Retornar) Obter a quantidade de Jogadores da rodada*/
    return this->_num_jogadores;

}

int Partida::getNumAtualJogadores(){
    /*Atualizar a quantidade de jogadores*/
    this->_atualSize;

}

void Partida::setJogadores(Jogador* jogadores){
    /*Definir os jogadores. */
    int i = 0;
    while(i <= getNumJogadores){
        this->_jogadores = new Jogador[i];
    }
}


void Partida::imprimeJogadoresOrdenados(){
    // cout << << endl;

}


Jogador* Partida::getJogadores(){}
Jogador Partida::getCampeao(){}
Jogador* Partida::getJogadoresOrdenados(){}
 /*
 void selection_sort(int num[], int tam) { 
  int i, j, min, aux;
  for (i = 0; i < (tam-1); i++) 
  {
     min = i;
     for (j = (i+1); j < tam; j++) {
       if(num[j] < num[min]) 
         min = j;
     }
     if (i != min) {
       aux = num[i];
       num[i] = num[min];
       num[min] = aux;
     }
  }
}
 */