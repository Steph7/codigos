# _*_coding: utf-8 _*_

#import <string>

def removerZeros(numero1, numero2):
    soma = numero1 + numero2
    stringSoma = str(soma)

    novoNumero = []

    for x in stringSoma:
        if(int(x)!=0):
            novoNumero.append(x)
    
    novoNumero = "".join(novoNumero)
    novoNumero = int(novoNumero)
    return novoNumero


#ENTRADAS do usuário

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

semZero = removerZeros(n1, n2)

print("Resultado: ", semZero)