# _*_coding: utf-8 _*_

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

#Salvar os elementos em uma lista
lista = [n1, n2, n3]

#ordenar a lista em ordem decrescente
lista.sort()

#A mediana de quantidades ímpares de números, 
# corresponde sempre ao valor central, o que
# nesse caso simplifica a situação pois sabemos
# que existem apenas 3 números em nossa lista

mediana = lista[1]

print('Mediana:', mediana)



