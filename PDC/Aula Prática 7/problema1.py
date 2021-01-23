# _*_coding: utf-8 _*_

f = open("texto.txt", "r")
texto = f.read()
linhas = texto.split("\n")

maior = None

for x in linhas:
    x = x + '\n' #retornar o espaço que foi retirado durante a separação
    numeroCaracteres = len(x)
    if(maior == None) or (len(maior) < len(x)):
        maior = x

print(maior)
print(len(maior))