# _*_coding: utf-8 _*_

def verificaTriangulo(a, b, c):
    if(a < b + c):
        if(b < a + c):
            if(c < b + a):
                return True
            return False
        return False
    return False

def tipoTriangulo(a , b, c):
    if(a == b) and (b == c):
        print("Triângulo Equilátero")
    elif(a == b) or (b == c) or (a == c):
        print("Triângulo Isósceles")
    elif(a != b) and (b != c) and (a != c):
        print("Triângulo Escaleno")



x = float(input("Digite o comprimento do primeiro lado: " ))
y = float(input("Digite o comprimento do segundo lado: " ))
z = float(input("Digite o comprimento do terceiro lado: "))


teste = verificaTriangulo(x, y, z)

if(teste == True):
    tipoTriangulo(x, y, z)
else:
    print("Não é um triângulo")