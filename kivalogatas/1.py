def beolvas(fájlnév):
    fájl = open(fájlnév, encoding="utf-8")
    sorok = fájl.readlines()
    fájl.close()
    return sorok

def feladat1(név):
    lista = beolvas(név)
    összeg = 0
    for i in range(len(lista)):
        összeg += int(lista[i])
    return összeg
def feladat2(név, első, utolsó):
    lista = beolvas(név)
    számok = []
    for i in range(első,len(lista)-utolsó):
        számok.append(int(lista[i].strip()))
    átlag = 0
    for i in range(len(számok)):
        átlag += számok[i]
    return átlag // len(lista)
def feladat3(név, első, utolsó):
    lista = beolvas(név)
    számok = []
    for i in range(első,len(lista)-utolsó):
        számok.append(int(lista[i].strip()))
    mini = 0
    minx = számok[0]
    for i in range(len(számok)):
        if minx > számok[i]:
            mini = i
            minx = számok[i]
    return mini, minx
def feladat4(név, első, utolsó):
    lista = beolvas(név)
    számok = []
    for i in range(első,len(lista)-utolsó):
        számok.append(int(lista[i].strip()))
    maxi = 0
    maxx = számok[0]
    for i in range(len(számok)):
        if maxx > számok[i]:
            maxi = i
            maxx = számok[i]
    return maxi, maxx

print(f"feladat1: [{feladat1("input1")}]")
print(f"feladat2: [{feladat2("input2", 2, 0)}]")
print(f"feladat3: [{feladat3("input3", 1, 1)}]")
print(f"feladat4: [{feladat4("input3", 1, 1)}]")