# _*_coding: utf-8 _*_

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

if nota1 >= 0 and nota1 <= 10:
    r1 = True
else:
    r1 = False
if nota2 >= 0 and nota2 <= 10:
    r2 = True
else:
    r2 = False
    
if(r1 == True and r2 == True):
    media = (nota1 + nota2)/2
    print("%.2f" % media)
else:
    print('Nota inválida')