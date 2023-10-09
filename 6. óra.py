'''
szam = int(input("Adj meg egy számot"))
if szam%2==0:
    print ("A szám oszhtható 2-vel")

else:
    print("A szám nem osztható 2-vel")

# Van-e benne a betű?

szo = input('Adj meg egy szót')
index = 0
talalat = False
while index <= len(szo) and not talalat:
    if szo[index] == 'a':
        talalat = True
    index += 1

if talalat:
    print("Az általad megadott szóban található a betű")

else:
    print("Az általad megadott szóban nem található a betű")


# Hány mondatból áll?

szoveg = 'Édesapja Petrovics István (Kartal, 1791. augusztus 15. – Pest, 1849. március 21.) mészárosmester, felvidéki szlovák családból származott[4] (a közhiedelemben elterjedt szerb származással szemben), de ő magyarnak vallotta magát. Apjának szlovák származását valószínűsíti annak evangélikus vallása (a szerbek általában ortodoxok), illetve Kiss József és Jakus Lajos kutatásai, akik apai ágon 1685-ig, a Nyitra vármegyei Vagyócig vezették vissza Petőfi származását. Vagyis a Petrovicsok csakúgy Felvidékről származnak, mint az anyai ág, amely a Turóc vármegyei Necpál községből ered.[5] Apai nagyapja Petrovics Tamás, aki 1770-ben 26 évesen költözött el Aszódra.[6]'
szamlalo = 0
for mondat in szoveg:
    if mondat == '.' or mondat == '!' or mondat == '?':
        szamlalo += 1
print(f'A szövegben {szamlalo} db mondat van.')
'''

# Hogy hívták a legelsőként beérő nőt a futóversenyen?

lista = [
            ["Béla", "f", "18:00"],
            ["Judit", "n", "18:01"], 
            ["Zoli", "f", "18:05"], 
]
for i in range(len(lista)):
    print(lista[i])
'''
for j in range(len(lista[i])):
    print(lista[i][j])
'''
egysor = ''
for j in range(len(lista[i])):
    egysor += lista[i][j] + " "
print(egysor)

i = 0
while (not(lista[i][1]=="n")):
    i += 1
print(lista[i][0])
