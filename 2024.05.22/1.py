adatok = []
def AdatokBe():
    file = open('adatok.txt', 'r', encoding='utf-8')
    
    for sor in file:
        adat = sor.strip().split(' ')
        print(adat)
        szotar = {'nev': adat[0], 
                  'szamok': adat[1::]}
        print(szotar['nev'])
        
        print(szotar['szamok'])
        összeg = 0
        for szamok in szotar['szamok']:
            szam = (int(szamok))
            összeg = összeg + szam
            adatok.append(szam)
        print(összeg)
        
    
AdatokBe()


