lista = []
with open('file.txt', 'r', encoding='UTF-8') as forrásfájl:
    for sor in forrásfájl:
        #print(sor)
        adatok = sor.strip().split(', ')
        eredmeny = adatok[1:3]
        for szo in eredmeny:
            print(szo)       