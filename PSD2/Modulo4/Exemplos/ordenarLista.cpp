#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

template <class T>
T sumList(deque <T> &data){
    if(data.empty()){
        throw "Error: empty list";
    } else {
        T sum = getFirst(data);
        for (T elem: data){
            // Funciona com os tipos: int, string, double
            sum += elem;
            // Funciona com os tipos: int, string, double e list
            // sum = sum + elem;
        }
        return sum;
    }
}

template <class T>
T getFirst(deque <T> &data){
    T first = data.front();
    data.pop_front();
    return first;
}

struct S{
    int x, y;
    // Para funcionar com o template devem ser feitas as 
    // seguintes alterações
    // Operador +
    S& operator + (const S &obj){
        S res;
        res.x = obj.x + x;
        res.y = obj.y + y;
        return res;
    }

    // Operador +=
    S& operator += (const S &obj){
        x = obj.x + x;
        y = obj.y + y;
        return *this;
    }
};