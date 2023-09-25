#Írj függvényt, amely feltölti 0 és 9 közötti számokkal a 28 elemből álló adatszerkezetet
#Írj függvényt, amlly kiírja, hogy hány kókouszgolyót adott el összesen a pékség 
# Í.F., amely kiírja, hogy hányadik hét volt a legjob eladások szempontjából
# Í. F., amely kiírja, hogy hetente hány kókuszgolyót adtak el
# Í.F., amely kiírja, hogy hány eladásmentes nap volt egy héten?
# Í.F., amely megmutatja, hogy melyik naphoz tatozik a legkevesebb páratlan számú eladás?
'''
def osszegzo(szamok):
	osszesen = 0
	for szam in szamok:
		osszesen = osszesen + szam
	print('A listában lévő számok összege: ', osszesen)


szamok = [3, 5, 19, 11, 17, 1]
osszegzo(szamok)
'''
lista = []
import random
a = random.randint(1,9)
b = 0
while b <= 28:
    lista.append(a)
    a = random.randint(1,9)
    b = b + 1
print(lista)

def osszegzo(lista):
    osszesen = 0
    for szam in lista:
        osszesen = osszesen + szam
    print(f'A pékség összesen: {osszesen} kókuszgolyót adott el')

osszegzo(lista)