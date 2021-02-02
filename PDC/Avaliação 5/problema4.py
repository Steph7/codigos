# _*_coding: utf-8 _*_

def cifrarTexto(palavra, chaveDeslocamento):
    lista = []
    for x in palavra:
        y = ord(x) + chave
                
        if(y > 122):
            y = y - 122 + 97 - 1
            
        y = chr(y)
        lista.append(y)
    lista = ''.join(lista)
    return lista

#ENTRADAS usuários

palavra = input("Digite uma palavra: ")
chave =int(input("Digite o valor da chave: "))

novaPalavra = cifrarTexto(palavra, chave)

print("Resultado: ", novaPalavra)