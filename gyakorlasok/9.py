'''
    A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
    illetve a legnagyobb érték az adatsorban (itt a listában).
    '''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

legkisebb = lista[0]
legnagyobb = lista[0]
for szam in lista:
    if szam < legkisebb:
        legkisebb = szam
    if szam > legnagyobb:
        legnagyobb = szam


print(f'A legkisebb szám: {legkisebb}')
print(f'A legnagyobb szám: {legnagyobb}')
