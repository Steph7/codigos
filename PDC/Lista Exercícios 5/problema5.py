# _*_coding: utf-8 _*_


def verificarPalindromo(string):
    aoContrario = string[::-1]
    if string == aoContrario:
        return True
    else:
        return False


frase = input()


if (verificarPalindromo(frase) == True):
    print("É palíndromo!")
else:
    print("Não é palíndromo!")