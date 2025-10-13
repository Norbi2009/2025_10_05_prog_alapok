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













# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan

szam1 = int(input("Adjon meg egy egész számot: "))

if(szam1 % 2 == 0):
    print("páros")
else:
    print("páratlan")

# kérjen be a felhasználótól egy számot és mondja meg hogy 10-zel osztható -e? Ha nem osztható 10-zel írja ki hoy utolsó szémjegyét!
# pl. be: 10 ki: tízzel osztható
# pl. be: 12 ki: tízzel nem osztható, utolsó számjegy 2

szam2 = int(input("Adjon meg egy 2. egész számot: "))

if(szam2 % 10 == 0):
    print("osztható")
else:
    print("nem osztható")
    print("az utolsó számjegy " + str (szam2 % 10))


# Kérjen be egy másik számot és írassa ki a két szám reciprokának összegét

szam3 = int(input("Adjon meg egy 3. egész számot is: "))
reciprok_osszeg = (1/szam2) + (1/szam3)

if(szam2 != 0):
    if(szam3 !=0):
        rec2 = 1/szam2
        rec3= 1/szam3
        print(rec2+rec3)
    else: print("a második számnak nincs reciproka")

print("A két szám reciprokának összege: ", reciprok_osszeg)

# Adja meg a két szám összegének a gyökét
if (szam2 + szam3 >=0):
    print(math.sqrt(szam2+szam3))
else:
    print("A 2 szám összege negatív")

# Logiaki operátorok
# and, or, xor, !(not)
if(szam2 != 0 and szam3 != 0):
    rec = 1/szam2
    rec2 = 1/szam3
    print(rec+rec2)
else:
    print("A két szám valamelyik nulla!")

# HF: bool algebra
# HF: Kérjen be a felhasználótól 3db számot (lehet tört is). Ez a három szám egy háromszög három oldala
#1. Derékszögű-e a háromszög?
#2. Egyenlőszárú-e a háromszög?
#3. Szabályos-e a háromszög? 

szam1 = random.randint(100, 999)
szam2 = random.randint(100, 999)
szam3 = random.randint(100, 999)

szamok = [szam1, szam2, szam3]

for i in range(3):
    if szamok[i] % 13 != 0:
        print(f"A(z) {szamok[i]} szám nem osztható 13-mal.")
    else:
        print(f"A(z) {szamok[i]} szám osztható 13-mal.")

atlag = sum(szamok) / 3
print("A számok átlaga:", atlag)

szamok.sort()
print("Sorrendbe állítva:", szamok)

van_4 = False
for sz in szamok:
    if sz % 10 == 4:
        van_4 = True
        break

if van_4:
    print("Van köztük 4-re végződő szám.")
else:
    print("Nincs köztük 4-re végződő szám.")
