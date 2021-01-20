# _*_coding: utf-8 _*_

def paridade(numero):
    # Se o número for par
    if(numero % 2 == 0):
        return True
    # Se o número for ímpar
    else:
        return False

# Receber número do usuário

n = int(input())
print('resultado', paridade(n))