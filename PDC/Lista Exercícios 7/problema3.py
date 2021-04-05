# _*_coding: utf-8 _*_

def valores(arquivo):
    linhas = arquivo.readlines()
    numeros = []
    for linha in linhas:
        numeros.append(int(linha))
    
    soma = 0
    somaPares = 0
    quantPares = 0
    quantPrimos = 0
    contador = 0
    maior = None
    menor = None

    for x in numeros:
        soma = soma + x
        if(maior == None) or (x > maior):
            maior = x
        if(menor == None) or (x < menor):
            menor = x
        if(x % 2 == 0):
            somaPares = somaPares + x
            quantPares += 1
    if (quantPares != 0):
        mediaPares = somaPares/quantPares
    else:
        mediaPares = 0

    for x in numeros:
        for y in range(1, x):
            if(x % y == 0):
                contador += 1
        if(contador == 1):
            quantPrimos += 1

    print("A soma é:%d" % soma)
    print("O maior número é:%d" % maior)
    print("O menor número é:%d" % menor)
    print("A média dos pares é:%d" % mediaPares)
    print("O número de primos é:%d" % quantPrimos)

# def valores(arquivo):
#     linhas = arquivo.readlines()
#     numeros = [int(num.strip()) for num in linhas]
#     print('A soma é:', sum(numeros))
#     print('O maior número é:', max(numeros))
#     print('O menor número é:', min(numeros))
    
#     n = 0
#     total = 0
#     nprimos = 0

#     for i in numeros:
#         primo = True

#     if i % 2 == 0:
#         total += i
#         n += 1
    
#     if i <= 1:
#         primo = False
    
#     for j in range(2,i):
#         if i % j == 0:
#             primo = False
#             break
#     if primo == True:
#         nprimos += 1

#     print('A média dos pares é:', total/n)
#     print('O número de primos é:', nprimos)