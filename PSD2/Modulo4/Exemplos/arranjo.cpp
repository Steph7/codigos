#include <vector>
#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

template <class T, int N>
class BoundedArray{
        T memblock[N];
    public:
        void set (int x, T value);
        T get (int x);
};

template <class T, int N>
void BoundedArray<T, N>::set (int x, T value){
    assert(x >= 0 && x < N);
    memblock(x) = value;
}

template <class T, int N>
T BoundedArray<T,N>::get (int x){
    assert(x >= 0 && x < N);
    return memblock(x);
}

int main(){
    //Primeiro Exemplo INT
    BoundedArray <int, 5> myints;
    myints.set (0, 100);
    cout << myints.get(0) << '\n';
    return 0;

    // Segundo Exemplo DOUBLE/FLOAT
    /*
    BoundedArray <double, 9> myfloats;
    myfloats.set (3, 3.1416);
    cout << myfloats.get(3) << '\n';
    return 0;
    */
}

