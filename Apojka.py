
def beolvasas():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(" ")
        lista.append((int(st[0]),int(st[1]),int(st[2])))
    return lista
def osszegzes(lista):
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i][2]
    return osszeg
def maxe(lista):
    maxe = 0
    for i in range(len(lista)):
        if(lista[i][2]> maxe):
            maxe = lista[i][2]
    return maxe
def maxi(lista):
    maxi = 0
    for i in range(len(lista)):
        if(lista[i][2] > lista[maxi][2]):
            maxi = i
    return maxi
def main():
    lista = beolvasas()
    print(lista,end=" ")
    print(osszegzes(lista))
    print(maxe(lista))
    print(maxi(lista))
main()