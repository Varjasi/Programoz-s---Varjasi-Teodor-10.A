adatok = []
def adatokbeolvasása():
    file = open('fuvarok.txt', 'r', encoding='utf-8')
    for sor in file:
        for oszlop in sor:
            adat = oszlop.strip().split(' ')
            adatok.append(adat)

adatokbeolvasása()
#print(adatok)
def nullakm():
    összeg = 0
    for sor in adatok:
        print(sor)
        if sor == ['0']:
            összeg = összeg + 1
    return(összeg)
     
eredmeny = nullakm()
print(f'Az adatbázisban {eredmeny} db 0 km havi futásteljesítményt tartalmazó hónap van')
