# _*_coding: utf-8 _*_

def contarEspacos(string):
    contador = 0
    for x in string:
        if(x == ' '):
            contador += 1
    return contador

frase = input()

print(contarEspacos(frase))