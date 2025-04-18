'''
 írj fv-t, mely beolvassa és eltárolja megfelelő adatszerkezetben a file tartalmát! (AdatokBe)
Add meg, hogy "Dóra" hány darab tortát készített! (fel_2)


Add meg, hogy összesen hány tortát készítettek! (fel_5)
'''
adatok  = []
def AdatokBe():
    file = open('adatok.txt', 'r', encoding='utf-8')
    for sor in file:
        adat = sor.strip().split(' ')
        adatok.append(adat)
    file.close()

def fel2():
    for adat in adatok:
        if adat[0] == 'Dóra':
            szamok = list(map(int, adat[1::]))
            print(szamok)
            összeg = 0
            for szam in szamok:
                összeg = összeg + szam
    print(f'Dóra {összeg} darab tortát készített')

#Add meg, hogy "Z" betűvel kezdődő emberek hány darab tortát készítettek a 2. napon! (fel_3)
def fel_3():
    for adat in adatok:
        if adat[0][0] == 'Z':
            szamok = list(map(int, adat[2]))
            print(szamok)
            összeg = 0
            for szam in szamok:
                összeg = összeg + szam
    print(f'A Z betűvel kezdődő emberek {összeg} darab tortát készítettek a 2. napon')

#Add meg, hogy ki készítette a 3. napon a legtöbb tortát! (fel_4)

def fel_4():
    for adat in adatok:
        szamok = list(map(int, adat[3]))
        maximum = szamok[0]
        index = 0
        talalat = False
        while index <= len(szamok) and not talalat:
            for i in szamok:
                if i > maximum:
                    maximum = i
                    talalat = True
            index += 1
    print(maximum)
    print(index)

def fel_5():
    lista = []
    for adat in adatok:
        for szam in adat[1::]:
             lista.append(int(szam))
    összeg = 0
    for i in lista:
        összeg = összeg + i
    print(f'Összesen {összeg} darab tortát készítettek')
        

#Hívások
AdatokBe()        
fel2()
fel_3()
#fel_4()
fel_5()
#print(adatok)
