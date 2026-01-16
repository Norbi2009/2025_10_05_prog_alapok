"""
Függvények
(scratch Blokkok)

előre definiált (megírt, megfogalmazott) folyamatok, amik külső értéktől függően, végrehajtják a belső utasításokat!

def fuggvenyNev():
    #Függvény tartalma

fuggvenyNev() # függvény meghívása
"""
# osszeadas fuggveny definialasa
def osszeadas():
    a = 12
    b = 17
    print(a+b)

# osszeadas kulso ertektol fuggen PARAMETEREN keresztul
def osszeadasParam(a,b):
    c = a + b
    print(c)

#osszeadas fuggveny meghivasa
osszeadas()
osszeadasParam(12,17)

# Visszatéréssel rendelkező függvények
def kettoAtizediken():
    # a = math.pow(2,10)
    a = 2**10
    return a

valtozo = kettoAtizediken()
print(valtozo)

def osszeadasVisszateressel(a,b):
    c = a + b
    return c

print(osszeadasVisszateressel(13,17))




import random

def veletlenszamKiiratas(db):
    for i in range(0,db,1):
        print(random.randint(100,999),end=" ")
    print()
veletlenszamKiiratas(5)


def szovegVisszafele(szoveg):
    for i in range(len(szoveg)-1,-1,-1):
        print(szoveg[i],end="")
    print()

szovegVisszafele("kalapács")


def szovegVisszafeleFv(szoveg):
    visszaSzoveg = ""
    for i in range(len(szoveg)-1,-1,-1):
        visszaSzoveg += szoveg[i]
    return visszaSzoveg
    print()

print(szovegVisszafeleFv("kalapács"))

# Írjon egy függvényt ami egy beküldött szóról eldönti, hogy palindrom-e és visszaadja válaszul?(Visszafele is ugyan az a szó)

def szovegPalindrom(szo):
    # i = 0
    # while(i <= len(szo) // 2 and szo[i] == szo[len(szo)-1-i]):
    #     i+=1
    # if(i>len(szo) // 2):
    #     return "palindrom"
    # else:
    #     return "nem palindrom"
    if(szo == szovegVisszafeleFv(szo)):
        return True
    else:
        return False
print("palindom-e a szó: ",szovegPalindrom("abba"))