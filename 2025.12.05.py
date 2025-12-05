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
szamok = [3,2,5,7,1]
print(szamok)
szamok.append(12)
print(szamok)
szamok.remove(3)
print(szamok)
print("első elem:", szamok[0])
print("Lista hossza: " ,len(szamok))
print("utolsó elem:", szamok[len(szamok)-1])

# hf:
# tolts fel egy 13 elemu listat[0,20] kozotti veletlen szammal
# szamok atlaga
# hany db paros szam van a listaban
# van-e benne nulla

