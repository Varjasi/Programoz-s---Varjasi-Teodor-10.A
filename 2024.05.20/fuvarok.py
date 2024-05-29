adatok = []
def adatokBeolvasása():
    fájl = open('fuvarok.txt', 'r', encoding='utf-8')
    for sor in fájl:
        for oszlop in sor:
            sorok = sor.strip().split(' ')
        return(oszlop)
    fájl.close()

prgram = adatokBeolvasása()
print(prgram)
    