# _*_coding: utf-8 _*_

def misturarStrings(string1, string2):
    lista1 = string1.split()
    lista2 = string2.split()
    n = len(string1)
    i = 0

    novaLista = []
    for x, y in  zip(lista1, lista2):
        if(i % 2 == 0) or (i == 0):
            novaLista.append(x)
        else:
            novaLista.append(y)
        i += 1
    novaString = ' '.join(novaLista)
    return novaString


s1 = input()
s2 = input()

print(misturarStrings(s1, s2))
print(misturarStrings(s2, s1))