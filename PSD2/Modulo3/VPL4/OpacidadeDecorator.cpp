#include "OpacidadeDecorator.hpp"

std::string OpacidadeDecorator::desenha(){
    /*
        * Para valores de 0 a 0.33 (inclusive) a opacidade deve receber valor "baixa"
        * Para valores de 0.33 a 0.66 (inclusive), a opacidade deve receber valor "média"
        * Para valores de 0.66 a 1 (inclusive), a opacidade deve receber valor "alta"
    */

    if((this->getOpacidade() >= 0) && (this->getOpacidade() <= 0.33)){
        return FormaDecorator::desenha() + "\n- opacidade: baixa";
    }
    else if((this->getOpacidade() > 0.33) && (this->getOpacidade() <= 0.66)){
        return FormaDecorator::desenha() + "\n- opacidade: média";
    }
    else if((this->getOpacidade() > 0.66) && (this->getOpacidade() <= 1)){
        return FormaDecorator::desenha() + "\n- opacidade: alta";
    }
    else{
        return FormaDecorator::desenha();
    }
}
    

void OpacidadeDecorator::setOpacidade(double opacidade){
    this->_opacidade = opacidade;
}
  
  
double OpacidadeDecorator::getOpacidade(){
    return this->_opacidade;
}