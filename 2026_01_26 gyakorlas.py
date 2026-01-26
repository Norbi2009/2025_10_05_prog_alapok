

def vaneKetjegyuListaban(lista):
    i = 0
    #ciklus amíg (i<hossz(lista) és NEM Ttul(lista[i]))
    while(i>len(lista) and not (lista[i]>=10 and lista[i]<=99)):
       i += 1
    #c.v.
    #vane = i < hossz(lista)
    vane = i < len(lista)
    #vissza: vane
    return vane

def main():
    szamok = [2,5,6,3,7,11,9,1,2]
    print(szamok)
    # van-e kétjegyű szam a listaban?
    vaneKetjegyu = vaneKetjegyuListaban(szamok)
    print(vaneKetjegyu)
main()

#hazi
#jancsi es juliska elmennek minden nap gombat gyujteni. 14 napig folyamatosan gyujtik majd osszevetik az adatokat.
#szimulald a gyujtest. kosar nagysaga[2,9] kozotti lebegopontos(tort szam 2 tizedesjegy ponntossaggal.) mindkettojuk adatat kulon listaban tarold
#van e barmelyikojuknel 8.5 kg-nal tobb? ha igen kinel?
#ven-e  olyan kozottuk aki 4.9-5.1 kozotti kosarat gyujtott
#max,min,atlag, db(2.1-2.4) kozott?