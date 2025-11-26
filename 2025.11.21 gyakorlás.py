#1 Kérjen be egy szöveg és egy betűt!
#2 Nézze meg van-e  a szövegben az adott betű, ha van..
#3 Adja meg hány darab betű van a szövegben!

szoveg = input("Adjon meg egy szöveget: ")
print()
betu = input("Adjon meg egy betűt: ")
print()

index = 0
while(index < len(szoveg) and szoveg[index] != betu):
    index += 1
print(index)

if(index < len(szoveg)):

    db = 0
    for karakter in szoveg: 
        if(karakter == betu):
            db+=1
print(db)
