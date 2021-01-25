# _*_coding: utf-8 _*_

def mdc(numero1, numero2):
    if(numero2 == 0):
        return numero1
    else:
        while(numero2 != 0):
            return mdc(numero2, numero1 % numero2)

x = int(input("Digite x: "))
y = int(input("Digite y: "))

divisorComum = mdc(x, y)
print(divisorComum)