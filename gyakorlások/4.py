#1. Feladat
import random
darab = 0
lista = []
while darab < 5:
    a = random.randint(1,10)
    if a % 2 == 0:
        lista.append(a)
    darab += 1
print (lista)

osszeg = 0
for szam in lista:
    osszeg = osszeg + szam
print (osszeg)