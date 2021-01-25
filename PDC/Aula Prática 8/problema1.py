# _*_coding: utf-8 _*_

def soma(m, n):
    if(n == m):
        return m
    else:
        while(m < n):
            return m + soma(m + 1, n)


num1 = int(input("Digite m: "))
num2 = int(input("Digite n: "))

soma = soma(num1, num2)
print(soma)