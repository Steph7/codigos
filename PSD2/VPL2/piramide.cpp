#include <iostream>
#include <string>

int main(){
    int i, num;
    std::string piramide;
    std::cin >> num;

    piramide ="*";
    std::cout << piramide << std::endl;
    
    for (i=1; i < num; i++){
        piramide += '*';
        std::cout << piramide << std::endl;
    }
    
    unsigned tam = piramide.size();
    
    for (i = num-1; i > 0; i--){
        piramide.resize(i);
        std::cout << piramide << std::endl;
    }
    return 0;
}