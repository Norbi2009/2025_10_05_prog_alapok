# Jancsi és Juliska autós kártyát gyűjtenek. Hogy ne legyen vita és gyorsan meg tudják különböztetni melyik autó kié, ezért a következőt találták ki.
# Mivel minden autó végsebessége 3 jegyű, ezért megnézik a középső számot. Ha páros akkor Jancsié, ha páratlan akkor Juliskáé. 
# Van összesen 30 kártyájuk. Szeretik egymás mellé rakni a kártyákat. Szimuláld a feladatot!
# Írj egy programot, ami kigenerál [300, 499] között egy számot úgy, hogy minden páros helyen Jancsi kártyája van, minden páratlan helyen Juliskáé!
import random

lista = []
for i in range(0,30,1):
    elso = random.randint(3,4)
    masodik = -1
    if(i % 2 == 1):  #Jancsi száma
        masodik = random.randint(0,4)*2
    else:  #Juliska száma
        masodik = random.randint(0,4)*2+1
    harmadik = random.randint(0,9)
    szam = int(str(elso)+str(masodik)+str(harmadik))
    szam = elso * 100 + masodik * 10 + harmadik
    lista.append(szam)
print(lista)


# Add meg Jancsi autóinak végsebességének átlagát!
# Add meg hány darab autója van Juliskának, ami 380-nál nagyobb a végsebessége!


osszeg = 0
for i in range(1,len(lista),2):
    # print(lista[i])
    osszeg += lista[i]

db = len(lista)/2
atlag = osszeg / db
print("Jancsi autóinak végsebességének átlaga:", round(atlag,2))

db_juliska = 0
for i in range(0,len(lista),2):
    if(lista[i] > 380):
        db_juliska += 1
print("Juliskának", db_juliska, "db autója van, ami 380-nál gyorsabb")