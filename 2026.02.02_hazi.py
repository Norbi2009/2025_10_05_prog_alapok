import random

def kartyaGeneralas():
    lista = []
    for i in range(1,14,1):
        lista.append("T"+str(i))
        lista.append("P"+str(i))
        lista.append("K"+str(i))
        lista.append("S"+str(i))
    return lista

def keveres(pakli):
    for i in range(500):
        a = random.randint(0,len(pakli)-1)
        b = random.randint(0,51)
        segedvaltozo = pakli[a]
        pakli[a] = pakli[b]
        pakli[b] = segedvaltozo

def lapIndexe(lap,pakli):
    index = 0
    #ciklus amíg (NEM Ttul(lista[i]))
    while( pakli[index] != lap):
        index += 1
    #c.v.
    #vissza: index
    return index



def main():
    pakli = kartyaGeneralas()
    #print(pakli)
    keveres(pakli)
    print(pakli)
    lap = input("Adjon meg egy lapot - T,P,S,K + [1,13](pl P1): ")
    index = lapIndexe(lap, pakli)
    print(index)
main()