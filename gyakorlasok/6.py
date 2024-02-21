'''
# 1. feladat
import random
darab = 0
szam = int(input("Adj meg egy számot!"))
lista = []
while darab < 5:
    a = random.randint(1,7)
    lista.append(a)
    darab += 1
print(lista)

talalat = False
index = 0

while index < len(lista) and not talalat:
    if lista[index] == szam:
        talalat = True
    index = index + 1

if talalat:
    print("Az általad megadott szám előfordul a listában")
else:
    print("Az általad megadott szám nem fordul elő a listában")
'''
# 2. feladat

szo = 'almafa'
for betu in szo:
    print(betu)

a = input('Adj meg egy betűt')
index = 0
talalat = False
talalatdarab = 0
while index < len(szo) and a != '':
    if szo[index] == a:
        talalat = True
        talalatdarab += 1
    a = input("Add meg a következő betűt!")
    index += 1

if talalat:
    print("A megadott betű/betűk előfordul a szóban, a jó találatok száma:", talalatdarab)
else:
    print("A megadott betű/betűk nem fordul elő a szóban")
if index == 0:
    print("Nem adtál meg egy betűt sem!")