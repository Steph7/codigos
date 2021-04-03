# _*_coding: utf-8 _*_

def substituirPalavra(string, palavra1, palavra2):
    fraseSeparada = frase.replace(',', ' ')
    fraseSeparada = fraseSeparada.replace('  ', ' ')

    palavrasfrase = fraseSeparada.split()

    contador = 0
    for x in palavrasfrase:
        if x == p1:
            contador += 1

    frase2 = frase.replace(p1, p2)

    print(frase2)
    print("Substituições realizadas: ", contador)



frase = input()
p1 = input()
p2 = input()

substituirPalavra(frase, p1, p2)