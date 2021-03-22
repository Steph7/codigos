# _*_coding: utf-8 _*_

def separarRNA(stringRNA):
    listaRNA = []
    for i in range(0, len(stringRNA), 3):
        n = i + 3
        novaString = stringRNA[i:n]
        listaRNA.append(novaString)
        print(novaString)
    return listaRNA


rnaTipos = {'UUU':'Phe', 'CUU':'Leu', 'UUA':'Leu', 'AAG': 'Lisina', 'UCU':'Ser', 'UAU':'Tyr', 'CAA':'Gln'}

rna = input("Digite o RNA: ")

listaseparadaRNA = separarRNA(rna)
cadeiaAminoacidos = []

for x in listaseparadaRNA:
    if x in rnaTipos:
        cadeiaAminoacidos.append(rnaTipos[x])

aminoacidos = '-'.join(cadeiaAminoacidos)

print("Cadeia de Aminoácidos: ", aminoacidos)