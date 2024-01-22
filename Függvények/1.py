'''
def szorzas(x, y):
    return 3*x, 3*y

print(szorzas(2,3))

a = int(input("adj meg egy számot"))
b = int(input("Adj meg még egy számot"))

print(szorzas(a,b))
'''
'''
a = False
def paros_e(x, y):
    return x, y
    if x%2==0 and y%2==0:
        return True
    else:
        return False
    
print(paros_e(y = 2, x=4))
'''
'''
import math
def ki(x:any):
    print(x)
    return
x = ki("Géza")

if x==None:
    print("nem volt visszatérési érték")

#Másodfokú megoldóképlet

 
def masodfoku(a:float,b:float,c:float):
    
    Másodfokú megoldóképlet
    return -1 : a=0
    if a==0:
        return

    diszkrinimans = b**2-4*a*c
    if diszkrinimans<0:
        return
    
    x1 = (-b +math.sqrt(diszkrinimans)  / (2*a))
    x2 = (-b + math.sqrt(diszkrinimans) / (2*a))
    return(x1, x2)

x = masodfoku(1,3,1)

if x == -1:
    print("Az a értéke 0 volt-")

if x == -2:
    print("A diszkrinimáns kisebb, mint 0.")

if type(x) == type((3, 2)):
    print("2 zérushelyünk van")

class A_NULLA:
    pass
class DISZKRINIMANS_KISEBB_NULLÁNÁL:
    pass

print("valami")
'''
'''
#Összegzés tétel
def osszegzes_tetel(l):
    s = 0
    for i in range(len(l)):
        s+=l[i]
    return(s)

print(osszegzes_tetel([2,3,4]))

#Eldöntés, Keresés, Kiválasztás

def eldontes(a:list):
    talalat = False
    index = 0
    while index < len(a) and not talalat:
        if a[index] % 3 == 0:
            talalat = True
        index += 1
    if talalat:
        return("A listában található 3-mal osztható szám")
    else:
        return("A listában nem található 3-mal osztható szám")

print(eldontes([4, 7]))


def kereses(a:list):
    talalat = False
    index = 0
    while index < len(a) and not talalat:
        if a[index] % 3 == 0:
            talalat = True
        index += 1
    if talalat:
        return("A listában található 3-mal osztható szám, az indexe:", index-1)
    else:
        return("A listában nem található 3-mal osztható szám")

print(kereses([4, 7, 3]))
'''
def kivalasztas(a:list):
    talalat = False
    index = 0
    while not talalat:
        if a[index] % 3 == 0:
            talalat = True
        index += 1
    if talalat:
        return("A listában található 3-mal osztható szám indexe:", index-1)
    else:
        return("A listában nem található 3-mal osztható szám")

print(kivalasztas([4, 7, 3]))

# Számlálás
darab = 0
def szamlalas(a:list):
    for i in a:
        if i % 3 == 0:
            darab += 1
    return("A listában")

