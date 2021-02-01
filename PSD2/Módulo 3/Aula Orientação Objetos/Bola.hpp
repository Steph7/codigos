#ifndef BOLA
#define BOLA

#include <string>

class Bola{

public:
	float peso;
	float raio;
	std::string cor;

	void setPeso(float);
	float getPeso();
}; 

#endif