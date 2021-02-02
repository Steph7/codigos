# _*_coding: utf-8 _*_

#import <string>

def alternarStrings(palavra1, palavra2):
    novaPalavra = []
    x = 0
    y = 0

    tamanhoPalavra1 = len(palavra1)
    tamanhoPalavra2 = len(palavra2)

    if(tamanhoPalavra1 >= tamanhoPalavra2):
        maior = palavra1
        menor = palavra2
    else:
        maior = palavra2
        menor = palavra1
    
    if(tamanhoPalavra1 != tamanhoPalavra2):
        while (x < len(maior)):
            while(y < len(menor)):
                w = palavra1[x]
                novaPalavra.append(w)
                z = palavra2[y]
                novaPalavra.append(z)
                y += 1
                x += 1
            w = maior[x]
            novaPalavra.append(w)
            x += 1
    else:
        while(x < len(maior)):
            w = palavra1[x]
            novaPalavra.append(w)
            z = palavra2[x]
            novaPalavra.append(z)
            x += 1
  
    novaPalavra = "".join(novaPalavra)
    return novaPalavra   


p1 = input("Digite a primeira palavra: ")
p2 = input("Digite a segunda palavra: ")

novaString = alternarStrings(p1, p2)

print("Combinação: ", novaString)