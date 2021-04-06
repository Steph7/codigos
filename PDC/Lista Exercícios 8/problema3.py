# _*_coding: utf-8 _*_

def maior_nota(dicionario):
    maior = max(zip(dicionario.values(), dicionario.keys()))
    nota = maior[0]
    materia = maior[1]
    print(materia, "%.1f" % nota)
    exit()


d = input()

maior_nota(d)