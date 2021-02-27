# _*_coding: utf-8 _*_

f = open("frases.txt", "r")
texto = f.read()
linhas = texto.split("\n")

#print(linhas)

frases = []

for linha in linhas:
    y = (linha.split(" "))
    #print(y)
    y = ''.join(y)
    y = y.lower()
    frases.append(y)
    
quant = 0
    
for frase in frases:
    print(frase)
    print(frase[::-1])
    if(frase == frase[::-1]):
        quant += 1

print("Quantidade de palíndromos: ", quant)
    
#print(frases)
