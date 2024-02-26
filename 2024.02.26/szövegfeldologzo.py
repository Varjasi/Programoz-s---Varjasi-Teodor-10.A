lista = []
with open('2024.02.26\input3.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        lista.append(adatok)

print(lista)       