import random

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
def main():
    lista1 = veletlenLista(13)
    print(veletlenLista)
    lista2 = veletlenLista(5)
    print(lista2)

    print("00-ra vegzodoek: ",negativ00reVegzodo(lista1))
    print("00-ra vegzodoek: ",negativ00reVegzodo(lista2))

main()