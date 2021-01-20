# _*_coding: utf-8 _*_


def removerDuplicados(string):
    output = ""
    char_usados = ""
    for x in string:
        if char_usados == x:
            output = output[:-1] + x.upper()
        elif char_usados!= x:
            output = output + x
        char_usados = x
    print(output)


palavra = input("Digite uma palavra: ")

removerDuplicados(palavra)