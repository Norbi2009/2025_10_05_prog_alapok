import random as r


szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    print(karakter,end=" ")

print()


for index in range(0, len(szoveg)-3, 1):
    print(szoveg[index]+",",end=" ")

print(szoveg[-3])