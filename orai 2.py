# Generáljon ki 3 véletlen háromjegyű számot amelyek 13-mal oszthatók
# állítsa ezeket sorrendbe
# adja meg az átlagukat
# van-e közöttük 4-el végződő?

import math
import random

# 100 / 13 = 7,6
# 999 / 13 = 78,8

a = random.randint(8,76)*13
b = random.randint(8,76)*13
c = random.randint(8,76)*13

szamjegy = int(input("adjon meg egy számjegyet: "))

print(a,b,c)

a = 130
b = 403
c = 624

if(a % 10 == szamjegy or b % 10 == szamjegy or c % 10 == szamjegy):
    print("Van közte "+str(szamjegy)+"-re végződő")
else:
    print("nincs közte "+str(szamjegy)+"-re végződő")
