# _*_coding: utf-8 _*_

def imprimirNumerosraizesinteiras(numero1, numero2):
    x = numero1
    while (x <= numero2):
        z = x ** (1/2)
        if(z.is_integer() == True):
            print(x)
        x += 1
    

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

imprimirNumerosraizesinteiras(x, y)

