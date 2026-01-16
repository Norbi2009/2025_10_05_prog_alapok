#Készítsen egy függvényt, ami egy db számtól függ és visszaad egy feltöltött listát [-10,50] közötti számokkal!
#Készíts egy függvényt, ami bármlyen lista elemeit megvizsgálva visszaadja, hogy hány db pozitiv szam van!
import random


def listafeltolt(db):
    lista = []
    for i in range(0,db,1):
        szam = random.randint(-10,50)
        lista.append(szam)
    return lista

def pozitivDb(szamoklista):
    darab = 0
    for i in range(0,len(szamoklista),1):
        if(szamoklista[i]>0):
            darab += 1
return darab

def main():
    lista = listafeltolt(13)
    print(lista)
    print(pozitivDb(lista))

main()
