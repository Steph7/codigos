#include "Circunferencia.hpp"

Circunferencia::Circunferencia(double xc, double yc, double raio){
    _xc = xc;
    _yc = yc;
    _raio = raio;
}

double Circunferencia::calcularArea(){
    double area = PI * pow(_raio, 2);
    return area;
}

/* Para saber se existe uma intersecção entre as duas circunferências será necessários fazer duas operações:
 (1) R + r > d (se a soma dos raios das circunferências for maior que a distância entre os centros, elas são circunferências externas)
 (2) Para calcular a distância entre dois pontos (duas coordenadas) - [Distância entre os centros]
        --> dAB = raiz da soma dos quadrados das diferenças entre o ponto xc e yc de cada circunferência
        dAB = raiz((xcA - xcB)^2 + (ycA - ycB)^2)
*/


bool Circunferencia::possuiIntersecao(Circunferencia* c){
    double dx = c->_xc - this->_xc;
    double dy = c->_yc - this->_yc;
    if (sqrt((dx*dx) + (dy*dy)) > (c->_raio + this->_raio)) {
        return false; // não tem intersecção
    }
    else {
        return true; // tem intersecção
    }
}