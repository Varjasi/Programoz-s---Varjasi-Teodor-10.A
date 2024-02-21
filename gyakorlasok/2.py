# Összegzés
#1. feladat
'''
import random
darab = 0
lista = []
while darab < 5:
    a = random.randint(1,10)
    if a % 2 == 0:
        lista.append(a)
    darab += 1
print (lista)

összeg = 0
index = 0
while index < len(lista):
    összeg = lista[index] + összeg
    index += 1
print(f'A listában található számok összege {összeg}')
'''
'''
#2. feladat
a = int(input("Adj meg egész számokat -5 és 5 közötti intervallumokban. Ha nem akarsz több számot megadni, írj 0-át vagy pedig adj meg értelmezési tartomáynon kívül seő értéket"))
összeg = 0
while a >= -5 and a <= 5 and a != 0:
    összeg = összeg + a
    a = int(input("Add meg a következő számot"))
if a ==  0:
    print("Nem adtál meg egy számot sem!")
else:    
    print("Az általad megadott számoknak az összege", összeg)
'''

# Eldöntés
#1. feladat
'''
import random
lista = []
db = 0
while db < 5:
    a = random.randint(1,7)
    lista.append(a)
    db += 1
print(lista)
talalat = False
b = int(input("Adj meg egy számot!"))
index = 0
while index < len(lista) and not talalat:
    if lista[index] == b:
        talalat = True
    index = index + 1
if talalat:
    print("A megadott szám előfordul a listában")
else:
    print("A megadott szám nem fordul elő a listában!")
'''
'''
szo = 'alma'
print(szo)

a = input("Adj meg egy betűt!")
index = 0
talalat = False
talalatdb = 0
rossztalalatok = 0
while a != '':
    if szo[index] == a:
        talalatdb += 1
        talalat = True
        a = input("Adj meg a következő betűt!")
    else:
        a = input("Adj meg a következő betűt!")
        rossztalalatok = rossztalalatok + 1

if talalat:
    print(f'Az általad megadott betű előfurdul a szóban, jó találataid száma eddig: {talalatdb}, rossz találataid pedig {rossztalalatok}')
else:
    print("Az általad megadott betű nem fordul elő a szóban")
'''

'''
    A SZÁMLÁLÁS esetében azt vizsgáljuk, hogy egy bizonyos tulajdonságú elemből 
    hány darab van az adatsorban (itt a listában).

    A program azt vizsgálja, hogy hány darab hárommal osztható szám van a listában.
    '''
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]
darab = 0
for szam in lista:
    if szam % 3 == 0:
        darab += 1
print(f'A listában {darab} db hárommal osztható szám található')
'''
'''
# Számlálás
# 1. feladat
import random
darab = 0
lista = []
while darab < 5:
    a = random.randint(1,10)
    lista.append(a)
    darab += 1
print(lista)

talalat = 0
for szam in lista:
    if szam % 2 == 0:
        talalat += 1
print(f'A listában {talalat} db páros szám található')
'''
'''
    A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
    illetve a legnagyobb érték az adatsorban (itt a listában).
    '''
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

legkisebb = lista[0]
legnagyobb = lista[0]

for szam in lista:
    if szam < legkisebb:
        legkisebb = szam
    if szam > legnagyobb:
        legnagyobb = szam
print(f'A lista legkissebb száma: {legkisebb}, míg a lista legnagyobb száma {legnagyobb}')
'''
# Szélsőérték meghatározása

lista = []
a = input("Add meg az első számot!")
while a != '*':
    lista.append(a)
    a = input("Add meg a következő számot!")
legkisebb = lista[0]
legnagyobb = lista[0]

for szam in lista:
    if szam < legkisebb:
        if szam / 2 == 0:
            legkisebb = szam
        
print(', ' .join(lista))
print (f'A listában található legkissebb szám: {legkisebb}')