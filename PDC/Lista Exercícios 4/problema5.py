# _*_coding: utf-8 _*_

def floyd(numero):
    n = 1

    #Definir as linhas
    for linha in range(1, numero + 1):
        #Definir as colunas com base na linha
        for coluna in range(1, linha + 1):
            print(n, end= " ")
            n = n + 1
        print()

#Digite um número inteiro
n = int(input())

floyd(n)
