# # Egy soros komment
# """
# Több soros komment
# !!!!!
# """

# #ctrl + ü a kijelölt sorok kommentelése

# # kód kód
# # kód kód
# # kód kód
# # hiba kód

# print ("Szöveg kiiratása", "Másik szöveg kiiratása", end="-*-*-*-*")
# print("Szabo Daniel", end="@@@@@")
# print("10.b", end="----")
# print("2025.09.07", end="+++++")
# print()
# print("alma", "körte", "szilva", "labda", sep="___")

# # Jelenítsd meg a következő ábrát a terminálon:
# #*
# #**
# #***
# #****
# #*****
# #1. egy print utasítással!
# print("*", "**", "***", "****", "*****", sep="\n")
# print()
# #2. több print utasítással és csak end tuljadonság lehet benne!
# print(end="*\n")
# print(end="**\n")
# print(end="***\n")
# print(end="****\n")
# print(end="******\n")

import math

szam = int(input("adj meg egy számot: "))
print (szam)

if szam % 10 == 0:
    print("osztható tízzel")
else:
    print("nem osztható")
    