#include "Ponto3D.hpp"

std::string Ponto3D::to_string() const {
    std::string x = std::to_string(this->_x);
    std::string y = std::to_string(this->_y);
    std::string z = std::to_string(this->_z);
    std::string str = ("("+x + "," + y + "," +z + ")");
    return str;
}

double Ponto3D::distancia(Ponto* p) const {
    Ponto3D* p3 = dynamic_cast<Ponto3D*> (p);
    double dx = (p3->_x) - (this->_x);
    double dy = (p3->_y) - (this->_y);
    double dz = (p3->_z) - (this->_z);
    double dist = sqrt((dx*dx) + (dy*dy) + (dz*dz));
    return dist;

}