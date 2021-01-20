# _*_coding: utf-8 _*_

#Função para verificar se o número é primo
def teste_primo(numero):
    x = 1
    quant = 0
    while (x <= numero):
        if (numero % x == 0):
            quant += 1
        x += 1
    if quant == 2:
        print('É primo')
    else:
        print('Não é primo')
    exit()

#Receber número inteiro do usuário
n = int(input("Digite um inteiro n: "))

teste_primo(n)