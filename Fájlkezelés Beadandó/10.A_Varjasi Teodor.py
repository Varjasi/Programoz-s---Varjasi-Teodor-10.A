

def print_menu():
    print("Menüpontok:")
    print("1. Számok összege")
    print("2. Számok soronkénti összege")
    print("3. Számok oszloponkénti összege")
    print("0. Kilépés")

print_menu()

#menu = int(input("Adj meg ezek közül egy meüpontot!"))
lista = []
with open ('input.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        print(type(sor))
        print(sor.strip())
        szamok = sor.strip()
        lista.append(int(szamok[1:3]))

print(lista)
'''
osszeg = 0
while menu != 0:
    if menu == 1:
        for szam in lista:
            osszeg = osszeg + szam
        print(f'A számok összege: {osszeg}')
    menu = int(input("Adj meg ezek közül egy menüpontot!"))

print(lista)
'''