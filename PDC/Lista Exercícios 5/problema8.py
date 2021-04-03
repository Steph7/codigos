# _*_coding: utf-8 _*_

def encontrarMaiorproduto(string):
    maior = None
    grupoMaior = []

    for i in range (0, len(string) - 2):
        seq = string[i:i+3]
        num1 = int(string[i])
        num2 = int(string[i+1])
        num3 = int(string[i+2])

        produto = num1 * num2 * num3

        if maior == None or produto > maior:
            maior = produto
            grupoMaior = seq
    return grupoMaior

frase = input()

print(encontrarMaiorproduto(frase))
