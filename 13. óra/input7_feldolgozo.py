file = open("13. óra/input7")
sorok = file.readlines()
file.close

print(sorok)
matrix = []
for i in range(len(sorok)):
    print(sorok[i])
    egysor = sorok[i].strip()
    print(egysor)
    lista = egysor.split(" ")
    print(lista)
    szamsor = []
    for i in range(len(lista)):
        szam = int(lista[i])
        szamsor.append(szam)
    print(szamsor)
    matrix.append(szamsor)

print(matrix)