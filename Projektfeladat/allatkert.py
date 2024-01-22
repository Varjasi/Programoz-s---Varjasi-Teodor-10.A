
# 1. Feladat
intervallum_min=3
intervallum_max=15

x = input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]")
x = int(x)
'''
if x>=intervallum_min and x<=intervallum_max:
    print("Jó számot adtál meg")
else:
    print("Nem jó számot adtál meg")
'''
feltetel = False
while not feltetel:
    x = input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]")
    x = int(x)
    if x>=intervallum_min and x<=intervallum_max:
        feltetel = True

# 2. Feladat

hetnapjai = ["hétfő", "kedd"]
hetek = []
for hetszama in range(x):
    lista = []
    for nap in hetnapjai:
        ert = input(f"Add meg, hogy Hétfőn hány támadás érte az állatkertet")
        lista.append(ert)
        print(lista)
        hetek.append(lista)
print(hetek)

hetek_str = []
for i in range(len(hetek)):
    lista = []
    for j in range(len(hetek[i])):
        lista.append(str(hetek[i] [j]))
    hetek_str.append(lista)
for hetszamlalo in range (len(hetek_str)):
    print(f"{hetszamlalo}.hét: {tamadasok}")
    tamadasok = " ".join(hetek_str[hetszamlalo])


for het_szamlalo in range(len(hetek)):
    str_ = str(het_szamlalo)+". hét"
    for nap_szamlalo in range(len(hetek[i])):
        str_ += str(hetek [het_szamlalo] [nap_szamlalo]) + " "
    print(str_)