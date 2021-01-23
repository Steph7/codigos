# _*_coding: utf-8 _*_

f = open("texto.txt", "r")
texto = f.read()
linhas = texto.split("\n")

palavras = []
for x in linhas:
    palavras = palavras + x.split(" ")

maior = None
for x in palavras:
    if(maior == None) or (len(maior) < len(x)):
        maior = x

print(maior)
print(len(maior))

