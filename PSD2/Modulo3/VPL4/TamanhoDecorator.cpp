#include "TamanhoDecorator.hpp"

std::string TamanhoDecorator::desenha(){
    std::string str = std::to_string(this->_tamanho);
    return FormaDecorator::desenha() + "\n- tamanho: " + str;
}

void TamanhoDecorator::setTamanho(int tamanho) {
  this->_tamanho = tamanho;
}

int TamanhoDecorator::getTamanho() {
  return this->_tamanho;
}