# _*_coding: utf-8 _*_

def lerData(string):
    if string[2] and string[5] != '/':
        exit()
    data = string.split('/')
    dia = data[0]
    mes = data[1]
    ano = data[2]
    for x in data:
        if type(int(x)) is not int:
            exit()
    dataCompleta = ' '.join(data)
    return dataCompleta
    
data = input()
print(lerData(data))