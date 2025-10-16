import random


# # lebegőpontos - float - tört
# a = 1.25
# b = float(input("adjon meg egy tizedes törtet: "))
# print(b*4)

# generáljon ki [1,10[ közötti tört számot 2 tizedesjegyre
# pl. 1.36, 2.30

# c = random.randint(100,999)/100
# c = random.random() #[0,1˙[
# print(round(c,2))   #HF befejezni

# Szövegkezelés
# szoveg = input("adjon meg egy szöveget: ")
# print(szoveg)
# print("Szöveg hossza: ", len(szoveg))
# print("első karakter" ,szoveg[0])
# # szöveg karakterekből épül fel
# # szöveg = karakter lánc
# karakter = szoveg[0]
# kod = ord(szoveg[0])
# print(kod)
# ujkod = kod + 1
# ujkarakter = chr(ujkod)
# print(ujkarakter)

# a = chr(random.randint(97,122))
# b = chr(random.randint(97,122))
# c = chr(random.randint(97,122))
# print(a,b,c,)



# Kérje be a felhasználó keresztnevét! Generáljon neki egy jelszót, az első 3 karakterének ascii kódjának szorzatát!
#  Ha nincs a név 3 jegyű, akkor kettő esetén a hossz érték legyen a szorzat3. tagja 1 esetén pedig a  szám köbe leygyen
# Alma - 65 * 108 * 109
# Co - 67 * 111 * 2
#G - 71 * 71 * 71

szoveg = input("Adja meg a keresztnevét: ")
hossz = len(szoveg)

if hossz >= 3:
    jelszo = ord(szoveg[0]) * ord(szoveg[1]) * ord(szoveg[2])
else:
    if hossz == 2:
        jelszo = ord(szoveg[0]) * ord(szoveg[1]) * hossz
    else:
        jelszo = ord(szoveg[0]) ** 3

print(f"A generált jelszavad: {jelszo}")

