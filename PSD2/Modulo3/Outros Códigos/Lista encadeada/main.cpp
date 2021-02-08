#include <iostream>
#include "lista.hpp"

int main() {

    Lista<string> l;

    l.inserir_final("python");
    l.inserir_final("c++");
    l.inserir_final("ruby");
    l.inserir_inicio("haskell");

    l.mostrar();

    cout << "Tamanho da lista: " << l.tamanho() << endl;
  return 0;
}