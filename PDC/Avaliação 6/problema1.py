# _*_coding: utf-8 _*_

listaA = []
listaB = []
listaComum = [] #armazena os elementos que estão em ambas as listas 

#Quantidade de números a serem inseridos = 10
i = 0

while(i < 5):
    n = int(input())
    listaA.append(n)
    i += 1

while(i < 10):
    x = int(input())
    listaB.append(x)
    i += 1


#print(listaA)
#print(listaB)

for x in listaA:
    if x in listaB:
        listaComum.append(x)

print("Interseção: ", listaComum)