# _*_coding: utf-8 _*_

unidades = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
dezenas = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
centenas = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

numero = input("Digite um número: ")

numeroInvertido = numero[::-1]

numeroRomano = []

for i in range(0, len(numero), 1):
    n = int(numeroInvertido[i])

    #unidades
    if  i == 0:
        for x in unidades:
            if x == n:
                numeroRomano.append(unidades[n])
    #dezenas
    if i == 1:
        for x in dezenas:
            if x == n:
                numeroRomano.append(dezenas[n])
    #centenas
    if i == 2:
        for x in centenas:
            if x == n:
                numeroRomano.append(centenas[n])

#print(numeroRomano)

numeroRomano = numeroRomano[::-1]
numeroRomano = ''.join(numeroRomano)

print("Número Romano: ", numeroRomano)