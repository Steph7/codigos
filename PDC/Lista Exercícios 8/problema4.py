# _*_coding: utf-8 _*_

def nota_media(dicio, lista):
    soma = 0
    n = len(lista)

    for materia, nota in dicio.items():
        for x in lista:
            if materia is x:
                soma = soma + nota
    media = soma/n        
    return media
    
d = input()
lista = input()

print(nota_media(d, lista))