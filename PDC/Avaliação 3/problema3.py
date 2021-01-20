# _*_coding: utf-8 _*_

def estacionamento(hora_entrada, min_entrada, hora_saida, min_saida):
    # Transformar o tempo em minutos para realizar a contagem de tempo
    if(hora_entrada < hora_saida):    
        tempo_horas = (hora_saida - hora_entrada) * 60
    elif(hora_entrada > hora_saida):
        tempo_horas = ((24 - hora_entrada) + (hora_saida)) * 60

    tempo_minutos = (min_saida - min_entrada)

    # Definir o tempo total (em minutos)
    tempo_total = tempo_horas + tempo_minutos

    resto = (tempo_total % 60)

    if(resto == 0):
        tempo_total = tempo_total
    else:
        tempo_total = tempo_total + (60 - resto)

    if(tempo_total <= 120):
        preco = (round(tempo_total/60)) * 1
    elif(tempo_total > 120) and (tempo_total < 240):
        preco = (round(tempo_total/60)) * 1.40
    elif(tempo_total >= 240):
        preco = (round(tempo_total/60)) * 2
    #preco = round(preco)
    print("Preço: R$", "%.2f" % preco)
    exit()

hora_ent = int(input("Digite a hora de chegada: " ))
min_ent = int(input("Digite o minuto de chegada: "))
hora_part = int(input("Digite a hora de partida: " ))
min_part = int(input("Digite o minuto de partida: "))

estacionamento(hora_ent, min_ent, hora_part, min_part)