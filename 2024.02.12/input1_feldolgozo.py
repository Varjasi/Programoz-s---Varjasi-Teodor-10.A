autok = []
with open ('input2.txt', 'r', encoding='utf-8') as forrásfájl:
    for sor in forrásfájl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)
print(f'{autok=}')
