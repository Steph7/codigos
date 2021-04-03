# _*_coding: utf-8 _*_

def desenharEstrelas(numero):
    listaDesenho = []
    for i in range(0, numero):
        listaDesenho.append('*')
    asteriscos = ''.join(listaDesenho)
    for i in range(0, numero):
        print(asteriscos[0:i])
    for i in range(0, numero):
        print(asteriscos[0:n-i])


n = int(input())

desenharEstrelas(n)