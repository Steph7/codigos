#_*_coding: utf-8 _*_

palavra = input('Digite uma palavra: ')

palavraInvertida = str(palavra)[::-1] # [::-1] faz com seja lida a sequência da ordem inversa

print(palavra, palavraInvertida)

if(palavra == palavraInvertida):
    print("É palíndromo")
else:
    print("Não é palíndromo")


