import random

gondolt_szam = random.randint(10,99)

print("Melyik kétjegyű számra gondoltam?")
szam = int(input("Szám: "))

while(szam != gondolt_szam):
    if(szam > gondolt_szam):
        print("A szám nagyobb mint a gondolt szám.")
    elif(szam < gondolt_szam):
        print("A szám kisebb mint a gondolt szám.")
    else:
        print("Eltaláltad")
    szam = int(input("Probálkozz még egyszer: "))

# Írassa ki hany db probalkozas volt!
# Figyeljen arra hogyha nem kétjegyű számot adott meg, az ne legyen új próbálkozás, és figyelmeztesse a felhasználót!
# Minden szám bekérésénél írja ki az aktuális próbálkozások számát!