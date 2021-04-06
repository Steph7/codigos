# _*_coding: utf-8 _*_

def nome_mais_comum(listaNomes):
    d = dict()
    for nome in listaNomes:
        if nome not in d:
            d[nome] = 1
        else:
            d[nome] += 1
    sorted(d)
    return max(d)

