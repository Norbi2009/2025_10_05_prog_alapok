import random 
import math

# 1.a
velszam = random.randint(10,99)
print(velszam)


# 1.b
db = 0
for haromjegyu in range(0,velszam,1):
    haromjegyu = random.randint(100,999)
    if(haromjegyu % 3 == 0):
        db+=1
    print(haromjegyu,end=" ")
print()
print(db)
print(round(math.sqrt(osszeg), 2))


# 2.feladat
szoveg = input("Adjon meg egy szöveget: ")
len(szoveg) = hossz
if( hossz % 2 == 0):
    index = hossz//2
    print(szoveg[index])
else:
    index1 = hossz//2
    index2 = hossz//2-1
    print(szoveg[index1], szoveg[index2])

for ix in range(0,hossz,2):
print(szoveg[ix],end="$")