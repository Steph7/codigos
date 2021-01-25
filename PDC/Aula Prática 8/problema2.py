# _*_coding: utf-8 _*_

def power(numero1, numero2):
    if(numero2 == 1):
        return numero1
    else:    
        while(numero2 > 1):
            return numero1 * power(numero1, numero2-1)


k = int(input("Digite k: "))
n = int(input("Digite n: "))

potencia = power(k, n)
print(potencia)