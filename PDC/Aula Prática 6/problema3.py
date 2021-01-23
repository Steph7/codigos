# _*_coding: utf-8 _*_

def separarPareseimpares(numero1, numero2, numero3, numero4, numero5):
    listaTodos = [numero1, numero2, numero3, numero4, numero5]
    listaPar = []
    listaImpar = []
    for x in listaTodos:
        # Testar se é par
        if(x % 2 == 0):
            listaPar.append(x)
        else:
            listaImpar.append(x)
    print(listaTodos)
    print(listaPar)
    print(listaImpar)
    exit()

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

separarPareseimpares(num1, num2, num3, num4, num5)