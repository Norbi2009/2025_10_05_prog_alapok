# Generáljon egy listába 13  db olyan négyjegyű véletlen számokat amik 3,5,7-re végződnek!
# Hány db 3-ra, 5-re és 7-re végződő szám van?
import random

lista = []

for i in range(0,13,1):
    valtozo = random.randint(100,999)
    veletlen = random.randint(1,3)
    if(veletlen == 1):
        lista.append(valtozo*10+3)
    elif(veletlen == 2):
        lista.append(valtozo*10+5)
    else:
        lista.append(valtozo*10+7)
print(lista)

haromra = 0
otre = 0
hetre = 0
for i in range(0,len(lista),1):
    if(lista[i] % 10 == 3):
        haromra += 1
    elif(lista[i] % 10 == 5):
        otre += 1
    else:
        hetre += 1
print("ötre: ", otre)
print("háromra végződő: ", haromra)
print("hétre: ",hetre)

# otre = 0
# for i in range(0,len(lista),1):
#     if(lista[i] % 10 == 5):
#         otre += 1
# print(otre)

# hetre = 0
# for i in range(0,len(lista),1):
#     if(lista[i] % 10 == 7):
#         hetre += 1
# print(hetre)

# számtani átlag
# hány db szám van átlag alatt
# mértani átlag
#a mértani átlag alatti számok összege
# 30db 13, 17-re végződő számokkal, hány osztható 13-mal és 17-tel
# bekérsz egy hosszabb szöveget, hány db felhasználó által megadott beű van benne?
# bekérsz 2 szót, mnd meg adott indexen hany db betu elteres van! (pl. alma, alkat -> 2 db kulünbség)
