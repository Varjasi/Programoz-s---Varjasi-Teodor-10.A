'''
def osszegzo(x, y):
    osszeg = x + y
    return(osszeg)

a = int(input("Adj meg egy számot"))
b = int(input("Adj meg még egy számot"))
print(osszegzo(a, b))
'''
# Van-e práos szám?

def paros_e(lista):
    talalat = False
    index = 0
    while index < len(lista) and not talalat:
        if lista[index]%2==0:
            talalat = True
        index += 1
    if talalat:
        return("A listában van páros szám")
    else:
        return("A listában nem található páros szám")

import random

szamok = []
db = 0
while db < 3:
    szam2 = 3
    szam = random.randint(1,50)
    szamok.append(szam)
    db += 1

print(szamok)
print(paros_e(szamok))
        