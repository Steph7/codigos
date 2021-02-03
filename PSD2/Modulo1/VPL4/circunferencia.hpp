#ifndef PI
#define PI 3.14
#endif

#ifndef CIRCUNFERECIA_H
#define CIRCUNFERENCIA_H

#include <cmath>

struct Circunferencia {
    double _xc, _yc; // coordenadas X e Y do centro do Circunferência
    double _raio; // raio do Circunferência

    Circunferencia(double, double, double);
    double calcularArea();
    bool possuiIntersecao(Circunferencia* c);
};

#endif