import math

def prime(szam):
    a = 2
    b = math.sqrt(szam)
    while(a<b and szam % a != 0):
        a += 1
    return a>=b

# def lnko(szam1,szam2):
#     kisebb = szam1
#     if(szam1>szam2):
#         kisebb = szam2
#     while(kisebb>=1 and not(szam1 % kisebb == 0 and szam2 % kisebb == 0)):
#         kisebb-=1
#     return kisebb

def lnko(a,b):
    if a == b:
        return a
    if b < a:
        c = a
        a = b
        b = c
    while (0 < a):
        a, b = b % a, a
    return b



def main():
    a = 28
    b = 31
    # for i in range(2,1000000,1):
    #     if prime(i):
    #         print(i)
    #print(prime(a)) # a=13 true
    #print(LNKO(a,b)) # a=13, b=26 LNKO=13
    print(prime(a))
    print(lnko(a,b))
main()

