#mennyi értékesítés történt összesen egy héten?
napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

osszesen = 0
for ertekesites in napi_ertekesitesek:
    osszesen = osszesen + ertekesites
print(f'Az összes értékesítés, ami ezen a napon történt: {osszesen}')

print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

osszeg = 0
darab = 0
erdemjegy = int(input("Add meg az első érdemjegyedet!"))

while erdemjegy != 0:
    osszeg = osszeg + erdemjegy
    darab = darab + 1
    erdemjegy = int(input("Add meg a következő érdemjegyedet!"))

if darab != 0:
    print(f'Az erdemjegyek átlaga: {osszeg/darab}')
else:
    print("Nem adtál meg egy jegyet sem!")
