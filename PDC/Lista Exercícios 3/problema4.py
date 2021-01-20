# _*_coding: utf-8 _*_

def total_segundos(int1, int2, int3):
    s1 = int1 * 3600
    s2 = int2 * 60
    soma = s1 + s2 + int3
    print(soma)
    exit()

# Receber dados do usuário

# Horas
h = int(input())

# Minutos
m = int(input())

# Segundos
s = int(input())

total_segundos(h, m, s)