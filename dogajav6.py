def adatokFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),st[4]))
    return lista

def main():
    adatok = adatokFeltoltes
    print(adatok)
main()