# Generáljon ki 3 véletlen háromjegyű számot amelyek 13-mal oszthatók
# állítsa ezeket sorrendbe
# adja meg az átlagukat
# van-e közöttük 4-el végződő?

import math
import random

valid_numbers = list(range(-999, -99)) + list(range(100, 1000))
a = random.choice(valid_numbers)
print(a)