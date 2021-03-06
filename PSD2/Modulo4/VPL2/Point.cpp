#include <iostream>

#include "Point.h"

std::ostream & operator << (std::ostream &out, const Point &p) {
  // TODO: implement this operator.
  out << "(" << p.getX() << ',' << p.getY() << ")";
  return out;
}

std::istream & operator >> (std::istream &in,  Point &p) {
  // TODO: implement this operator.
  in >> p.x >> p.y;
  return in;
}

Point Point::operator + (const Point &p) {
  // TODO: implement this operator.
  Point novoPonto;
  novoPonto.x = this-> x + p.x;
  novoPonto.y = this-> y + p.y;
  return novoPonto;
}

Point& Point::operator += (const Point &p) {
  // TODO: implement this operator.
  this->x += p.x;
  this->y += p.y;
  return *this;
}