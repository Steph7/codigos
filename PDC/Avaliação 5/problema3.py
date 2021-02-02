# _*_coding: utf-8 _*_

def desembaralharPalavras(palavraEmbaralhada):
    palavraNova = palavraEmbaralhada[::-1]
    tamanhoPalavra = len(palavra)
    indiceMetade = tamanhoPalavra/2
    
    inicioPalavra = []
    finalPalavra = []
    x = 0

    while(x < indiceMetade):
        y = palavraNova[x]
        inicioPalavra.append(y)
        x += 1

    inicioPalavra = ''.join(inicioPalavra)
    print(inicioPalavra)

    while(x < tamanhoPalavra):
        y = palavraNova[x]
        finalPalavra.append(y)
        x += 1
    
    finalPalavra = ''.join(finalPalavra)
    print(finalPalavra)


    ordemCorreta = finalPalavra + inicioPalavra
    return ordemCorreta



palavra = input("Frase embaralhada: ")

palavraOrdem = desembaralharPalavras(palavra)

print("Frase correta: ", palavraOrdem)