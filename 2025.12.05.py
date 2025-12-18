"""
lista - dinamikus
- tudunk bele uj elemet rakni, ezzel nő az elemszáma
- tudunk belole torolni ezzel csokken az elemszama
- lekerheto barmelyik eleme
- modosithato barmelyik eleme
deklarálás (valtozo letrehozasa):
lista_neve = []
lista_neve.append(ujelem)
elem torlese:
lista_neve.remove(elem)
beégetett lista:
lista_neve = [3,2,5,7,1]
lista hossza:
len(lista_neve)
"""
# szamok = [3,2,5,7,1]
# print(szamok)
# szamok.append(12)
# print(szamok)
# szamok.remove(3)
# print(szamok)
# print("első elem:", szamok[0])
# print("Lista hossza: " ,len(szamok))
# print("utolsó elem:", szamok[len(szamok)-1])

# hf:
# tolts fel egy 13 elemu listat[0,20] kozotti veletlen szammal
# szamok atlaga
# hany db paros szam van a listaban
# van-e benne nulla

import random

# 1.
# lista = [random.randint(0, 20) for _ in range(0,13,1)]
# print("Lista:", lista)

# # 2.
# atlag = sum(lista) / len(lista)
# print("Átlag:", atlag)

# # 3.
# paros_db = sum(1 for x in lista if x % 2 == 0)
# print("Páros számok darabszáma:", paros_db)

# # 4.
# if 0 in lista:
#     print("Van benne nulla")
# else:
#     print("Nincs benne nulla")


n = 13

lista = []

for index in range(0,n,1):
    a = random.randint(0,20)
    lista.append(a)
print(lista)

osszeg = 0
for inex in range(0,len(lista),1):
    osszeg += lista[index]
print(osszeg)