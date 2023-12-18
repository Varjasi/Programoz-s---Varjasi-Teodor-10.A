# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="input.txt"

file=open(filename, "r")
file_lista=file.readlines()
file.close()

name_list=[]
pancake_list=[]
for i in range(len(file_lista)):
    _lista=file_lista[i].strip()
    _lista_parts=_lista.split()

    # így is lehet: _lista_parts=file_lista[i].strip().split()
    name_list.append(_lista_parts[0])

    _l=[]
    for j in range(1,len(_lista_parts)):
        _l.append(int(_lista_parts[j]))
    pancake_list.append(_l)

print(name_list)

print (pancake_list[1])
'''
for i in range(len(pancake_list)):
    print(len(pancake_list[i]))
'''

# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
fejlec="Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
print(fejlec)


# 3) Add meg, hogy márciusban ki sütötte a legtöbb palacsintát!

# 1. lista
osszeg = 0
for elso in pancake_list[0]:
    osszeg = osszeg + elso
print(f'Az első lista össege {osszeg}')

# 2. lista
osszeg2 = 0
for masodik in pancake_list[1]:
    osszeg2 = osszeg2 + masodik
print(f' A msáodik lista: {osszeg2}')

# 3. lista
osszeg3 = 0
for harmadik in pancake_list[2]:
    osszeg3 = osszeg3 + harmadik
print(f'A hamradik lista: {osszeg3}')

# 4. lista
osszeg4 = 0
for negyedik in pancake_list[3]:
    osszeg4 = osszeg4 + negyedik
print(f'A negyedik lista: {osszeg4}')

osszesen = [osszeg, osszeg4 , osszeg3, osszeg2]
print(osszesen)



# Aki a legtöbb palacsintát sütötte (while)
# 4) Add meg, hogy ki sütötte az évben a legkevesebb palacsintát!

osszesen[0] = 'Jani'
osszesen[1] = 'Pisti'
osszesen[2] = 'Balázs'
osszesen[3] = 'Dani'

legkisebb = osszesen[0]
legnagyobb = osszesen[0]

for z in osszesen:
    if z > legnagyobb:
        legnagyobb = z
    if z < legkisebb:
        legkisebb = z
print(f'Aki a legtöbb palacsintát sütötte az évben: {legnagyobb}')
print(f'Aki a legkevesebb palacsintát sütötte az évben: {legkisebb}')


# 5) Add meg, hogy az a személy, akinek B-vel kezdődik a neve, Májusban hány palacsintát sütött.
print(osszesen[2])

#Halmaz létrehozása

with open('./adatok/kimenet.txt', 'w', encoding='utf-8') as celfajl:
        print('Ez kerül a fájlba...', file=celfajl)
with open('input.txt', 'a', encoding='utf-8') as input:
    print('Botond: ', file=input)

# 6) Volt-e olyan személy, akinek az évben változó teljesítménye volt?
#       Pl: sütött valamennyit, majd a következő hónapban többet, a következőben az előzőnél kevesebbet stb
#       írd ki a személy nevét!