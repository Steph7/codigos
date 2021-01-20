# _*_coding: utf-8 _*_

def total_segundos(int1, int2, int3):
    s1 = int1 * 3600
    s2 = int2 * 60
    soma = s1 + s2 + int3
    print('resultado', soma)
    exit()

# Receber dados do usuário
t = input()
lista = [int(i) for i in t.split(' ') ]
#print(lista)

# Horas
h = int(lista[0])

# Minutos
m = int(lista[1])

# Segundos
s = int(lista[2])

#print ('h =', h, 'm =', m, 's =', s)

total_segundos(h, m, s)