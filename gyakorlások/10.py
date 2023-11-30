szam = int(input("Adj meg egy számot!"))
lista = []

while szam != '':
    lista.append(szam)
    szam = int(input("Add meg a következő számot!"))

print (lista)