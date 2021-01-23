# _*_coding: utf-8 _*_

def definirMediasaltos(distancia1, distancia2, distancia3, distancia4, distancia5):
    maior = None
    menor = None
    soma = 0
    quantidade = 0
    contadorMaior = 0
    contadorMenor = 0
    listaSaltos = [distancia1, distancia2, distancia3, distancia4, distancia5]
    novalistaSaltos = []
    for n in listaSaltos:
        if(maior == None) or (maior < n):
            maior = n
    for n in listaSaltos:
        if(menor == None) or (menor > n):
            menor = n
    for n in listaSaltos:
        if((n != maior) and (n != menor)):
            novalistaSaltos.append(n)
        if(n == maior):
            contadorMaior += 1
        if(n == menor):
            contadorMenor += 1
        if(contadorMaior > 1) and (len(novalistaSaltos) < 3):
            novalistaSaltos.append(maior)
        if(contadorMenor > 1) and (len(novalistaSaltos) < 3):
            novalistaSaltos.append(menor)
    for n in novalistaSaltos:
        soma = soma + n
        quantidade += 1
    media = soma / quantidade
    print("Média: ", "%.2f" % media)
    exit()



dist1 = float(input())
dist2 = float(input())
dist3 = float(input())
dist4 = float(input())
dist5 = float(input())

definirMediasaltos(dist1, dist2, dist3, dist4, dist5)
