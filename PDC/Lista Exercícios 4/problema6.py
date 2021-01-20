# _*_coding: utf-8 _*_

def escalas(inicio, m, passo):
    for linha in range (inicio, m + 1, passo):
        #Fahrenheit
        f = linha * (9/5) + 32
        #Kelvin
        k = linha + 273
        print(linha, int(f), k)


#Temperatura início
temp_inicio = int(input())

#Temperatura fim
temp_fim = int(input())

#Intervalo
intervalo = int(input())

escalas(temp_inicio, temp_fim, intervalo)