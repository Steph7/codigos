# _*_coding: utf-8 _*_

numero = int(input())

f = open("texto.txt", "r")
texto = f.read()
linhas = texto.split("\n")

palavras = []
for x in linhas:
    palavras = palavras + x.split(" ")

for x in palavras:
    if(len(x) >= numero):
        print(x)