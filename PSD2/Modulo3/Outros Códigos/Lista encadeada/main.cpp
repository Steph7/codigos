#include <iostream>
#include "lista.hpp"
#include "no.hpp"

int main() {

    Lista l;

    l.inserir_final(10);
    l.inserir_final(20);
    l.inserir_final(30);
    l.inserir_inicio(40);

    l.mostrar();

    cout << "Tamanho da lista: " << l.tamanho() << endl;
  return 0;
}