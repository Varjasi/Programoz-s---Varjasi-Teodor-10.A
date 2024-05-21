# 1. feladat
import random
listameret = int(input("Add meg a lista méretét [10..20]"))


elemek = []
index = 0
while index < listameret:
        számok = random.randint(1,5)
        if listameret < 20 and listameret > 10:              
            elemek.append(számok)
            index = index + 1
        else:
            print("Hibás érték! Próbáld meg újra!")
            listameret = int(input("Add meg a lista méretét [10..20]"))

print(f'A lista tartalma: {elemek}')

# 2. feladat

# Összegzés
összeg = 0
for i in elemek:
     összeg = összeg + i

print(f'A listában lévő elemek összege: {összeg}')

# Kiválasztás
maximum = elemek[0]
talalat = False
while not talalat:
    index2 = 0
    for g in elemek:
        if g > maximum:
            maximum = g
            talalat = True
            pozicio = index2
        index2 += 1

print(f'A listában lévő legnagyobb elem: {maximum}, helye: {pozicio}. pozíció')
