# Generálj ki egy páros véletlen számot [-10, 10] között!
# írasd ki az adott számot

import random
import math

a = random.randint(-5,5)*2 
print("szám:"+ str(a))

# vegyük a szám abszolút értékét
# ha a szám negatív akkor szám*(-1) kölünben önmaga
if a<0 :
    print("abs:" + str(a*(-1)))
else:
    print("abs:" + str(a))

# irassa ki a szám gyökét

if(a >=0 ):
    print("gyök(a): "+str(math.sqrt(a)))
else:
    print("A negatív számnak nincs gyöke.")

if(a>0) :
    print("pozitív")
else: 
    if(a==0):
        print("nulla")
    else:
        print("negatív")


# Felhsználótól bekérés

# szoveg = input("Adjon meg egy számot: ")
# print(szoveg)

# HF 8-13 

# Sekvencia - utasítások sorozata
# Szelekció - Elágazás
# Iteráció - Ciklus, ismétlés

# HF megoldás

sec = 3923
# 1 óra 5 perc 23 másodperc
# 3600 + 300 + 23 = 3923
# szoveg = input("Adjon meg egy időpontot: ")
# print(szoveg)
ora = sec // 3600
perc = (sec - ora * 3600) // 60
# mp = (sec - ora * 3600) - (perc *60)
mp = sec % 60
print(ora, "óra")
print(perc, "perc")
print(mp, "másodperc")