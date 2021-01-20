#_*_coding: utf-8 _*_

dias = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

# Avaliar se o ano é bissexto
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    bissexto = True
else:
    bissexto = False

# Verificar se o mês é um número válido
if mes >= 1 and mes <= 12:
    mes_ok = True
else:
    mes_ok = False

meses_com_30 = {4,6,9,11}
meses_com_31 = {1,3,5,7,8,10,12}

if bissexto == True and mes == 2:
    if dias <= 29:
        dias_ok = True
    else:
        dias_ok = False
elif bissexto == False and mes == 2:
    if dias <= 28:
        dias_ok = True
    else:
        dias_ok = False

for x in meses_com_30:
    if mes == x:
        if dias <= 30:
            dias_ok = True
        else:
            dias_ok = False

for x in meses_com_31:
    if mes == x:
        if dias <= 31:
            dias_ok = True
        else:
            dias_ok = False
    

if mes_ok == True and dias_ok == True:
    print('Data válida')
else:
    print('Data inválida')