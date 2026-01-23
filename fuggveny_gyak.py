#irjon egy fuggvenyt ami visszaadja a  listak terjedelmet. Terjedelem = maximum-minimum
import random
def maximumErtek(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1): # = 1-től (n-1)-ig egyesével
        if(lista[i]>maxe):
            maxe = lista[i]
    #e.v.
    #c.v.
    #vissza: maxe
    #pr.v.
    return maxe

lista = [3,5,7,3,4,5,6]
print(maximumErtek(lista))