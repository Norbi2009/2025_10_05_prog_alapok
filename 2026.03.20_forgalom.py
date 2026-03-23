def fajlBeolvasas():
    f = open("txt adatok/forgalom.txt","r",encoding = "utf-8")
    elsoSor = f.readline()
    sorok = f.readlines()
    # print(sorok)
    t = []
    for sor in sorok:
        st = sor.strip().split(" ")
        t.append((int(st[0]),int(st[1]),int(st[2]),int(st[3]),st[4]))

    f.close()
    return t, elsoSor


def main():
    adatok = fajlBeolvasas()
    t = adatok[0]
    elsoSor = adatok[1]

main()