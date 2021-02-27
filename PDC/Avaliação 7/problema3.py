# _*_coding: utf-8 _*_

def definirIdade(data):    
    diaAtual = 5
    mesAtual = 10
    anoAtual = 2020
    
    numerosData = data.split("/")
    dia = int(numerosData[0])
    mes = int(numerosData[1])
    ano = int(numerosData[2])

    # Cenário depois do aniversário 
    if(mes < mesAtual):
        idade = anoAtual - ano

    # Cenário: mês é o mês do aniversário
    elif(mesAtual == mes):
        if(dia <= diaAtual):
            idade = anoAtual - ano
        else:
            idade = (anoAtual - ano) - 1

    #Cenrário depois do aniversário
    else:
        idade = (anoAtual - ano) - 1
        
    return idade



f = open("datas.txt", "r")
texto = f.read()
pessoas = texto.split("\n")


for dados in pessoas:
    dadosPessoas = dados.split(" ")
    nome = dadosPessoas[0]
    data = dadosPessoas[1]
    
    idadePessoa = definirIdade(data)
    print("Nome:", nome)
    print("Idade: %d anos" % (idadePessoa))