# _*_coding: utf-8 _*_

def contarUm (string):
    contador = 0
    for x in string:
        if(x == '1'):
            contador += 1
    return contador


numero = input()

print(contarUm(numero))