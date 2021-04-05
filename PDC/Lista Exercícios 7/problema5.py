# _*_coding: utf-8 _*_

def espacosBrancos(arquivo):
    linhas = arquivo.readlines()
    #print(linhas)
    contador = 0
    for x in linhas:
        for y in x:
            if(y == ' '):
                contador += 1
    return contador