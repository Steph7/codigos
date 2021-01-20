# _*_coding: utf-8 _*_

def fizz_buzz(x):
    if((x % 3 == 0) and (x % 5 == 0)):
        print("FizzBuzz")
    elif((x % 3) == 0):
        print("Fizz")
    elif((x % 5) == 0):
        print("Buzz")
    else:
        print(x)
    exit()

y = int(input("Digite um número inteiro: "))

fizz_buzz(y)