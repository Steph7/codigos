# _*_coding: utf-8 _*_

d = dict()
maior = None

while True:
    entrada = input()   
    if entrada == '-1':
        break
    else:
        if(entrada not in d):
            d[entrada] = 1
            continue
        else:
            d[entrada] = d[entrada] + 1
            continue    
    exit()

for x in d:
    if((maior == None) or (d[x] > maior)):
        maior = d[x]
        imprimirMaior = x
print(imprimirMaior)   