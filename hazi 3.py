# HF: Kérjen be a felhasználótól 3db számot (lehet tört is). Ez a három szám egy háromszög három oldala
#1. Derékszögű-e a háromszög?
#2. Egyenlőszárú-e a háromszög?
#3. Szabályos-e a háromszög?


import math

a = int(input("Add meg az első oldalt: "))
b = int(input("Add meg a második oldalt: "))
c = int(input("Add meg a harmadik oldalt: "))

if (round(a**2 + b**2, 5) == round(c**2, 5)) or \
   (round(a**2 + c**2, 5) == round(b**2, 5)) or \
   (round(b**2 + c**2, 5) == round(a**2, 5)):
    print("Derékszögű háromszög")
else:
    print("Nem derékszögű háromszög")

if a == b or a == c or b == c:
    print("Egyenlő szárú háromszög")
else:
    print("Nem egyenlő szárú háromszög")

if a == b and b == c:
    print("Szabályos háromszög")
else:
    print("Nem szabályos háromszög")

szam1 = int(input("Adjon meg egy egész számot: "))

if szam1 % 2 == 0:
    print("páros")
else:
    print("páratlan")

szam2 = int(input("Adjon meg egy 2. egész számot: "))

if szam2 % 10 == 0:
    print("tízzel osztható")
else:
    print("tízzel nem osztható, utolsó számjegy:", szam2 % 10)

szam3 = int(input("Adjon meg egy 3. egész számot is: "))

if szam2 != 0 and szam3 != 0:
    rec2 = 1 / szam2
    rec3 = 1 / szam3
    print("A két szám reciprokának összege:", rec2 + rec3)
else:
    if szam2 == 0:
        print("A második számnak nincs reciproka (0)")
    if szam3 == 0:
        print("A harmadik számnak nincs reciproka (0)")

osszeg = szam2 + szam3
if osszeg >= 0:
    print("A két szám összegének gyöke:", math.sqrt(osszeg))
else:
    print("A két szám összege negatív, nincs valós gyöke.")
