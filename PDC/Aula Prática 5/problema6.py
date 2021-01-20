# _*_coding: utf-8 _*_

nome = input("Digite um nome: ")

print(nome)

output = nome
for x in nome:
    output = output[:-1]
    print(output)
