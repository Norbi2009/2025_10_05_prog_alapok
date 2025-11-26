import random
import math

# 1.a
velszam = random.randint(10, 99)
print(velszam)

# 1.b
db = 0
osszeg = 0
for szamlalo in range(velszam):
    haromjegyu = random.randint(100, 999)
    if haromjegyu % 3 == 0:
        db += 1
    osszeg += haromjegyu
    print(haromjegyu, end=" ")

print()
print(db)
print(round(math.sqrt(osszeg), 2))

# 2. feladat
szoveg = input("Adjon meg egy szöveget: ")
hossz = len(szoveg)

if hossz % 2 == 1:  # páratlan hossz → van középső
    index = hossz // 2
    print(szoveg[index])
else:               # páros hossz → két középső
    index1 = hossz // 2 - 1
    index2 = hossz // 2
    print(szoveg[index1], szoveg[index2])

for ix in range(0, hossz, 2):
    print(szoveg[ix], end="$")
