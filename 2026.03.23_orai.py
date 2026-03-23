def fajlBeolvasas():
    fajl = open("txt adatok/resztvevok.txt","r",encoding = "UTF-8")
    elsoSor = fajl.readline().strip()
    sorok = fajl.readlines()
    t = []
    for sor in sorok:
        sor = sor.strip().split(';')
        t.append((sor[0], sor[1], sor[2], int(sor[3]), sor[4]))
    fajl.close()
    return t, elsoSor




def main():
    t = fajlBeolvasas()
    print(fajlBeolvasas())

main()