# _*_coding: utf-8 _*_
import codecs

def separarCaracteres(palavra):
    return [char for char in palavra]

f = open("PDC\Outros\dna.txt", "r", encoding = 'utf=8')
texto = f.read()
letraMusica = texto.split("\n")

# EXEMPLO TESTE
#s = "유난히도 반짝였던 서울! 처음 보는 또 다른 세상 땀에 잔뜩 밴 채 만난 넌 뭔가 이상했었던 아이 난 달에서, 별에서 우리 대화는 숙제 같았지 하루는 베프, 하루는 웬수"
#s = s.split()

d = dict() #Palavras selecionadas
interjeicao = ['oh', 'la', 'na', 'La','yeah', 'ya', 'ooh', 'Oh', 'Hoo', 'hoo']
particulas = ['은', '를', '는']
pronomes = ['저', '나', '난', '저희', '저희들', '우리', '우린', '우리들', '너', '자네', '그대', '당신', '너희', '너희들', '너네', '너네들', '자네들', '그대들', '당신들', '그', '그녀', '그들', '그녀들']
pontuacao = [',' , '.', '!', '?', '(', ')']
palavrasIngles = ['love', 'DNA', 'you', 'us', 'I', 'lovers', 'baby', 'You', 'myself', 'me', "lovin'", 'stop', "can't", 'what', 'my', 'it', 'know', 'do']

d3 = dict() # Palavras excluídas
d4 = dict() #Palavras coreanas (pronomes e partículas)

for linha in letraMusica:
    palavras = linha.split()
    #print(palavras)
    for x in palavras:
        if(x in pontuacao) or (x in interjeicao) or (x in palavrasIngles):
            if(x not in d3):
                d3[x] = 1
            else:
                d3[x] += 1
        elif(x in particulas) or (x in pronomes):
            if(x not in d4):
                d4[x] = 1
            else:
                d4[x] += 1
        elif(x not in d):
            d[x] = 1
        else:
            d[x] += 1

#print(d)
#print(d3)
#print(d4)

i = 1 #contador
palavrasAprendidas = 0
palavrasMaisfrequentes = dict()
for item in sorted(d, key = d.get, reverse = True)[:5]:
    print ("Palavra", i, ":", item, "Quantidade:", d[item]) 
    i += 1
    palavrasAprendidas = palavrasAprendidas + d[item]

totalPalavras = 0
totalPalavrasconhecidas = 0
totalParticulasepronomes = 0

for x in d:
    totalPalavras = totalPalavras + d[x]
for y in d3:
    totalPalavras = totalPalavras + d3[y]
    totalPalavrasconhecidas = totalPalavrasconhecidas + d3[y]
for z in d4:
    totalPalavras = totalPalavras + d4[z]
    totalParticulasepronomes = totalParticulasepronomes + d4[z]

porcentagemAprendida = (palavrasAprendidas/totalPalavras)*100
porcentagemConhecida = (totalPalavrasconhecidas/totalPalavras)*100
porcentagemParticulasepronomes = (totalParticulasepronomes/totalPalavras)*100
porcentagemTotal = porcentagemAprendida + porcentagemConhecida

numeroPalavras = len(d)
numeroPalavrasconhecidas = len(d3)
numeroParticulasepronomes = len(d4)
numeroPalavrasTotal = numeroPalavras + numeroPalavrasconhecidas + numeroParticulasepronomes

print('--------------------------------------------- \n')
print("Total de aparições das palavras Aprendidas: ", palavrasAprendidas)
print("Total de aparições das palavras Conhecidas: ", totalPalavrasconhecidas)
print("Total de Palavras: ", totalPalavras)
print('--------------------------------------------- \n')

print("Quantidade de palavras diferentes na letra: ", numeroPalavrasTotal)
print("Quantidade de palavras diferentes conhecidas na letra: ", numeroPalavrasconhecidas)
print("Quantidade de partículas e pronomes diferentes na letra: ", numeroParticulasepronomes)
print('--------------------------------------------- \n')
print("Porcentagem de palavras aprendidas da letra: ", "%.2f" % porcentagemAprendida, '%')
print("Porcentagem de palavras já conhecidas da letra: ", "%.2f" % porcentagemConhecida, '%')
print("Porcentagem de particulas e pronomes na letra: ", "%.2f" % porcentagemParticulasepronomes, '%')
print("Porcentagem letra conhecida (com as novas palavras): ", "%.2f" % porcentagemTotal, '%')