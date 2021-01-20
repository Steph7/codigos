# _*_coding: utf-8 _*_

velocidade_max = float(input("Digite o valor da velocidade máximo: "))
velocidade_registrada = float(input("Digite o valor da velocidade registrada: "))

infr_media = velocidade_max * 1.2
infr_grave = velocidade_max * 1.5

if (velocidade_registrada <= velocidade_max):
    print('Sem Infração')
if (velocidade_registrada == infr_media):
    print('Infração Média')
if(velocidade_registrada > infr_media and velocidade_registrada <= infr_grave):
    print('Infração Grave')
if(velocidade_registrada > infr_grave):
    print('Infração Gravíssima')