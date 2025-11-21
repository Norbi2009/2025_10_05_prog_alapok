#1
import random 
import math

#a
vszam1 = random.randint(10,99)
print("a véletlen szám:")
print(vszam1)


print()

#b
szam = random.randint(100,999)
print("a számok: ")
for szam in range(0, vszam1, 1):
    print(szam, end=" ")

for szam in range(vszam1, vszam1, 3):
    print(szam, end=" ")


print()


#2 
print()

szoveg = input("jó reggelt")
print(szoveg)
# for szoveg in range(szoveg):
#     print(szoveg)