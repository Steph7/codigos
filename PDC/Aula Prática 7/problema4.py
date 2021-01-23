# _*_coding: utf-8 _*_

f = open("datas.txt", "r")
texto = f.read()
linhas = texto.split("\n")

datas = []
for x in linhas:
    data = x.split("/")
    data = data[::-1]
    datas.append(data)

print(datas)

maisRecentes = None
for x in datas:
    if(maisRecentes == None) or (maisRecentes < x):
        maisRecentes = x

maisRecentes = maisRecentes[::-1]

print(maisRecentes)