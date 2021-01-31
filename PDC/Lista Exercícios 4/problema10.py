# _*_coding: utf-8 _*_

def separarNumero(stringNumero):
    return [char for char in stringNumero]

def escreverNumeroporextenso(stringNumero):
    listaStringnumeros = separarNumero(n)
    numeros = []
    
    for x in listaStringnumeros:
        numeros.append(int(x))
    #print(numeros)
    tamanhoLista = len(numeros)
    
    #Nomes dos números por extenso
    unidades = {0: "", 1: "um", 2: "dois", 3: "tres", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove"}
    dezenasEspeciais = {10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "catorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"}
    dezenas = {2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta", 8: "oitenta", 9: "noventa"}
    centenaEspecial = {1: "cem"}
    centenas = {1 :"cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seiscentos", 7: "setecentos", 8: "oitocentos", 9: "novecentos"}
    milhares = {1: "mil"}

    #Lista nome do nº por extenso
    nomeNumero = []
    
    # MIL (valor máximo)
    if(tamanhoLista == 4):
        if(numeros[0] == 1):
            mil = milhares[1]
            nomeNumero.append(mil)

    # UNIDADES, DEZENAS E CENTENAS                      
    if(tamanhoLista==3):
        if((numeros[0] == 1) and (numeros[1] == 0) and (numeros[2] == 0)):
            cent = centenaEspecial[numeros[0]]
            nomeNumero.append(cent)
        else:
            cent = centenas[numeros[0]]
            if((numeros[1] == 0) and (numeros[2] == 0)):
                nomeNumero.append(cent)
            elif(numeros[1] == 0) and (numeros[2] != 0):
                uni = unidades[numeros[2]]
                nomeNumero.extend((cent, 'e', uni))
            else:
                dezenasEsp = int(''.join(stringNumero[1:]))
                if(dezenasEsp in dezenasEspeciais):
                    dez = dezenasEspeciais[dezenasEsp]
                    nomeNumero.extend((cent, 'e', dez))
                else:
                    dez = dezenas[numeros[1]]
                    if(numeros[2] == 0):
                        nomeNumero.extend((cent, 'e', dez))
                    else:
                        uni = unidades[numeros[2]]
                        nomeNumero.extend((cent, 'e', dez, 'e', uni))
    
    # UNIDADES E DEZENAS          
    if(tamanhoLista==2):
        dezenasEsp = int(''.join(stringNumero[0:]))
        if(dezenasEsp in dezenasEspeciais):
            dez = dezenasEspeciais[dezenasEsp]
            nomeNumero.append(dez)
        else:
            dez = dezenas[numeros[0]]
            if(numeros[1] == 0):
                nomeNumero.append(dez)
            else:
                uni = unidades[numeros[1]]
                nomeNumero.extend((dez, 'e', uni))
    
    # Só UNIDADES        
    if(tamanhoLista==1):
        uni = unidades[numeros[0]]
        nomeNumero.append(uni)


    nomeNumero = " ".join(nomeNumero)
    print(nomeNumero)
    #Remover os espaços para contar apenas as letras
    nomeNumero = nomeNumero.replace(" ", "")
    quantidadeLetras = len(nomeNumero)
    
   
    return quantidadeLetras


# Pedir entrada de dados ao usuário
n = input()

quantidade = escreverNumeroporextenso(n)

print(quantidade)