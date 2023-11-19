'''
print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
összeg = 0

érdemjegy = int(input("Add meg az első érdemjegyedet"))

while érdemjegy != 0:
    darab = darab + 1
    összeg = összeg + érdemjegy
    érdemjegy = int(input("Add meg a következő érdemjegyedet:)"))

if érdemjegy != 0:    
    print(f'A jegyedinek az átalaga: {összeg/darab}')
else:
    print("Nem adtál meg egy érdemjegyet sem!")
'''
'''
    Az ELDÖNTÉS esetében azt vizsgáljuk,
    hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).
    
    A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
lista = [2, 5, 4, 8, 7, 11, 10, 12]
index = 0
talalat = False

while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print("A listában van 3-mal osztható szám, az indexe:", index)
else:
    print("A listában nincs 3-mal osztható szám")
'''

'''
    A KIVÁLASZTÁS esetében azt tudjuk, hogy szerepel (legalább) egy bizonyos tulajdonságú elem 
    az adatsorban (itt a listában), és ennek az elemnek az indexére vagyunk kíváncsiak.

    A program azt vizsgálja, hogy hányadik indexű helyen áll a hárommal osztható szám a listában. 
    Az első ilyen elem előfordulása érdekel bennünket.  
    '''
lista = [2, 5, 4, 8, 9, 11, 10, 12]

index = 0
talalat = False

while not talalat:
    if lista[index] % 16 == 0:
        talalat = True
    index = index + 1
print (f'A listában a 3-mal oszható számank az indexe: {index-1}')