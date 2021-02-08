#include "Ponto2D.hpp"


std::string Ponto2D::to_string() const {
    std::string x = std::to_string(this->_x);
    std::string y = std::to_string(this->_y);
    std::string str = ("("+x + "," + y +")");
    return str;
}

double Ponto2D::distancia(Ponto* p) const {
    Ponto2D* p2 = dynamic_cast<Ponto2D*> (p);
    double dx = (p2->_x) - (this->_x);
    double dy = (p2->_y) - (this->_y);
    double dist = sqrt((dx*dx) + (dy*dy));
    return dist;

}

void Ponto2D::converteParaPolar(){
    double dx = (this->_x)*(this->_x);
    double dy = (this->_y)*(this->_y);
    double r = sqrt(dx + dy);
    double theta = atan(this->_y/this->_x);
    _x = r;
    _y = theta;
}