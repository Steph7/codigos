# _*_coding: utf-8 _*_

numero = int(input("Digite um inteiro: "))
f = open("texto.txt", "r")
texto = f.read()
linhas = texto.split("\n")

caracteres = [',', '.', '!', '?']

palavras = []
for x in linhas:
    palavras = palavras + x.split(" ")


for x in palavras:
    for y in x:
        if (y in caracteres):
            y = ''
    if(len(x) <= numero):
        print(x)
