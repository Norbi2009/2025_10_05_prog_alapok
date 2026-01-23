import random

def maximumIndex(lista):
    maxi = 0 
    # ciklus i = 1-tól (n-1)-ig egyesével
    for i in range(1,len(lista),1):
    #    ha(lista[i]>lista[maxi])
        if(lista[i]>lista[maxi]):
            maxi = i
    #   e.v.
    #c.v.
    #vissza: maxi
    return maxi


def veletlenLista(szam):
    szam = 10
    lista = []

    for i in range(0,szam,1):
        veletlen = random.randint(-19,19)
        if(veletlen > 1):
            lista.append(veletlen * 50)
        elif(veletlen < -1):
            lista.append(veletlen * 50)
    print(lista)

    def negativ00reVegzodo(barmilyenLista):
        db = 0
        for i in range(0,len(barmilyenLista,1)):
            if(barmilyenLista[i] % 100 == 0):
                db+=1
        return db
def pozitivSzamokAtlaga(lista):
    db = 0
    osszeg = 0
    for elem in lista:      #végigmegyünk a lista összes elemén
        if(elem>0):         #ha pozitiv a szam akkor 
            db+=1           # a db valtozot noveljuk 1-gyel
            osszeg += elem
    atlag = osszeg / db
    return atlag

def listaAtlaga(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    atlag = osszeg / len(lista)
    return atlag
def main():
    lista1 = veletlenLista(13)
    print(veletlenLista)
    lista2 = veletlenLista(5)
    print(lista2)

    print("00-ra vegzodoek: ",negativ00raVegzodo(lista1))
    print("00-ra vegzodoek: ",negativ00raVegzodo(lista2))
    
    lista1atlaga = listaAtlaga(lista1)
    print("az első lista átlaga: ", lista1atlaga)
    print("a masodik lista pozitiv szamainak atlaga: ", pozitivSzamokAtlaga(lista1))

    print("az első lista átlaga: ",
          pozitivSzamokAtlaga(lista1))
    print("a masodik lista átlaga: ",
          pozitivSzamokAtlaga(lista2))
    maxIndexLista1 = maximumIndex(lista1)
    print("Első lista legnagyobb elem helye: ", maxIndexLista1+1)
main()