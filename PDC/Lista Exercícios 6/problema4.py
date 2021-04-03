# _*_coding: utf-8 _*_

def trocarCaractere(string):
    primeiroCaractere = string[0]
    restoString = string[1:]
    # print(restoString)
    if(primeiroCaractere not in restoString):
        return string
    else:
        for x in restoString:
            if (x == primeiroCaractere):
                novaResto = restoString.replace(x, "*")
        novaString = primeiroCaractere + novaResto
        return novaString


frase = input()

print(trocarCaractere(frase))