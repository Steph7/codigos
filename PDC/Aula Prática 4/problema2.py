# _*_coding: utf-8 _*_

def gerador_tabuada(numero):
    x = 1
    print('Tabuada de', numero, ':')
    while(x <= 10):
        tab = numero * x
        print(numero, 'X', x, '=', tab)
        x += 1
    exit()



#RECEBER número do usuário
num = int(input("Digite um inteiro: "))

gerador_tabuada(num)