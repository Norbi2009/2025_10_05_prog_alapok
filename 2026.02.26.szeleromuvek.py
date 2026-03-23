def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),int(st[4]),int(st[5])))
    return lista

def szerelomuvekDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i][3]
    return osszeg

def maximumIndexDb(lista):
    maxi = 0
    for i in range(1,len(lista)-1,1):
        if(lista[i][3]>lista[maxi][3]):
            maxi = i
    return maxi

def vaneSzeleromuVarosban(lista, varos):
    i = 0
    while(i<len(lista) and lista[i][0] != varos):
        i += 1
    vane = i<len(lista)
    return vane


def main():
    t = adatokBeolvasasa()

    db = szerelomuvekDarab(t)
    print(db)

    maxindex = maximumIndexDb(t)
    print( t[maxindex][0], "város",t[maxindex][5],"évében csinálták egyszerre a legtobb szélerőművet.")

    varos = input("Adjon meg egy várost: ")
    vane = vaneSzeleromuVarosban(t,varos)
    if(vane):
        print("Ebben a varosban van szélerőmű.")
    else:
        print("Ebben a varosban nincs szélerőmű.")

main()