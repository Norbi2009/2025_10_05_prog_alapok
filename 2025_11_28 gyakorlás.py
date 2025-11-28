# Egy szövegben hány db szóköz van?

szoveg = "Géza kék az ég"
db = 0

for karakter in szoveg:
    if(karakter == " "):
        db += 1

print(db ,"Ennyi db szóköz van a szövegben.")


#Adja meg hogy a szovegben van-e cs betű (ketto karakter egymas mellett)
# pl alma, kacsa, filc

sz = input("Ajon meg egy szöveget: ")
index = 0
while(index<len(sz)-1 and (sz[index] != "c" or sz[index+1] != "s")):
    index += 1

if(index <len(sz)-1):
    print("Van benne cs")
else: 
    print("Nincs benne cs") 



#De Morgan azonosság