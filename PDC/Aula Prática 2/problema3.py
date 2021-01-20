# _*_coding: utf-8 _*_

idade = int(input("Digite a idade: "))
tempo_contribuicao =  int(input("Digite o tempo de contribuição: "))
sexo = input("Digite o sexo(M/F): ")


#SE HOMEM
if sexo == 'M':
    if idade >= 65:
        print('Pode aposentar')
    elif idade >= 60 and idade < 65:
        if tempo_contribuicao >= 35:
            print('Pode aposentar')
        else:
            print('Não pode aposentar')
    else:
            print('Não pode aposentar')

#SE MULHER
elif sexo == 'F':
    if idade >= 60:
        print('Pode aposentar')
    elif idade >= 55 and idade < 60:
        if tempo_contribuicao >= 30:
            print('Pode aposentar')
        else:
            print('Não pode aposentar')
    else:
            print('Não pode aposentar')