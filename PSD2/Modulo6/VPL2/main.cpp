#include <iostream>
#include <string.h>

struct IndiceNaoinicializado {
  int index;
};

struct IndiceNegativo {
  int index;
};

struct IndiceMaiorArranjo {
  int index;
}; 


template <class T, int N> class BoundedArray {
  public:
    void set(int index, T value) {
      if(index < 0) throw IndiceNegativo{index};
      if(index >= N) throw IndiceMaiorArranjo{index};
      else{
        buf[index] = value;
        testador[index] = 1;
      }
    }
    T get(int index) {
      if(index < 0) throw IndiceNegativo{index};
      if(index >= N) throw IndiceMaiorArranjo{index};
      if(testador[index] != 1) throw IndiceNaoinicializado{index};
      return buf[index];
    }
  private:
    T buf[N];
    int testador[N];
};

template <class T> void testArray() {
  BoundedArray<T, 8> a;
  char action;
  while (std::cin >> action) {
    int index;
    std::cin >> index;
    try {
      if (action == 's') {
        T value;
        std::cin >> value;
        a.set(index, value);
      } else if (action == 'g') {
        std::cout << a.get(index) << std::endl;
      }
    }
    catch (IndiceNaoinicializado e){
      std::cerr << "Erro: indice nao inicializado." << std::endl;
    }
    catch (IndiceNegativo e){
      std::cerr << "Erro: indice negativo." << std::endl;
    }
    catch (IndiceMaiorArranjo e){
      std::cerr << "Erro: indice maior que arranjo." << std::endl;
    }
    catch (...) {
      std::cerr << "Erro desconhecido." << std::endl;
    }
  }
}

int main() {
  char type;
  std::cin >> type;
  switch(type) {
    case 'd':
      testArray<double>();
      break;
    case 'i':
      testArray<int>();
      break;
    case 's':
      testArray<std::string>();
      break;
  }
  return 0;
}