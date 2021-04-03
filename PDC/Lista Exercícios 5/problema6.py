# _*_coding: utf-8 _*_

def verificarContido(string1, string2):
    if string2 in string1:
        return True
    else:
        return False

frase1 = input()
frase2 = input()

print(verificarContido(frase1, frase2))