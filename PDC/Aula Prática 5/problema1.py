# _*_coding: utf-8 _*_

nome_completo = input("Digite seu nome completo: ") 

nome = nome_completo.split()

ultimo = len(nome)
sobrenome = nome[ultimo - 1]

nome_primeiros = ""

for x in nome:
    if x not in sobrenome:
        nome_primeiros += (x + " ")

sobrenome = sobrenome.strip()

print("Nome formatado: %s, %s" % (sobrenome, nome_primeiros))