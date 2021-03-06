/**
 * Todas as tarefas deste exercicio devem ser feitas sobre esse arquivo.
 * Os metodos e operacoes marcados com a tag "TODO" devem ser editados.
 */

#include <iostream>
#include <vector>
#include <typeinfo>
#include "polygon.h"

std::ostream& operator << (std::ostream &out, const Polygon &poly) {
  for (const Point& p: poly.limits) {
    out << " " << p;
  }
  return out;
}

bool operator == (const Polygon &lhs, const Polygon &rhs) {
  // TODO: implement this method.
  std::vector<Point>vetorPontoslhs = lhs.operator const std::vector<Point, std::allocator<Point>> &();
  std::vector<Point>vetorPontosrhs = rhs.operator const std::vector<Point, std::allocator<Point>> &();
  if(vetorPontoslhs == vetorPontosrhs) {
    return true;
  }
  return false;
}

bool Point::contains(const Point& p) const {
  return p.x == this->x && p.y == this->y;
}

std::ostream& operator << (std::ostream &out, const Point &p) {
  out << "(" << p.x << ", " << p.y << ")";
  return out;
}

bool RightRectangle::contains(const Point& p) const {
  // TODO: implement this method.
  int i;
  int contador = 0;
  /*
  int maiorX = 0;
  int menorX = 0;
  int maiorY = 0;
  int menorY = 0;
  for(i = 0; i < limits.size(); i++){
    if(this->limits[i].x >= maiorX){
      maiorX = this->limits[i].x;
    }
    if(this->limits[i].x <= menorX){
      menorX = this->limits[i].x;
    }
    if(this->limits[i].y >= maiorY){
      maiorY = this->limits[i].y;
    }
    if(this->limits[i].y <= menorY){
      menorY = this->limits[i].y;
    }
  }
  if((p.x >= menorX) && (p.x <= maiorX) && (p.y >= menorY) && (p.y <= maiorY)){
    return true;
  }
  else{
    return false;
  }
  */
  
  for(i = 0; i < limits.size(); i++){
    if((this->limits[i].x < p.x) && (this->limits[i].y > p.y)){
      contador += 1;
    }
  }
  if(contador > 0){
    return true;
  }
  else{
    return false;
  }
}

Point::Point(int xx, int yy): x(xx), y(yy) {
    // TODO: implement this method.
  this->limits.push_back(*this);
}

RightRectangle::RightRectangle(int x0, int y0, int x1, int y1) {
  // TODO: implement this method.
  Point ponto1 = Point(x0, y0);
  Point ponto2 = Point(x1, y1);
  Point ponto3 = Point(x0, y1);
  Point ponto4 = Point(x1, y0);
  this->limits.push_back(ponto1);
  this->limits.push_back(ponto2);
  this->limits.push_back(ponto3);
  this->limits.push_back(ponto4);
  //Rectangle(ponto1, ponto2);
}