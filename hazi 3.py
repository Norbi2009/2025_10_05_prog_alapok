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

# HF: python - ciklusok, loop, interációk,...