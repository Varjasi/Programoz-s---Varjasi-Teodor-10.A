szorzatok = []

with open('adatok/szorzatok.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('./adatok/gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            szorzat = int(adatok[0]) * int(adatok[1])
            szorzatok.append(szorzat)
            celfajl.write(str(f' Összeszoroztt számok: {szorzatok[0]}'))

print(f'Összeszorzott számok: {szorzatok}')