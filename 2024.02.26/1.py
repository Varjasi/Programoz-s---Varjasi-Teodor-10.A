
adatok = []
def atlagszamolas():
    with open('2024.02.26\input1.txt', 'r', encoding='utf-8') as celfajl:
        for sor in celfajl:
            adat = sor.strip()
            adatok.append(int(adat))
atlagszamolas()
print(adatok)

darab = 0

eredmeny = 0
for i in adatok:
    eredmeny = eredmeny + i
    darab = darab + 1

print(f'Az átlag: {int(eredmeny/darab)}')

