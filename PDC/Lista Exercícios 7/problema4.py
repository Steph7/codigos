# _*_coding: utf-8 _*_

def contarUm(string):
    contador = 0
    for x in string:
        if(x == '1'):
            contador += 1
    return contador

def num1s(arquivo):
    linhas = arquivo.readlines()
    s = ""
    # print(linhas)
    for x in linhas:
        s = x
        # print(s)
    print(contarUm(s))