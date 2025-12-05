# Egy szövegben hány db szóköz van?

# szoveg = "Géza kék az ég"
# db = 0

# for karakter in szoveg:
#     if(karakter == " "):
#         db += 1

# print(db ,"Ennyi db szóköz van a szövegben.")


# #Adja meg hogy a szovegben van-e cs betű (ketto karakter egymas mellett)
# # pl alma, kacsa, filc

# sz = input("Ajon meg egy szöveget: ")
# index = 0
# while(index<len(sz)-1 and (sz[index] != "c" or sz[index+1] != "s")):
#     index += 1

# if(index <len(sz)-1):
#     print("Van benne cs")
# else: 
    # print("Nincs benne cs") 



#De Morgan azonosság

#van-e a szövegben sz betű?

szoveg = "apa"
dube = "cs"
print(szoveg)

# if "sz" in szoveg:
#     print("Van benne")
# else:
#     print("Nincs benne")


index = 0
while(index <len(szoveg)-1 and not(szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index+=1
if(index<len(szoveg)-1):
    print("benne van a/az",dube,"betű")
else:
    print("nincs benne a/az",dube,"betű")


# palindrom-e
ujszoveg = ""
for index in range(len(szoveg) -1, -1, -1):
    ujszoveg += szoveg[index]
if(ujszoveg == szoveg):
    print("A szöveg palindrom")
else:
    print("A szöveg nem palindrom")


j = 0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-j-1]):
    j+=1
if(j<len(szoveg)/2):
    print("A szöveg nem palindrom")
else:
    print("A szöveg palindrom")