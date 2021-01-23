# _*_coding: utf-8 _*_

import string as str

def separarString(texto):
    lista = texto.split(".")
    x = int(lista[0])
    y = int(lista[1])
    z = int(lista[2])
    w = int(lista[3])

    if(conferirIP(x, y, z, w) == True):
        print("Válido")
    else:
        print("Inválido")
    exit()

def conferirIP(parte1, parte2, parte3, parte4):
    if(parte1 >= 0) and (parte1 <= 255):
        if(parte2 >= 0) and (parte2 <= 255):
            if(parte3 >= 0) and (parte3 <= 255):
                if(parte4 >= 0) and (parte4 <= 255):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    exit()



enderecoIP = input()

separarString(enderecoIP)