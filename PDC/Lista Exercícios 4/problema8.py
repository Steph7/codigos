# _*_coding: utf-8 _*_

def salario_atual():
    # O salário em 2015 era de R$2000
    salario = 2000
    
    ano_inicial = 1995
    ano_atual = 2020
    tempo = ano_atual - ano_inicial

    # 1996 Ano em que o aumento foi de 1.5%
    aumento = 1.5/100
    x = 0 #Pois estamos considerando um período de tempo começando de 2015
    while(x < tempo):
        # A partir de 1997, a taxa de aumento passou a ser o dobro do ano anterior
        #ano_iteracao = ano_inicial + x
        salario = salario * (1 + aumento)
        aumento = (aumento * 2)
        x += 1
    return salario

print(salario_atual())