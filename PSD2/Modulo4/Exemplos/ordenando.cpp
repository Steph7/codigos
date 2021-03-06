#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    vector<int> data;
    int val = 0;
    while(cin >> val){
        data.push_back(val);
    }
    sort(data.begin(), data.end());
    for(int elem:  data){
        cout << elem << " ";
    }
    cout << endl;
}

// Definindo a função polimófica -> TEMPLATE
/*
template <class T> void readNSort{
    vector<T> data;
    T val = 0;
    while(cin >> val){
        data.push_back(val);
    }
    sort(data.begin(), data.end());
    for(int elem:  data){
        cout << elem << " ";
    }
    cout << endl;
}
/*