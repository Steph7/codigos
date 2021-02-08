#include "Ponto4D.hpp"

std::string Ponto4D::to_string() const {
    std::string x = std::to_string(this->_x);
    std::string y = std::to_string(this->_y);
    std::string z = std::to_string(this->_z);
    std::string w = std::to_string(this->_w);
    std::string str = ("("+x + "," + y + "," +z + "," +w + ")");
    return str;
}

double Ponto4D::distancia(Ponto* p) const {
    Ponto4D* p4 = dynamic_cast<Ponto4D*> (p);
    double dx = (p4->_x) - (this->_x);
    double dy = (p4->_y) - (this->_y);
    double dz = (p4->_z) - (this->_z);
    double dw = (p4->_w) - (this->_w);
    double dist = sqrt((dx*dx) + (dy*dy) + (dz*dz) + (dw*dw));
    return dist;

}