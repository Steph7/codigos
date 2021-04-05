# _*_coding: utf-8 _*_

def converterFahrenheit(temperaturaC):
    temperaturaF = temperaturaC * (9/5) + 32
    return temperaturaF

def converterKelvin(temperaturaC):
    temperaturaK = temperaturaC + 273
    return temperaturaK

def escalas(arquivo):
    linhas = arquivo.readlines()
    
    inicio = int(linhas[0])
    fim = int(linhas[1])
    intervalo = int(linhas[2])
    

    for i in range(inicio, fim + 1, intervalo):
        tF = converterFahrenheit(i)
        tK = converterKelvin(i)
        print(i, "%d" % tF, tK)
