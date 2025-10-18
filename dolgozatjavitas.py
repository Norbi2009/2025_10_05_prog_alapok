import random

# 4. feladat

a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
print("Véletlen számok: ", a,b,c)
if(a != 0 and b != 0 and c != 0):
    harmonk = 3 / (1/a + 1/b + 1/c)
elif(a == 0 and b != 0 and c != 0):
    harmonk = 2 / (1/b + 1/c)
elif(b == 0 and a != 0 and c != 0):
    harmonk = 2 / (1/a + 1/c)
elif(c == 0 and a != 0 and b != 0):
    harmonk = 2 / (1/a + 1/b)
elif(a == 0 and b == 0 and c != 0):
    harmadik = 2 / (1/c)
elif(a == 0 and c == 0 and b != 0):
    harmadik = 2 / (1/b)
elif(c == 0 and b == 0 and a != 0):
    harmadik = 2 / (1/a)
else:
    print("nincs megoldás")
print("Harmonikus közép: ",round(harmonk,3))