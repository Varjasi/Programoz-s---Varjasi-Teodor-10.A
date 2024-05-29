jelek = []
def beolvas():
    file = open('jel.txt', 'r', encoding='utf-8')
    for sor in file:
        jel = sor.strip().split(' ')
        jelek.append(list(map(int, jel)))
    file.close()

beolvas()

sorszam = int(input("Add meg a jel sorszámát"))

print(f'X: {jelek[sorszam-1][3]} Y: {jelek[sorszam-1][4]}')
#print(adatok)
print(type(jelek[0]))

def eltelt(jel0, jel1):
    ido = abs(jel1[0] - jel0[0]) * 3600 + abs(jel1[1]-jel0[1]) * 60 + abs(jel1[2]- jel0[2])
    return(ido)
    
kulonbseg = eltelt(jelek[0], jelek[-1])

ora = kulonbseg // 3600
perc = (kulonbseg % 3600) // 60
masodperc = kulonbseg % 3600

print(f'h: {ora} p: {perc} m: {masodperc}')

for jel in jelek:
    print(jel[3])

