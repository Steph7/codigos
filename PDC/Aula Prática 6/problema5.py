# _*_coding: utf-8 _*_

def ordenarData(data):
    listaData = data.split("/")
    dia = listaData[0]
    mes = listaData[1]
    ano = listaData[2]
    print("%s/%s/%s" % (mes, dia, ano))
    exit()


data = input()

ordenarData(data)

    
